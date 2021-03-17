########################################################################
#	Conner I Sandefur 												   #
#	Created: 12/21/2020												   #
#	Updated: 01/11/2021												   #
# 	Description: Class ExpData contains all information about a 	   #
#			experimental data set file 								   #
########################################################################

# import statements
import sample as s
import matplotlib.pyplot as plt

class ExpData(object):
	"""Class to store experimental time series data
	    name: experimental data set name
	    type: cell type / (model) organisms
	    desc: description of data set
	    units: unit of experimental data value
	    timeUnits: unit of time
	    samples = list of class Sample objects
	"""


	


	def __init__(self, efile):
		"""Initialize this ExpData instance by:
			opening efile, which is of the following format:
			# experimental data set name
			# cell type / model organism
			# description
			# unit of experimental data value
			# header line (time\tavg_celltype_name1\tsd_celltype_name1
			where absent data is represented as NA
			and then setting up the experimental data set arrays
		"""
		# setup experimental data set name
		f = open(efile, 'r')
		self.name = ((f.readline()).lstrip('#')).rstrip('\n')
		print ('Importing data set: ' + self.name)

		# load cell type / model organism
		self.type = ((f.readline()).lstrip('#')).rstrip('\n')
		print ('Importing cell type / model organism: ' + self.type)

		# load description
		self.desc = ((f.readline()).lstrip('#')).rstrip('\n')
		print ('Importing description: ' + self.desc)

		# load units
		self.units = (((f.readline()).lstrip('#')).rstrip('\n')).strip()
		print ('Importing units: ' + self.units)

		# load header line and read in sample names
		header = (f.readline().strip('\n')).split('\t')
		numSamples = int((len(header) - 1)/2)
		print('Importing ' + str(numSamples) + ' samples')
		
		# set time units
		self.timeUnits = header[0].split('_')[1].strip()
		#  initialize a list of Sample objects with names and data units
		self.samples = list()
		for i in range(0,numSamples):
			self.samples.append(s.Sample(header[i*2+1].split('_')[2], self.units))
			print ('name of sample: ' + self.samples[i].get_name())
			print ('units of sample: ' + self.samples[i].get_units())
			self.samples[i].set_timeUnits(self.timeUnits)
		
		# capture time points and experimental data points into self.samples list
		for l in f:
			items = l.split('\t')
			for i in range(0,len(self.samples)):
				#print ('At sample #: ' + str(i))
				self.samples[i].append_time(items[0])
				self.samples[i].append_avg(items[i*2+1])
				self.samples[i].append_sd(items[i*2+2])
				#print(len(items))
				#print(items[len(items)-1])
				if (len(items) > i*2+2):
				    self.samples[i].append_timeLabel(items[len(items)-1])
		
		
		
	def get_samples(self):
	    return self.samples
	
	def plot_samples(self):
	  
	    # adjust plotting parameters
	    fs = 18 #font size
	    lw = 4	# line width
	    parameters = {'axes.labelsize': fs,
        	'axes.labelweight': 'bold',
        	'axes.linewidth' : lw,
        	'axes.titlesize': fs,
        	'axes.titleweight': 'bold',
        	'xtick.labelsize': fs,
        	'axes.spines.top': False,
        	'axes.spines.right': False,
        	'ytick.labelsize': fs,
        	'font.weight': 'bold',
        	'legend.fontsize': 18
	    }
	    plt.rcParams.update(parameters)
	    # determine number of samples to plot
	    numToPlot = len(self.samples)
	    toPlot = self.samples
	    # plot 4 samples at a time
	    i = 0 # index of sample to plot
	    numFigs = 0
	    while i < numToPlot:
	        # for each figure
	        for r in range(0,2):
	            for c in range (0,2):
	                if ( (r==0) and (c==0)) :
	                    # create new figure
	                    numFigs = numFigs + 1
	                    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15,15))
	                    fig.suptitle('Exp Data samples list, plot ' + str(numFigs) , fontsize=fs, fontweight='bold')
	                curAx = axes[r][c]
	                if (i < numToPlot):
	                    time = self.samples[i].get_time()
	                    avg = self.samples[i].get_avg()
	                    sd = self.samples[i].get_sd()
	                    curAx.errorbar(time, avg, fmt='o', markersize=4,
	                        color='black', ecolor='gray')
	                    curAx.set_xlabel('Time (' + self.samples[i].get_timeUnits() + ')')
	                    curAx.set_ylabel(self.samples[i].get_units())
	                    curAx.set_title('Sample: ' + self.samples[i].get_name())
	                else:
	                    curAx.axis("Off")
	                i = i + 1
	                
	        plt.subplots_adjust(top=0.88, bottom=0.107,
			    left = 0.093, right = 0.933,
			    wspace=0.352, hspace = 0.32)
	        plt.show()