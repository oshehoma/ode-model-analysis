########################################################################
#	Conner I Sandefur 												   #
#	Created: 12/09/2020												   #
#	Updated: 12/14/2020												   #			
# 	Description: Class Model contains all information about a 		   #
#			single simulation of an ordinary differential equation 	   #
#			model, including model equations, parameters, and 		   #
# 			initial conditions used in the simulation				   #	
########################################################################

# import statements
import numpy as np    				# library of array tools
#import math							# library of math tools
import matplotlib.pyplot as plt 	# import the plotting tools
from scipy.integrate import odeint	# ODE integrator
import parameters as p 				# import the Parameter tools
import variables as v 				# import the Variable tools

class Model:
	"""Class containing all information about a model simulation:
		Parameters (descriptions, units, and values),
		Variables (description, units, and initial conditions),
		model equations, and simulation results. 

	"""

	### BEGIN FOR TESTING PURPOSES - HARD CODED MODEL INFORMATION
	#N = 368010			# census 2019 sum across 13 counties
	#I0 = 100		# number of active cases from first day of data set
	#R0 = 150	# number of recovered individuals from first day of data set
	#D0 = 10		# number of deceased individuals from 
						#first day of data set
	#S0 = N-I0-R0-D0		# number of susceptible based on 
						#case data and 2019 census
	#ic = [S0, I0, R0, D0]

	


	#beta = 1/11.0		# average rate of infection (1/days)
	#gamma = 1/14.5		# average rate of recovery (days)
	#mu = 1/1250			# average rate of death
	#pars = np.array([N, beta, gamma, mu])


	### END FOR TESTING PURPOSESS
	

	def __init__(self, name, pfile, vfile):
		"""Initialize this Model instance by:
			setting up array of Parameters,
			setting up array of Variables, and
			simulating the model
			model parameters are in pfile
			variables, including time, vfile file

		"""
	
		self.name = name

		# load list of class Parameter
		self.pars = p.load_pars(pfile)

		# load list of class Variable
		self.vars = v.load_vars(vfile)

		###############################################
		### BEGIN SITUATION SPECIFIC REGION OF CODE ###
		###    UPDATE FOR YOUR MODEL ICS and TIME 	###
		###############################################
		# find variables in array of Varameters using symbol
		# SIRD MODEL
		for var in self.vars: # for each Parameter class instance
			if (var.get_symbol() == 'I'):
				I0 = var.get_value()
			elif (var.get_symbol() == 'R'):
				R0 = var.get_value()
			elif (var.get_symbol() == 'D'):
				D0 = var.get_value()
			elif (var.get_symbol() == 'S'):
				S0 = var.get_value()
			elif(var.get_symbol() == 't'):
				t = var.get_value()
		self.ic = [S0, I0, R0, D0]
		
		step = 1/24 # step size 
		self.time = np.arange(0, t, step) 	# time 
	
		###############################################
		###  END SITUATION SPECIFIC REGION OF CODE  ###
		###############################################

		# run the model
		print('Running the simulation.')
		self.sim = odeint(self.model(), self.ic, self.time)

		# calculate model components
		print('Calculating model components.')
		[self.comps, self.compNames, self.compUnits] = self.calculate()
		

	def __str__(self):
		"""Print general model information:
			Name of this model
			Model equations
			Table of variables
			Table of parameters
		"""
		dets =('Model Name: ' ,
			self.name, '\n'
			'Number Model Variables: ' , 
			str(len(self.vars)),  '\n'
			'Number Model Parameters: ' ,
			str(len(self.pars)) )

		return ''.join(dets)


	#  TO DO:
	#	print simulation and component results to file
	#	update plot method to generate more than one figure for
	#		variable and/or component numbers greater than 6
	#
	#

	def par_print_to_file(self, fname):
		"""Function to print parameters to file in the same format
			as parameters are input into Model:

			p_symbol, p_units, p_value, p_description where
			p_symbol is the symbol used for the parameter by the model,
			p_units are the units for the parameter,
			p_value is the value of the parameter,
			p_description is the description of the parameter, 
			and the first line is the header line
		"""

		f = open(fname, 'w')	# open file f to overwrite content
		f.write('Parameter symbol, Units, Value, Description\n')
		for p in self.pars:
			f.write(p.get_info())
			f.write('\n')
		f.close()			



	def var_print_to_file(self, fname):
		"""Function to print variables to file in the same format
			as variables are input into Model:

			v_symbol, v_units, v_value, v_description where
			v_symbol is the symbol used for the variable by the model,
			v_units are the units for the variable,
			v_value is the value of the variable,
			v_description is the description of the variable, 
			and the first line is the header line
		"""

		f = open(fname, 'w')	# open file f to overwrite content
		f.write('Variable symbol, Units, Value, Description\n')
		for v in self.vars:
			f.write(v.get_info())
			f.write('\n')
		f.close()			



	def sim_print_to_file(self, fname):
		"""Function to print simulation results and model components
			to comma-separated file:
			time, variable1, variable2, ..., variableM, component1, 
				component2, ..., componentN where
			time is the time step,
			variable1 is value of the first variable in the system at 
				this time step,
			...,
			variableN is value of the Nth variable in the system at 
				this time step,
			component1 is the value of the first component in the 
				system (e.g. -beta*S*I),
			...,
			componentN is the value of the Nth component in the 
				system.
		"""

		f = open(fname, 'w') # open file f to overwrite content
		# header line depends on variables and model components


		
		# time is in self.time, which is a numpy array
		# variable is in self.sim, which is a numpy array
		# components are in self.comps, which is a numpy array





		# 
		f.close()
					
	




	def plot(self):
		""" Plot each simulated model in its own subplot"""
	
		# adjust plotting parameters
		fs = 15 #font size
		lw = 4	# line width
		parameters = {'axes.labelsize': fs, 
			'axes.labelweight': 'bold',
			'axes.linewidth' : lw,
			'axes.titlesize': fs,
			'axes.titleweight': 'bold',
			'xtick.labelsize': 13,
			'axes.spines.top': False,
			'axes.spines.right': False,
			'ytick.labelsize': fs,
			'font.weight': 'bold'
 			}
		plt.rcParams.update(parameters)

		

		# we only want up to six plots per figure 
		# plot a maximum of three subplots per row:
		numVars = len(self.sim[0,:])
		print(numVars)
		#ax_list = np.empty(numVars, dtype=object)
		if (numVars % 6 == 0): 
			numFigs = int(numVars / 3)
		else:
			numFigs = int(numVars / 3) + 1
		#print (str(numRows))


		fig = plt.figure(figsize=(15,15))
		fig.suptitle('Model Variables', fontsize=fs, 
				fontweight='bold', x = 0.85, color = 'navy')


		# plot a maximum of three subplots per row:
		#numVars = len(self.vars[:,0])
		#print(numComps)
		ax_list = np.empty(numVars, dtype=object)
		if (numVars % 3 == 0): 
			numRows = int(numVars / 3)
		else:
			numRows = int(numVars / 3) + 1
		#print (str(numRows))






		# plot first subplot: 
		
		for p in range(0, len(self.sim[0,:])):
			ax_list[p] = fig.add_subplot(numRows,3,p+1, 
				title = str(self.vars[p].get_desc()) + ' (' +
						str(self.vars[p].get_symbol()) + ')',
				xlabel = 'Time (' + self.vars[len(self.sim[0,:])].get_units() + ')',
				ylabel = str(self.vars[p].get_units()),
			)
			ax_list[p].plot(self.time, self.sim[:,p], 
						color='black', label=str(p))

		
		plt.subplots_adjust(top=0.91, bottom=0.06, 
			left = 0.1, right = 0.97, 
			wspace=0.3, hspace = 0.3)



		plt.show()


		fig.savefig('sim_plots.png')


		fig = plt.figure(figsize=(15,15))
		fig.suptitle('Model Components', fontsize=fs, 
				fontweight='bold', x = 0.85, color = 'navy')

		# plot a maximum of three subplots per row:
		numComps = len(self.comps[:,0])
		#print(numComps)
		ax_list = np.empty(numComps, dtype=object)
		if (numVars % 3 == 0): 
			numRows = int(numComps / 3)
		else:
			numRows = int(numComps / 3) + 1
		#print (str(numRows))

		# plot first subplot: 
		for p in range(0, len(self.comps[:,0])):
			ax_list[p] = fig.add_subplot(numRows,3,p+1, 
				title = self.compNames[p], 
				xlabel = 'Time (' + self.vars[len(self.sim[0,:])].get_units() + ')',
				ylabel = self.compUnits[p]
			)
			ax_list[p].plot(self.time, self.comps[p,:], 
						color='black', label=str(p))

		
		plt.subplots_adjust(top=0.91, bottom=0.06, 
			left = 0.1, right = 0.97, 
			wspace=0.3, hspace = 0.3)

		plt.show()


		fig.savefig('comp_plots.png')







	def model(self):
		"""Model function used by the ODE integrator
			Note: this function changes as parameters and 
			model equations change
		"""
		
		###############################################
		### BEGIN SITUATION SPECIFIC REGION OF CODE ###
		###    UPDATE FOR YOUR MODEL PARAMETERS 	###
		###############################################
		# find parameters in array of Parameters using symbol
		for par in self.pars: # for each Parameter class instance
			if (par.get_symbol() == 'N'):
				N = par.get_value()
			elif (par.get_symbol() == 'beta'):
				beta = par.get_value()
			elif (par.get_symbol() == 'gamma'):
				gamma = par.get_value()
			elif (par.get_symbol() == 'mu'):
				mu = par.get_value()
		###############################################
		###  END SITUATION SPECIFIC REGION OF CODE  ###
		###############################################
			
		
		def step(y, t):
			"""Function to integrate the model. 
				The model equations go here
			"""

			###############################################
			### BEGIN SITUATION SPECIFIC REGION OF CODE ###
			###    UPDATE WITH YOUR MODEL EQUATIONS 	###
			###############################################
			# set up model variables:
			(S, I, R, D) = y

			# set up model equations:
			dSdt = -beta*S*I/N  		
			dIdt = beta*S*I/N - gamma*I - mu*I 
			dRdt = gamma*I
			dDdt = mu*I

			eqs = np.array([dSdt, dIdt, dRdt, dDdt], dtype=float)
			###############################################
			###  END SITUATION SPECIFIC REGION OF CODE  ###
			###############################################
		

			return eqs

		return step



	def calculate(self):
		"""Calculate components of the model. These components can
			be, for example, parts of a model equation or a ratio
			of two model variables. 
		"""

		###############################################
		### BEGIN SITUATION SPECIFIC REGION OF CODE ###
		###    UPDATE FOR YOUR MODEL PARAMETERS, 	###
		###		YOUR MODEL VARIABLES, 				###
		###    AND WITH YOUR MODEL COMPONENTS 		###
		###############################################
		# find parameters in array of Parameters using symbol
		for par in self.pars: # for each Parameter class instance
			if (par.get_symbol() == 'N'):
				N = par.get_value()
			elif (par.get_symbol() == 'beta'):
				beta = par.get_value()
			elif (par.get_symbol() == 'gamma'):
				gamma = par.get_value()
			elif (par.get_symbol() == 'mu'):
				mu = par.get_value()

		# set up model variables:
		S = self.sim[:,0]
		I = self.sim[:,1]
		R = self.sim[:,2]
		D = self.sim[:,3]

		comp1 = beta*S*I/N  		
		comp2 = gamma*I
		comp3 = mu*I

		components = np.array([comp1, comp2, comp3], dtype=float)
		componentNames = ['infection rate', 
					'recovery rate', 'death rate']
		componentUnits = ['# individuals/time', 
					'# individuals/time', '# individuals/time']
		###############################################
		###  END SITUATION SPECIFIC REGION OF CODE  ###
		###############################################

		return [components, componentNames, componentUnits]




