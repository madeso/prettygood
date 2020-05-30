#!/usr/bin/env python3

#format:
# %arg% replaces arg with its value, error if missing
# [arg] replaces arg with its value, "" if missing
# $func(arg,arg,arg) calls func

class MissingFunction(Exception):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class MissingAttribute(Exception):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class SyntaxError(Exception):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class InvalidState(Exception):
    pass

class _Node:
    def __init__(self):
        pass
    def eval(self, funcs, data):
        pass

class _Text(_Node):
    def __init__(self, text):
        self.text = text
    def eval(self, funcs, data):
        return self.text

class _Attribute(_Node):
    def __init__(self, name):
        self.name = name
    def eval(self, funcs, data):
        if self.name in data:
            return data[self.name]
        else:
            return ""

class _FunctionCall(_Node):
    def __init__(self, name, args):
        self.name = name
        self.args = []
        for a in args:
            self.args.append( _CompileList(a) )
    def eval(self, funcs, data):
        if self.name in funcs:
            args = []
            for a in self.args:
                args.append(a.eval(funcs, data))
            return funcs[self.name](args)
        else:
            raise MissingFunction(self.name)

class _List(_Node):
    def __init__(self, nodes):
        self.nodes = nodes
    def eval(self, funcs, data):
        r = ""
        for n in self.nodes:
            r += n.eval(funcs, data)
        return r

def _ParseArguments(start, pattern):
    ''' return new index, and a list of string arguments that need to be parsed'''
    args = []
    state = 0
    mem = ""
    for i in range(start, len(pattern)):
        c = pattern[i]
        if c == _Syntax.BEGINSIGN:
            mem += c
            state += 1
        elif c == _Syntax.ENDSIGN:
            if state == 0:
                if mem != "":
                    args.append(mem)
                return i, args
            else:
                mem += c
            state -= 1
        elif c == _Syntax.SEPSIGN:
            if state == 0:
                args.append(mem)
                mem = ""
            else:
                mem += c
        else:
            mem += c
    raise SyntaxError("should have detected an end before eos")

class State:
    TEXT = 0
    VAR = 1
    FUNC = 2
    
class _Syntax:
    VARSIGN = '%'
    FUNCSIGN = '$'
    BEGINSIGN = '('
    ENDSIGN = ')'
    SEPSIGN = ','
        
class _Parser:
    def __init__(self):
        self.mem = ""
        self.nodes = []
    
    def doit(self, pattern):
        self.state = State.TEXT
        i = 0
        while i < len(pattern):
            c = pattern[i]
            i += 1
            if self.state == State.TEXT:
                if c == _Syntax.VARSIGN:
                    self.add()
                    self.state = State.VAR
                elif c == _Syntax.FUNCSIGN:
                    self.add()
                    self.state = State.FUNC
                else:
                    self.mem += c
            elif self.state == State.VAR:
                if c == _Syntax.VARSIGN:
                    self.add()
                    self.state = State.TEXT
                else:
                    self.mem += c
            elif self.state == State.FUNC:
                if self.mem == "":
                    if c.isalpha():
                        self.mem += c
                    else:
                        raise SyntaxError("function name is empty")
                else:
                    if c.isalnum():
                        self.mem += c
                    elif c == _Syntax.BEGINSIGN:
                        i, args = _ParseArguments(i, pattern)
                        i += 1
                        self.add(args)
                        self.state = State.TEXT
                    else:
                        raise SyntaxError("function calls must end with () and, mus begin with a letter and can only continue with alphanumerics")
            else:
                raise InvalidState
        if self.mem != "":
            self.add()
        return self.nodes
    
    def add(self, args=None):
        if self.state == State.TEXT:
            if self.mem != "":
                self.nodes.append(_Text(self.mem))
        elif self.state == State.VAR:
            if self.mem != "":
                self.nodes.append(_Attribute(self.mem))
            else:
                raise SyntaxError("varsign?")
                # self.nodes.append(_Text(_Parser.VARSIGN))
        elif self.state == State.FUNC:
            if args == None:
                raise SyntaxError("weird func call")
            self.nodes.append(_FunctionCall(self.mem, args))
        else:
            raise InvalidState
        self.mem = ""

def _CompileList(patt):
    p = _Parser()
    return _List(p.doit(patt))

class _Pattern:
    def __init__(self, patt):
        self.list = _CompileList(patt)
    def eval(self, funcs, data):
        return self.list.eval(funcs, data)

def Compile(pattern):
    return _Pattern(pattern)

def _opt(args, i, d=None):
    if len(args)>i:
        return args[i]
    else:
        return d

def DefaultFunctions():
    return {
      "title": lambda args: args[0].title()
    , "capitalize": lambda args: args[0].capitalize()
    , "lower": lambda args: args[0].lower()
    , "upper": lambda args: args[0].upper()
    , "swapcase": lambda args: args[0].swapcase()
    , "rtrim": lambda args: args[0].rstrip(_opt(args,1))
    , "ltrim": lambda args: args[0].lstrip(_opt(args,1))
    , "trim": lambda args: args[0].strip(_opt(args,1))
    , "zfill": lambda args: args[0].zfill(int(_opt(args,1, "8")))
    , "replace": lambda args: args[0].replace(args[1], args[2], _opt(args, 3))
    }


if __name__ == "__main__":
    data = {"artist":"Zynic", "title":"dreams in black and white", "album":"Dreams", "track":"1"}
    print(Compile("%artist% - %title% (%album%)").eval(DefaultFunctions(), data))
    print(Compile("%artist% - $title(%title%) (%album%)").eval(DefaultFunctions(), data))
    print(Compile("$zfill(%track%,3). $title(%title%)").eval(DefaultFunctions(), data))
    #print _ParseArguments(0, "a,b(1, 3),c)")
