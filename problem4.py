# Solution for problem 4: "Largest Palindrom Product"
# http://projecteuler.net/problem=4

# First approach
def solve1():
	nums = []
	
	for a in xrange(999, 100, -1):
		for b in xrange(999, a, -1):
			if isPalindromic(a*b):
				nums.append(a*b)
	
	return max(nums)

# This implementation is faster than solve1() because it breaks
# when a*b is smaller than the largest palindrome found
def solve2():
	largest = 99*99
	
	for a in xrange(999, 100, -1):
		for b in xrange(999, a, -1):
			if a*b <= largest:
				break
				
			if isPalindromic(a*b):
				largest = a*b
	
	return largest


def isPalindromic(n):
	return str(n) == str(n)[::-1]


print solve1()
print solve2()
