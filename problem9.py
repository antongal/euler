import math

# Problem 9: Special Pythagorean triplet
# http://projecteuler.net/problem=9


def solve():

	for a in xrange(1, 1000):
		for b in xrange(1, 1000):	

			c1 = math.sqrt(a*a + b*b)
			c2 = 1000 -a -b

			if c1 == c2:
				print a,b,int(c1)
				return a*b*int(c1)

	return -1


print solve()
