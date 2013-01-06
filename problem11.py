# Solution for Problem 11
# http://projecteuler.net/problem=11

# This is a straightforward solution for this problem, the downsde is that it computes same
# products multiple times, but for this size 20x20 is quite fast.

# reads the matrix from in_f and
# returns the greatest product of four adjacent numbers in 
# the same direction (up, down, left, right, or diagonally) 
def solve(in_f):
	f = open(in_f)
	
	row = 0
	col = 0
	m = []
	for line in f:
		row = []
		for num in line.split(' '):
			row.append(int(num))
		m.append(row)
	
	return max(horizontal_max(m), vertical_max(m), diagonal_max(m))
	
	
def horizontal_max(m):
	max_prod = 0
	for row in xrange(0, len(m)):
		for col in xrange(0, len(m[row])-4):
			max_prod = max(max_prod, f(m, (row, col), (row, col+1), (row, col+2), (row, col+3)))
			
	return max_prod


def vertical_max(m):
	max_prod = 0
	for row in xrange(0, len(m)-4):
		for col in xrange(0, len(m[row])):
			max_prod = max(max_prod, f(m, (row, col), (row+1, col), (row+2, col), (row+3, col)))

	return max_prod
	

def diagonal_max(m):
	max_prod = 0
	# right diagonals
	for row in xrange(0, len(m)-4):
		for col in xrange(0, len(m[row])-4):
			max_prod = max(max_prod, f(m, (row, col), (row+1, col+1), (row+2, col+2), (row+3, col+3)))
			
	#left diagonals
	for row in xrange(0, len(m)-4):
		for col in xrange(0, len(m[row])):
			max_prod = max(max_prod, f(m, (row, col), (row+1, col-1), (row+2, col-2), (row+3, col-3)))
			
	return max_prod
	
	
# this is the function to maximize
# m = matrix
# i, j, k, l = tuples representing the coordinates of elements to evaluate
def f(m, i, j, k, l):
	return m[i[0]][i[1]] * m[j[0]][j[1]] * m[k[0]][k[1]] * m[l[0]][l[1]]



print solve("problem11/input.txt")
