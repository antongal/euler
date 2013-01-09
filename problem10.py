import math

# Solution for Problem 10
# http://projecteuler.net/problem=10


# Returns the sum of all the primes below two million
def solve(n):
	res = 2
	for i in xrange(3, n, 2):
		if isPrime(i):
			res += i

	return res



def isPrime(n):
	for i in xrange(2, int(math.sqrt(n)) +1):
		if n % i == 0:
			return False
			
	return True



print solve(2000000)
