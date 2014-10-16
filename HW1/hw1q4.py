# Katie Pitts
# KLPitts@tamu.edu
# 10-16-2014
# HW1, Problem 4, Drifter data

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
	
	
if __name__=='__main__':
	tracks = read_drifter('drifter.dat')
	print 'Gandalf drifter track: ', tracks['GANDALF']