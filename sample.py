########################################################################
#	Conner I Sandefur 												   #
#	Created: 12/21/2020												   #
#	Updated: 03/15/2021												   #
# 	Description: Class Sample contains all information about a 	       #
#			sample from an experimental data set file 				   #
########################################################################

# import statements
import numpy as np

class Sample(object):
		"""Class to store information about one sample of
			experimental time series data:
			name
			time
			time units
			average data points
			standard deviation data points
			units
			symbol of associated model variable (via mapping file)
		"""

		def __init__(self, name, units):
			"""Initialize sample with a name and units
				and empty lists for time, avg, and sd
			"""
			self.name = name
			self.units = units
			self.time = list()
			self.avg = list()
			self.sd = list()
			self.timeLabels = list()
			self.symbol = 'NaN'


		def __str__(self):
			lines = list()
			lines.append(self.name + ' (' + self.units + ')\n')
			lines.append('time ' + '(' + self.timeUnits + ')' +
				  '\taverage\tstd dev\n')
			for i in range(0, len(self.time)):
				lines.append(self.time[i] + '\t' +
					str(self.avg[i]) + '\t' +
					str(self.sd[i]) + '\n'
				)
			return ''.join(lines)


		def get_name(self):
			"""Return name of this sample"""
			return self.name


		def get_units(self):
			"""Return units for this sample"""
			return self.units
			
		def get_timeUnits(self):
			"""Return units for this sample"""
			return self.timeUnits
	
		
		def get_timeLabels(self):
			"""Return units for this sample"""
			return self.timeLabels
			
		def get_time(self):
		    """Return time array for this sample"""
		    return self.time
		    
		    
		def get_avg(self):
		    """Return average array for this sample"""
		    return self.avg
		    
		    
		def get_sd(self):
		    """Return sd array for this sample"""
		    return self.sd


		def append_time(self, time):
			"""Sets the time points array for this sample"""
			self.time.append(float(time.strip()))
		def append_timeLabel(self, label):
		    """Sets the time label array for this sample"""
		    self.timeLabels.append(label.strip())




		def set_timeUnits(self, timeUnits):
			"""Sets the time units for this sample"""
			self.timeUnits = timeUnits


		def append_avg(self, avg):
			"""Sets the average data points array for this sample"""
			if (avg.strip() != "NA"):
				self.avg.append(float(avg.strip()))
			else:
				self.avg.append(np.nan)


		def append_sd(self, sd):
			"""Sets the standard deviation points for this sample"""
			sd = sd.strip('\n')
			if (sd != ''):
				if (sd != "NA"):
					self.sd.append(float(sd.strip()))
				else:
					self.sd.append(np.nan)


		def set_units(self, units):
			"""Sets the units for this sample"""
			self.units = units
			
		def set_symbol(self, symbol):
			"""Set the model variable symbol associated with this sample"""
			self.symbol = symbol
			#print(symbol)
			
		def get_symbol(self):
			"""Get the model variable symbol associated with this sample"""
			return self.symbol
		
