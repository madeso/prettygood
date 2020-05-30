#!/usr/bin/env python3

import os


def _CountDirectorySeperators(pattern):
    count = 0
    for c in pattern:
        if c == os.sep:
            count += 1
    return count


class FormatError(Exception):
    pass


class Match:
    isText = False
    data = ""

    def __str__(self):
        if self.isText:
            return self.data.replace("%", "%%")
        else:
            return "%" + self.data + "%"


class Complexity:
    Arguments = 0
    Verifiers = 0

    def __str__(self):
        return "<%(args)s / %(ver)s>" % {"args": self.Arguments, "ver": self.Verifiers}


class KeyValueExtractor:
    def __init__(self):
        self.numberOfDirectorySeperators = 0
        self.matchers = []

    def get_keys(self):
        return [m.data for m in self.matchers if m.isText is False]

    def _getSearchableString(self, path):
        s = ""
        s += os.path.splitext(os.path.basename(path))[0]
        d = os.path.dirname(path)
        for _ in range(0, self.numberOfDirectorySeperators):
            s = os.path.basename(d) + os.sep + s
            d = os.path.dirname(d)
        return s

    def _addText(self, t):
        m = Match()
        m.isText = True
        m.data = t
        self.matchers.append(m)
        self.numberOfDirectorySeperators += _CountDirectorySeperators(t)
        return self


    def _addArgument(self, t):
        m = Match()
        m.isText = False
        m.data = t
        self.matchers.append(m)
        return self
    
    def extract(self, fi):
        t = self._getSearchableString(fi)
        return self._subExtract(t)

    def __str__(self):
        s = ""
        for m in self.matchers:
            s += str(m)
        return s

    def _subExtract(self, text):
        start = 0
        arg = ""
        result = {}
        
        for matcher in self.matchers:
            if matcher.isText:
                end = text.find(matcher.data, start)
                if end == -1:
                    return result, 'Unable to find %(search)s in %(data)s' % {"search": matcher.data,
                                                                              "data": text[start:]}
                
                if arg != "":
                    val = text[start:end]
                    if not self._setVariable(result, arg, val):
                        return result, "Unable to apply <%(val)s> to %(arg)s, already contains <%(src)s>" % \
                               {"val": val, "arg": arg, "src": result[arg]}
                    arg = ""
                start = end + len(matcher.data)
            else:
                if arg != "":
                    raise FormatError()
                arg = matcher.data

        if arg != "":
            val = text[start:]
            if not self._setVariable(result, arg, val):
                return result, "Unable to apply <%(val)s> to %(arg)s, already contains <%(src)s>" % {"val": val,
                                                                                                     "arg": arg,
                                                                                                     "src": result[arg]}
        return result, ""

    @staticmethod
    def _setVariable(container, varname, value):
        if varname in container:
            old = container[varname].lower().replace("_", "").strip().lstrip("0")
            new = value.lower().replace("_", "").strip().lstrip("0")
            if old != new:
                return False
        container[varname] = value
        return True

    # def calculateComplexity(self):
    # counts = {}
    #    for m in self.matchers:
    #        if m.isText == False:
    #            varname = m.data.lower()
    #            c = 0
    #            if varname in counts:
    #                c = counts[varname]
    #            ++c
    #            counts[varname] = c
    #    
    #    cx = Complexity()
    #    cx.Arguments = counts.Count(lambda(x): x.Value > 0)
    #    cx.Verifiers = counts.Count(lambda(x): x.Value > 1)
    #    return cx

    def countInText(self, calculator):
        count = 0
        for m in self.matchers:
            if m.isText:
                count += calculator(m.data)
        return count


def Compile(apattern):
    pattern = os.path.normpath(apattern)
    p = KeyValueExtractor()
    
    k = '%'
    special = False
    mem = ""

    for c in pattern:
        if c == k:
            t = mem
            mem = ""
            if special:
                if t == "":
                    mem += k
                else:
                    p._addArgument(t)
            else:
                if t == "":
                    pass
                else:
                    p._addText(t)
            special = not special
        else:
            mem += c

    if special:
        raise FormatError()
    st = mem
    
    if st != "":
        p._addText(st)
    return p


if __name__ == "__main__":
    t = Compile("%album%/%artist%-%title%")
    print(t)
    print("------------------")
    print(t.extract("songs/crap/Cannibal/Ke$ha-Crazy Beautiful Life.mp3"))
    print(t.extract("songs/One Of The Boys/Katy Perry-I Kissed A Girl.mp3"))
    print(t.extract("All I Ever Wanted/Kelly Clarkson-Long Shot.mp3"))
    print(t.extract("music.mp3"))
    print(t.extract("the las - There she goes again.mp3"))
    
    print("------------------")
    t = Compile("%artist%-%album%/%track%.%title% by %artist%")
    print(t)
    print(t.extract("Miss Li - Beats and bruises/3. My Man by Miss Li.mp3"))
    print(t.extract("Miss Li - Beats and bruises/4. Hit it.mp3"))
    print(t.extract("Miss Li - Beats and bruises/5. Forever Drunk by mis li.mp3"))
