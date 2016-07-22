import RollingHash
RollingHash = RollingHash.RollingHash

def KarpRabin(s,t):

	#hashing s
	rs = RollingHash(256,2147483647)
	for c in s: rs.append(c)


	rt = RollingHash(256,2147483647)
	#hashing the string consisting of the first |s| chars
	for c in t[:len(s)]: rt.append(c)
	if(rs.hash() == rt.hash()): return 0

	#sliding
	for i in range(len(s),len(t)):
		rt.skip()
		rt.append(t[i])
		if(rs.hash() == rt.hash()): return i-len(s)+1

	#if we're here, s is not in t
	raise ValueError('substring not found')


assert(KarpRabin("the","the thing we're looking for is here") == 0)
assert(KarpRabin("567","01234567") == 5)
assert(KarpRabin("bcd","abcde") == 1)

#error case
#KarpRabin("not found","")