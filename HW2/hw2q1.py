import numpy as np

def distance(N, M):
	"""Function that returns an NxM matrix that defines the distance between
	each of the points in one array to each of the points in another array.

	Inputs
	___________
	Two arrays of points with shapes (N, 2) and (M, 2).
	
	Returns
	___________
	NxM matrix that defines the distance between each of the points in one 
	array to each of the points in the other array.
	
	Examples
	___________
	>>> N = np.array([[5,6],[6,7],[7,8]])
	>>> M = np.array([[1,2],[2,3]])
	>>> dist = distance(N,M)
	>>> print dist
	[[ 5.65685425  4.24264069]
	[ 7.07106781  5.65685425]
	[ 8.48528137  7.07106781]]

	
	Author
	___________
	Katie Pitts
	Oct 14, 2014
	KLPitts@tamu.edu
	
	"""

	d = np.sqrt( (N[:,0, np.newaxis] - M[:,0])**2 + (N[:,1, np.newaxis] - M[:,1])**2 )
	return d


if __name__ == '__main__':
	N = np.array([[5,6],[6,7],[7,8]])
	M = np.array([[1,2],[2,3]])
	dist = distance(N,M)
	print dist