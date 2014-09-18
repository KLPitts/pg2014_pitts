"""Module for functions assigned in homework #1

>>> import HW1
>>> HW1.FunctionName(argument)

Functions to choose from:

Q1: fib(N)
Q2: integrate(f, dx=1.0)
Q3: read_dis(filename)
Q4: read_drifter(filename)

Katie Pitts
OCNG 689
Sept 2014"""


# HW1 Q1

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
	
	
# HW1 Q2

import numpy as np

def integrate(f, dx=1.0):
	"""Function to compute the integral of a list of numbers [f_n(x_n)]
	using the trapezoidal rule with a default value of dx=1.0. 
	Function assumes uniform x grid spacing.
	http://en.wikipedia.org/wiki/Trapezoidal_rule
	
	
	Inputs
	___________
	f = a list of y-values to compute integral under
	dx (optional) = differential of x; the spacing between x grid points.
	Default is dx=1.0.
	
	
	Returns
	___________
	Definite integral of list f, as calculated by trapezoidal rule.
	
	
	Examples
	___________	
	>>> f = [1.0, 3.0, 4.0, 5.0]
	>>> integrate(f)
	10.0

	>>> integrate(f, dx=0.5)
	5.0
	
	
	Author
	___________
	Katie Pitts
	Sept 2014
	KLPitts@tamu.edu
	
	"""
	
	f1 = f[0]
	fn = f[-1]
	trapz = (dx/2)*(f1 + np.sum(f[1:-1])*2 + fn)
	
	return trapz
		

# HW1 Q3

import datetime

def read_dis(filename):
	"""Function to read data from the file discharge.dat,
	return a list of dates (as datetime objects) and 
	discharge (ignoring any flags).
	
	
	Inputs
	___________
	filename = discharge data file (.dat)
	
	
	Returns
	___________
	A list of dates (as datetime objects) 
	and discharge values (ignoring any flags)
	
	
	Examples
	___________	
	>>> dis=read_dis(filename)
	>>> dis[0][0],dis[1][0]
	(datetime.date(1923, 6, 1), 4800)
	
	
	Author
	___________
	Katie Pitts
	Sept 2014
	KLPitts@tamu.edu
	
	"""
	
	f = open(filename)
	
	dates = []
	discharges = []
	
	for line in f.readlines():
		data = line.split('\t')
		if (data[0] == 'USGS'):
			year = int(data[2][:4])
			month = int(data[2][5:7])
			day = int(data[2][8:])
			
			date = datetime.date(year,month,day)
			
			dates.append(date)
			
			discharge = int(data[3].split('_')[0])
			
			discharges.append(discharge)
			
	return [dates, discharges]
	
	
# HW1 Q4

def read_drifter(filename):
	"""Function to read data from the file drifter.dat.  
	Return a dictionary based on the track name as indices, 
	returning a list of lat/lon pairs.
	
	
	Inputs
	___________
	filename = drifter.dat
	
	
	Returns
	___________
	A dictionary based on the track name as indices, 
	returning a list of	lat/lon pairs.
	
	
	Examples
	___________	
	>>> tracks = read_drifter('drifter.dat')
	>>> tracks['FRODO']
	[(43.3232, 121.3132), 
	...
	(43.1313, 121.4546)]
	
	
	Author
	___________
	Katie Pitts
	Sept 2014
	KLPitts@tamu.edu
	
	"""
	
	f = open(filename)
	
	tracks = {}
	names = []
	positions = []
	
	for line in f.readlines():
		data = line.split()
		if data != []:
			if (data[0] == 'Track'):
				if data[1] == 'ACTIVE':
					try: 
						test = int(data[3])
						name = data[1] + ' ' + data[2] + ' ' + data[3]
					except:
						name = data[1] + ' ' + data[2]
				else:
					name = data[1]
				names.append(name)
				positions = []
			elif (data[0] == 'Trackpoint'):
				lat = float(data[1][1:]) + (float(data[2])%100.0)/60.0
				if (data[1][:1] == 'S'):
					lat = lat*(-1)
				lon = float(data[3][1:]) + (float(data[4])%100.0)/60.0
				if (data[3][:1] == 'W'):
					lon = lon*(-1)
				lat = "%.3f" % lat
				lon = "%.3f" % lon					
				positions.append((lat, lon))
				tracks.update({name:positions})
			

	return tracks