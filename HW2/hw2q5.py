# Katie Pitts
# KLPitts@tamu.edu
# 10-16-2014
# HW2, Problem 5, Read and plot topography/bathymetry

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, shiftgrid
from collections import Counter


def read_topo(filename):
	"""
	Function to read the topography/bathymetry of the world using the 
	ETOPO5 surface dataset.
	"""
	
	f = open(filename)
	
	x = []  # longitudes
	y = []  # latitudes
	z = []  # topography
		
	for line in f.readlines():
		data = line.split()
		
		lon = float(data[0])
		lat = float(data[1])
		topo = float(data[2])
		
		x.append(lon)
		y.append(lat)
		z.append(topo)
		
	return x, y, z
	
	
	
if __name__ == '__main__':
	filename = 'global_merged5.txt'										
	lon, lat, topo = read_topo(filename)
	[k for k,numlat in Counter(lat).items() if numlat>1]
	[k for k,numlon in Counter(lon).items() if numlon>1]

	x = np.reshape(lon,(numlon,numlat))
	y = np.reshape(lat,(numlon,numlat))
	z = np.reshape(topo,(numlon,numlat))
		
	m = Basemap(projection='cyl',
		llcrnrlon=-180,
		urcrnrlon=180,
		llcrnrlat=-90,
		urcrnrlat=90)

	fig = plt.figure(figsize=(10, 7))
	plt.title('World Topography')
	pcm = m.pcolormesh(x, y, z, cmap='RdBu_r', vmin=-7000, vmax=7000)
	m.contour(x, y, z, [-1000,0,1000], colors='k', linewidths=[0.5,1,0.5])
	m.drawmeridians(np.arange(-180, 180, 30),
                # dashes=[1, 0],
                labels=[0,0,0,1])
	m.drawparallels(np.arange(-90, 90, 30),
                # dashes=[1, 0],
                labels=[1,0,0,0])
	
	cax = fig.add_axes([0.135, 0.10, 0.750, 0.05])
	cb = plt.colorbar(pcm, cax=cax, 
                  orientation='horizontal')
	cb.set_label('Topography [m]')
	
	plt.show()
