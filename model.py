########################################################################
#	Conner I Sandefur 												   #
#	Created: 12/09/2020												   #
#	Updated: 12/09/2020												   #			
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
	

	def __init__(self, pfile, vfile):
		"""Initialize this Model instance by:
			setting up array of Parameters,
			setting up array of Variables, and
			simulating the model
			model parameters are in pfile
			variables, including time, vfile file

		"""
	
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
		self.Ymodel = odeint(self.model(), self.ic, self.time)
		

	def __str__(self):
		"""Print general model information:
			Name of this model
			Model equations
			Table of variables
			Table of parameters
		"""
		dets =('Model Name: ' ,
			'undefined name' '\n'
			'Model Equations: '  '\n',
			'undefined equations'  '\n'
			'Model Variables: '  '\n',
			'undefined variables'  '\n'
			'Model Parameters: '  '\n',
			'undefined parameters')

		return ''.join(dets)


	#  TO DO:
	# 	update diagnostic plot to contain variable names and units
	#	update diagnostic plot to save figure!
	#	print simulation results to file
	#	update print (__str__) for Model class
	#
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

		fig = plt.figure(figsize=(15,15))
		fig.suptitle('Model Diagnostic Plot', fontsize=fs, 
				fontweight='bold', x = 0.85, color = 'navy')


		# plot a maximum of three subplots per row:
		numVars = len(self.Ymodel[0,:])
		print(numVars)
		ax_list = np.empty(numVars, dtype=object)
		if (numVars % 3 == 0): 
			numRows = int(numVars / 3)
		else:
			numRows = int(numVars / 3) + 1
		print (str(numRows))

		# plot first subplot: 
		
		for p in range(0, len(self.Ymodel[0,:])):
			ax_list[p] = fig.add_subplot(numRows,3,p+1, 
				title = 'Variable name will here',
				xlabel = 'Time unit will go here',
				ylabel = 'Variable unit will go here'
			)
			ax_list[p].plot(self.time, self.Ymodel[:,p], 
						color='black', label=str(p))

		plt.show()



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











