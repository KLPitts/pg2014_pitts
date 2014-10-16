# Katie Pitts
# KLPitts@tamu.edu
# 10-16-2014
# HW2, Problem 3, High pass filter

import numpy as np
import matplotlib.pyplot as plt


def HighPass(x, y, N=1):
	"""
	A 'high-pass' filter function that removes a trend from a given 
	series of points using a polynomial fit of order N.
	
	Inputs
	___________
	x and y values of a function
	N = order of polynomial fit. Default is N = 1.
	
	Returns
	___________
	The difference between the given series and the polynomial fit.
	"""
	
	sol = np.polynomial.Polynomial.fit(x, y, N)
	trend = sol(x)
	return y - trend
	
	
if __name__ == '__main__':
	N = 4
	x = 5 * np.random.rand(1000)
	noise = 20 * np.random.randn(1000)
	y = -0.3*x**4 - 0.9*x**3 + 0.1*x**2 - 0.7*x + noise
	
	detrend = HighPass(x, y, N)
	
	plt.plot(x,y,'k.', label='Polynomial')
	plt.plot(x, detrend,'b.', label='Detrended polynomial')
	plt.legend(loc='best')
	plt.show()