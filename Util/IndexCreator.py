class IndexCreator:
	def __init__(self):
		self._index = 0
	
	def generate(self):
		r = self._index
		self._index += 1
		return r
	
	def clear(self):
		self._index = 0

if __name__ == "__main__":
	i = IndexCreator()
	print i.generate(), i.generate(), i.generate(), i.generate()
	i.clear()
	print i.generate(), i.generate(), i.generate(), i.generate()