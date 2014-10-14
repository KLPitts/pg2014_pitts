import urllib2
import datetime
import numpy as np
import matplotlib.pyplot as plt

class brazos_dis(object):
	"""
	Class to read and plot discharge data
	
	Author
	___________
	Katie Pitts
	Oct 14, 2014
	KLPitts@tamu.edu
	
	"""

	def __init__(self, filename):
		"""Method to read data"""
		self.filename = filename

		website = urllib2.urlopen(filename)
	
		dates = []
		discharges = []
	
		for line in website.readlines():
			data = line.split('\t')
			if (data[0] == 'USGS'):
				year = int(data[2][:4])
				month = int(data[2][5:7])
				day = int(data[2][8:])
		
				date = datetime.date(year,month,day)
				dates.append(date)
		
				try:
					discharge = int(data[3])
					discharge_m3s = discharge*0.0283 	# convert cfs to m^3/s
				except:
					discharge_m3s = np.nan
		
				discharges.append(discharge_m3s)
	
		self.dates = np.array(dates)
		self.discharges = np.array(discharges)
		#return self.dates, self.discharges

	def year_dis(self, chosenyear=2010):
		"""Method to read and plot one year (chosenyear) of data.
		Default is chosenyear=2010"""
		chosendates = []
		chosendischarges = []
		years = np.array([date.year for date in self.dates])
		for i in range(len(self.dates)):
			if years[i] == chosenyear:
				chosendate = self.dates[i]
				chosendis = self.discharges[i]
				chosendates.append(chosendate)
				chosendischarges.append(chosendis)
		return chosendates, chosendischarges
	

	def plot_alldis(self):
		"""Method to plot hydrograph of entire timeseries."""
		plt.plot(self.dates, self.discharges)
		plt.title('Timeseries Hydrograph')
		plt.xlabel('Years')
		plt.ylabel(r'Discharge [$m^{3}/s$]')
		plt.show()
		
	def compositeDis(self, chosenyear):
		"""Method to calculate mean annual hydrograph 
		with dates given for chosenyear."""
		means = []
		stds = []
		chosendates, chosendischarges = self.year_dis(chosenyear)
		for i in range(len(chosendates)):
			month = chosendates[i].month
			day = chosendates[i].day
			annuals = []
			for j in range(len(self.dates)):
				if (self.dates[j].month == month) and (self.dates[j].day == day):
					annuals.append(self.discharges[j])
			means.append(np.nanmean(np.array(annuals)))
			stds.append(np.nanstd(np.array(annuals)))
			
		return means, stds
		
	def plot_composite(self,chosenyear = 2010):
		"""Method to plot mean annual discharge and variability 
		along with chosenyear hydrograph."""
		chosendates, chosendischarges = self.year_dis(chosenyear)
		means, stds = self.compositeDis(chosenyear)
		filldates = np.hstack([[chosendates],[chosendates[::-1]]])
		fillstds = np.concatenate([np.array(means)+np.array(stds),(np.array(means)-np.array(stds))[::-1]])
		
		fig = plt.figure(figsize=(14, 5))
		p=plt.fill(filldates.T,fillstds,'gray',label='One standard deviation')
		plt.plot(chosendates,means,'k-',label='Mean annual hydrograph')
		plt.plot(chosendates,chosendischarges,'r-',label='%s hydrograph'%(chosenyear))
		plt.ylim([0.0,2500.0])
		plt.grid('on')
		plt.xlabel('Dates')
		plt.ylabel(r'Discharge [$m^{3}/s$]')
		plt.legend(loc='best')
		plt.show()


if __name__ == '__main__':
	filename = 'http://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=08116650&referred_module=sw&period=&begin_date=1967-10-01&end_date=2014-10-01'	
	dis = brazos_dis(filename)
	#print dis.year_dis(2012)
	dis.plot_alldis()
	dis.plot_composite(1994)