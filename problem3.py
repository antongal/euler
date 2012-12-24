# A naive and inefficient solution for problem 3
# Largest Prime Factor: http://projecteuler.net/problem=3

import math

#Returns the largest prime factor of n
def solve(n):
	largest = 1
	
	if isPrime(n):
		return n

	root = int(math.floor(math.sqrt(n)))
	for i in xrange(root, 2, -1):
		if n % i == 0 and isPrime(i):
			largest = i
			break
	return largest

def isPrime(n):
	if n % 2 == 0:
		return False

	for i in xrange(3, int(math.floor(math.sqrt(n))), 2):
		if n % i == 0:
			return False
	return True


print solve(600851475143L)
