import math

# Solution for Problem 7: 10001st prime
# http://projecteuler.net/problem=7

# Returns the n-th prime number
def solve(n):
	
	primes = 1
	i = 1
	
	while primes < n:
		i += 2
		if isPrime(i):
			primes += 1

	return i


def isPrime(n):
	for i in xrange(2, int(math.ceil(math.sqrt(n))) +1):
		if n % i == 0:
			return False
	return True

print solve(10001)
