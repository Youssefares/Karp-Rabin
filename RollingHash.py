from collections import deque


class RollingHash:
	'#todo'

	def __init__(self, base, prime):
		self.base = base
		self.prime = prime
		self.h = 0
		self.magic = 1
		self.string = deque('')

	def hash(self):
		return self.h;

	def append(self,val):
		self.h = (self.h*self.base + ord(val))%self.prime
		self.magic = (self.magic*self.base)%self.prime
		self.string.append(val)

	def skip(self):
		#todo: update hash & magic
		val = self.string[0]
		self.string.popleft()


r = RollingHash(256,2147483647)
r.append('b')
r.append('c')

print(r.hash())