def RemoveEmpty(p):
    for s in p:    
        if s != "":
            yield s

def Unique(strings):
    list = []
    for s in strings:
        if s not in list:
            list.append(s)
    return list


def FirstChars(s, count, extra="..."):
    l = len(s)
    if l + len(extra) > count:
        return s[0: count - len(extra)] + extra
    else:
        return s

def RemoveFromEndIfFound(str, extra):
    if str.endswith(extra):
        return str[0:len(str)-len(extra)]
    else:
        return str
def RemoveLeadingZeros(s):
    return s.strip().lstrip('0')


def CountCharacters(s, count):
    n = 0
    for c in s:
        if count(c):
            n+=1
    return n

# http://www.stereopsis.com/strcmp4humans.html
def Compare(sa, sb):
    if sa == sb:
        return 0

    a = CharPointer(sa)
    b = CharPointer(sb)

    while a.hasMore() and b.hasMore(): 
        # a0, b0 will contain either a number or a letter

        if a.Char.isdigit(): 
            a0 = parsenum(a) + 256
         else:
            a0 = a.Char.lower()
        
        if b.Char.isdigit(): 
            b0 = parsenum(b) + 256
         else:  
            b0 = b.Char.lower()
        

        if a0 < b0:
            return -1
        if a0 > b0:
            return 1

        a.next()
        b.next()
    

    if a.hasMore():
        return 1
    if b.hasMore():
        return -1

    return 0


class CharPointer:
    def __init__(self, String="", Index=0):
        self.String = String
        self.Index = Index

    @property
    def Char(self):
            return self.String[self.Index]
    
    def next(self):    
        self.Index+=1
    
    def prev(self):
        self.Index-=1
        
    def hasMore(self):
        return self.Index < len(self.String)

def parsenum(a):
    result = int(a.Char)
    a.next()

    while a.hasMore() and a.Char.isdigit():
        result *= 10
        result += int(a.Char)
        a.next()

    a.prev()
    return result


if __name__ == "__main__":
    print sorted(["berit", "anna", "anna 1", "anna 02", "anna 003", "anna4"], cmp=Compare)
    print CountCharacters("anna", lambda(c): c=='a')
    print RemoveLeadingZeros("007")
    print RemoveFromEndIfFound("hello:", ':')
    print RemoveFromEndIfFound("hello world", ':')
    print FirstChars("hello world", 8)
    print Unique(["a", "b", "a", "c" , "b", "a"])
    print list(RemoveEmpty(["a", "", "b", "", "", "c"]))