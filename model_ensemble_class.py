########################################################################
#	Conner I Sandefur 												   #
#	Created: 02/23/2021												   #
#	Updated: 03/17/2021												   #
# 	Description: Class Model_Ensemble contains all information about   #
#			one or more instances of class Model and one more more 	   #
#			instances of class ExpData								   #
########################################################################

# import statements
import model as mod_class
import expdata as exp
import matplotlib.pyplot as plt

#from  import data

class Model_Ensemble_Class(object):
  """Class containing all information about an ensemble model and
		associated experimental/observational data :

        self.data: experimental data set in expfile
	"""
  def __init__(self, expfile, mapfile, outfile, efile, step, runToSS, cfile = None, sep='\t'):
    """Initialize this Model_Ensemble instance by: loading experimental data from expdata file
    """
    # load the experimental data
    self.data = exp.ExpData(expfile)# get the list of experimental data
    samples = self.data.get_samples()# print samples to screen
    for i in range(0,len(samples)):
      print('Sample #' + str(i) + ' is '+ samples[i].get_name())
    self.data.plot_samples()
    
    # map variables to experimental data
    f = open(mapfile, 'r') # open mapping file
    f.readline() # read in experimental data file line
    f.readline() # read in model file line
    for l in f: # for each line in the file
      #print(l)
      for i in range(0, len(samples)):
      	#print(samples[i].get_name())
      	#print(l.split(',')[1].strip('\n').strip(' '))
      	if (samples[i].get_name() == l.split(',')[1].strip('\n').strip(' ')):
        	#print('found match')
        	#print(l.split(',')[0])
        	samples[i].set_symbol(str(l.split(',')[0]))
        	#print(samples[i].get_symbol())
        	break
        	
    f.close()
    
    for i in range(0,len(samples)):
    	print('Sample #' + str(i) + ' is ' + samples[i].get_name() + ' and maps to model variable ' + samples[i].get_symbol())
      
    # initialize list of models
    models = list()
    # initialize a single model instance
    aModelInstance = mod_class.Model(efile, step, runToSS, cfile, sep)
    models.append(aModelInstance)
    variables = aModelInstance.get_vars()
    
    # print variables to screen
    for i in range(0,len(variables)):
      print('Variable #' + str(i) + ' is ' + variables[i].get_symbol())
      
    
    # create initial conditions based on experimental data set
    expindices = list()
    expics = list()
    eqs = aModelInstance.get_eqs()
    for i in range(0, len(eqs)): # for each equation in this model instance:
      # for each sample
      j = 0
      for s in samples: # for each experimental data sample
        if (s.get_symbol() == eqs[i].get_symbol()):
          print('Comparing sample ' + s.get_name() + ' with variable ' + eqs[i].get_symbol()) 
          expindices.append(i)
          expics.append(samples[j].get_avg()[0])
        j = j + 1
    #expindices = [1, 2, 3]
    #expics = [samples[0].get_avg()[0], samples[1].get_avg()[0], samples[2].get_avg()[0]]
    #print(samples[0].get_avg()[0])
    
    # run model
    
    aModelInstance.run_model(samples[0].get_time(), expindices, expics)
    
    # calculate score
    score = self.calculate_score(aModelInstance)
    print("Calculated RMSD: " + str(score))
    aModelInstance.set_score(score)
    
    
    # plot variables and simulations together
    print('Plotting model and samples together')
    self.plot_fit(aModelInstance)
    
    aModelInstance.sim_print_to_file(outfile)
    	
      
    # plot variables
    #self.data.plot_samples()

  def calculate_score(self, aModel):
  	"""Method to calculate a score comparing simulation with experimental/observational data"""
  	score = 0
  	rmsd = 0
  	samples = self.data.get_samples()
  	eqs = aModel.get_eqs()
  	for i in range(0, len(eqs)): # for each equation in this model instance:
  		# for each sample
  		for s in samples: # for each experimental data sample
  			if (s.get_symbol() == eqs[i].get_symbol()):
  				#print('Comparing sample ' + s.get_name() + ' with variable ' + eqs[i].get_symbol()) 
  				# get sample and simulation time units
  				#print('Sample time is ' + s.get_timeUnits() + ' and simulation time is ' + variables[len(variables)-1].get_units())
  				# compare the sample to the variable for each sample time point
  				sample_time = s.get_time()
  				sim_time = aModel.get_time()
  				sim_results = aModel.get_results()  		
  				
  				# scale sample --> s_scaled = (s_avg - sample_min)/(sample_max - sample_min)
  				# scale sim_results --> s
  					 	
  				# compare the sample to the variable for each sample time point
  				s_t = 0 # sample_time index
  				for t in range(0, len(sim_time)): # for each simulated time point
  					#print(t)
  					#print(sample_time[s_t])
  					if sample_time[s_t] == sim_time[t]:
  						#print('Sample time = ' + str(sample_time[s_t]) + ' and sim time =  ' + str(sim_time[t]))
  						#print('Simulation results = ' + str(sim_results[i][int(t)]))
  						#print('Sample results = ' + str(s.get_avg()[s_t]))
  						score = score + (sim_results[i][int(t)] - s.get_avg()[s_t])**2
  						#print(score)
  						s_t = s_t + 1
  				rmsd = (rmsd + (score/(s_t))**(1/2))#/(float(max(s.get_avg()) - float(min(s.get_avg()))))
  				#print('max: ' + str(min(s.get_avg())))
  			 	#sample_time = s.get_time()
  			 	
  			  
  			# for each variable (variables are in the order that is in the variables input file)
  				# if variable == symbol
  					# 
  	
  	
  	return rmsd
  
  
  
  def plot_fit(self, aModel):
	  
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
	    #numToPlot = len(self.samples)
	    #toPlot = self.samples
	    samples = self.data.get_samples()
	    numToPlot = len(samples)
	    print()
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
	    				fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(25,25))
	    				fig.suptitle('Data samples and simulation results, plot ' + str(numFigs) , fontsize=fs, fontweight='bold')
	    			curAx = axes[r][c]
	    			if (i < numToPlot):
	    				time = samples[i].get_time()
	    				avg = samples[i].get_avg()
	    				sd = samples[i].get_sd()
	    				curAx.errorbar(time, avg, fmt='o', markersize=4, color='black')#curAx.errorbar(time, avg, yerr=sd, fmt='o',color='black', ecolor='gray')
	    				curAx.set_xlabel('Time (' + samples[i].get_timeUnits() + ')')
	    				curAx.set_ylabel(samples[i].get_units())
	    				curAx.set_title('Sample: ' + samples[i].get_name())
	    				# plot the simulated results
	    				for j in range(0,len(aModel.get_eqs())): 
	    					if aModel.get_eqs()[j].get_symbol() == samples[i].get_symbol(): 
	    						break 
	    				if (j <= len(samples)):
	    					# find the equation that matches this variable
	    					#pass
    						curAx.plot(aModel.get_time(), aModel.get_results()[j], color='green', linewidth = 4)
	    			else:
	    				curAx.axis("Off")
	    			i = i + 1
	    			
	    	plt.subplots_adjust(top=0.88, bottom=0.08, left = 0.093, right = 0.933, wspace=0.35, hspace = 0.46)
	    	plt.show()
            
  
  
  	