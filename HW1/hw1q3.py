# Katie Pitts
# KLPitts@tamu.edu
# 10-16-2014
# HW1, Problem 3, Discharge data

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
			
	return dates, discharges
	
	
if __name__ == '__main__':
	filename = 'discharge.dat'
	dis=read_dis(filename)
	print 'First 5 discharge dates and values: ', dis[0][0:5], dis[1][0:5]