# Solution for problem 6: Sum square difference
# http://projecteuler.net/problem=6

def solve(n):
	sum_of_squares = n*(n+1)*(2*n+1)/6
		
	square_of_sum = n*(n+1)/2
	square_of_sum *= square_of_sum
	
	return abs(sum_of_squares - square_of_sum)


print solve(100)
