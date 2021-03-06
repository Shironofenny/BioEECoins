class OKByte32():

	def __init__(self, length = 0):
		self.data = bytearray(length*2)

	def append(self, appendedByte):
		self.data.append(appendedByte/256)
		self.data.append(appendedByte%256)

	def __getitem__(self, index):
		if isinstance(index, int):
			return (self.data[index*2] * 256 + self.data[index*2+1])
		elif isinstance(index, slice):
			start, stop, step = index.indices(len(self.dat))
			return [ (self.data[i*2] * 256 + self.data[i*2+1]) for i in range(start, stop, step) ]
		else :
			raise TypeError("Index must be either int or slice")

	def __setitem__(self, index, value):
		if ( not isinstance(value, int) ):
			raise TypeError("Value must be an integer")
		else :
			if isinstance(index, int):
				self.data[index*2] = value/256
				self.data[index*2+1] = value%256
			elif isinstance(index, slice):
				start, stop, step = index.indices(len(self.dat))
				for i in range(start, stop, step): 
					self.data[i*2] = value(i)/256
					self.data[i*2+1] = value(i)%256
			else :
				raise TypeError("Index must be either int or slice")

	def toByteArray(self):
		return self.data
