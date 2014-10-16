# Katie Pitts
# KLPitts@tamu.edu
# 10-16-2014
# HW1, Problem 2, Trapezoidal integration

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
	"""
	
	f1 = f[0]
	fn = f[-1]
	trapz = (dx/2)*(f1 + np.sum(f[1:-1])*2 + fn)
	
	return trapz
		

if __name__ == '__main__':
	f = [1.0, 3.0, 4.0, 5.0]
	print 'Given f: ', f
	print 'Trapezoial integration: ', integrate(f)
	print 'If dx=0.5, integration: ', integrate(f, dx=0.5)