def Enumerate(*args):
	for a in args:
		yield a

def IsEmpty(e):
	for a in e:
		return False
	return True

def Remove(e, isValid):
	for t in e:
		if isValid(t):
			yield t

def Convert(e, c):
	for a in e:
		yield c(a)

def GetOrNull(t, isValid, invalid=None):
	if isValid(t):
		return t
	else:
		return invalid
