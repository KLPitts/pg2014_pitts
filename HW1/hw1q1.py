# Katie Pitts
# KLPitts@tamu.edu
# 10-16-2014
# HW1, Problem 1, Fibonacci numbers

def fib(N):
	"""Function to return a list of N Fibonacci numbers
	http://en.wikipedia.org/wiki/Fibonacci_number
	
	
	Inputs
	___________
	N = number of Fibonacci numbers to be returned, 
	starting with beginning of Fibonacci sequence.
	
	
	Returns
	___________
	Returns list of N Fibonacci numbers, starting with 1
	"""
	
	F = [0, 1]
	
	if N > 1:
		for i in range(2, N+1):
			next = F[i-1] + F[i-2]
			F.append(next)
			
	return F[1:N+1]
	
	
if __name__ == '__main__':
	print 'List of 1 Fibonacci numbers: ', fib(1)
	print 'List of 2 Fibonacci numbers: ', fib(2)
	print 'List of 6 Fibonacci numbers: ', fib(6)