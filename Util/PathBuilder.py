kExtraInvalidCharacters = ".:\' !?()#,&"

def _InvalidPathCharacters():
	for c in System.IO.Path.GetInvalidPathChars():
		yield c
	for c in kExtraInvalidCharacters:
		yield c

def _InvalidFileCharacters():
	for c in System.IO.Path.GetInvalidFileNameChars():
		yield c
	for c in kExtraInvalidCharacters:
		yield c

class PathBuilder:
	def __init__(self, path):
		self._dir = path

	def subdir(self, name):
		safe = name
		
		for c in _InvalidPathCharacters():
			safe = safe.replace(c, '_')
		
		return PathBuilder(Path.Combine(self._dir, safe))

	@property
	def path(self):
		return self._dir
	
	def __str__(self):
		return self._dir

	def file(self, name, extention):
		safe = name
		for c in _InvalidFileCharacters():
			safe = safe.Replace(c, '_')
		
		return Path.ChangeExtension(Path.Combine(self._dir, safe), extention)
