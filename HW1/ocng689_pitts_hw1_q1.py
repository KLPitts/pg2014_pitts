def fib(N):
	"""Function to return a list of N Fibonacci numbers
	http://en.wikipedia.org/wiki/Fibonacci_number
	
	
	Inputs
	___________
	N = number of Fibonacci numbers to be returned, 
	starting with beginning of Fibonacci sequence.
	
	
	Examples
	___________
	>>> fib(1)
	[1]

	>>> fib(2)
	[1, 1]

	>>> fib(6)
	[1, 1, 2, 3, 5, 8]
	
	
	Author
	___________
	Katie Pitts
	Sept 2014
	KLPitts@tamu.edu
	
	
	"""
	
	F = [0, 1]
	
	if N > 1:
		for i in range(2, N+1):
			next = F[i-1] + F[i-2]
			F.append(next)
			
	return F[1:N+1]