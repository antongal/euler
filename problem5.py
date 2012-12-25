# Solution for problem 5: Smallest multiple
# http://projecteuler.net/problem=5


# Returns the smallest number that can be divided 
# by each of the numbers from 1 to 10 without any remainder
def solve(n):
	res = n
	
	for i in xrange(n, 2, -1):
		res *= i / gcd(i, res)

	return res


def gcd(a, b):
	if (b == 0):
		return a
	return gcd(b, a % b)


print solve(20)
