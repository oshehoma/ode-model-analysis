########################################################################
#	Conner I Sandefur 												   #
#	Created: 12/09/2020												   #
#	Updated: 12/17/2020												   #			
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
import parameter as p 				# import the Parameter tools
import variable as v 				# import the Variable tools
import equation as e 				# import the Equation tools
import component as c 				# import the Component tools
import mymodel as m 	     	    # import the mymodel file 
import mycomps as mc 				# import the mycomps file
from datetime import datetime




class Model(object):
	"""Class containing all information about a model simulation:
		Parameters (descriptions, units, and values),
		Variables (description, units, and initial conditions),
		model equations, and simulation results. 

	"""

	def __init__(self, efile, cfile = None):
		"""Initialize this Model instance by:
			opening efile, which is of the following format:
			#model name
			#variables input file name 
			#parameters input file name
			equation1,
			.....
			equationX
			and then, setting up the model equations, 
				array of Parameters, and array of Variables
			
		"""
	
		# setup model name
		f = open(efile, 'r')
		self.name = ((f.readline()).lstrip('#')).rstrip('\n')
		print ('Initializing: ' + self.name)

		# load list of model variables
		vfile = ((f.readline()).lstrip('#')).rstrip('\n')				
		print ('Loading variables from ' + vfile)
		self.vars = v.load_vars(vfile)
		print('There are '+str(len(self.vars)-1)+' dependent variables.')

		# load list of model parameters
		pfile = ((f.readline()).lstrip('#')).rstrip('\n')
		print ('Loading parameters from ' + pfile)
		self.pars = p.load_pars(pfile)
		print ('There are '+ str(len(self.pars)) +' parameters.')

		# load equations
		print ('Loading equations from ' + efile)
		self.eqs = e.load_eqs(efile)
		print ('There are ' + str(len(self.eqs)) + ' equations.')


		if cfile is not None:
			print('Loading components from ' + cfile)
			self.comps = c.load_comps(cfile)
			print ('There are ' + str(len(self.comps)) + ' components.')


		#for eq in self.eqs:
		#	print(eq)

		# check number variables agrees with number of equations
		if (len(self.eqs) != len(self.vars)-1):
			print('CAUTION: # of equations and variables off')


		print('Setting initial conditions using ' + vfile)
		# order equation array by the order in equation file
		# go through each model equation and assign initial condition
		j = 0 # index for equation array
		self.ic = list() 

		while (j < len(self.eqs)): # go through each equation
			found = 0
			i = 0
			while ( (found != 1) and (i < len(self.vars))):
				#print ('in while')
				if (self.eqs[j].get_symbol() == self.vars[i].get_symbol()):
					found = 1
					self.ic.append(self.vars[i].get_value())
				i = i + 1 # go to next variable
			j = j + 1 # go to the next equation
		
		# find and set up time
		i = 0
		while (i < len(self.vars)):
			if (self.vars[i].get_symbol() == 't'):
					t = self.vars[i].get_value()
			i = i + 1
		step = 1/1000 #1/24 # step size 
		self.time = np.arange(0, t, step) 	# time 
	



		# calculate model components
		#print('Calculating model components.')
		#[self.comps, self.compNames, self.compUnits] = self.calculate()
		

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


	def run_model(self):
		"""Method to run model
		"""

		# run the model
		print('Running the simulation.')
		self.sim = odeint(m.model(), self.ic, self.time)

	def calc_model_comps(self):
		"""Method to call function to calculate components
		"""

		# run the model
		if self.sim is not None:
			print('Calculating the model components using simulation.')
			self.comp_sim = mc.calc_comps(self.sim)

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
		#f.write('var 1,var 2,var 3,var 4\n')


		
		# time is in self.time, which is a numpy array
		# variable is in self.sim, which is a numpy array
		# components are in self.comps, which is a numpy array


		#self.sim.tofile(f, ',') NOT what i want

		#np.savetxt(fname, (self.time),fmt='%f') #, self.sim, self.comp_sim), delimiter=',') #, fmt='%d')


		# concatenate time and variables:
		toStack = list()
		headerInfo = list()
		toStack.append(self.time)
		headerInfo.append('Time')
		for i in range(0, len(self.sim[0,:])):
			toStack.append(self.sim[:,i])
			headerInfo.append(self.eqs[i].get_symbol())
		for i in range(0, len(self.comp_sim)):	
			toStack.append(self.comp_sim[i])
			headerInfo.append(self.comps[i].get_symbol())
		time_vars = np.stack(toStack)

		header = ','.join(headerInfo)

		#time_vars = np.stack( (self.time, self.sim[:,0]))
		#time_vars = np.stack( (time_vars, self.sim[:,1]))
		#time_vars = np.stack( (time_vars, self.sim[:,2]))
		#time_vars = np.stack( (time_vars, self.sim[:,3]))
			
		print(np.shape(self.time))
		print(np.shape(self.sim))
		print(np.shape(self.sim[:,0]))
		print(np.shape(time_vars))
		print(self.time)
		print(self.sim)
		print(time_vars)

		np.savetxt(fname, np.transpose(time_vars),delimiter=',',fmt='%f', header=header)

		# 
		f.close()
					
	




	def plot_sims(self, fname):
		""" Plot each simulated variable in its own subplot,
			with four subplots per figure and fname as the 
			figure stem
		"""

		print ('Plotting simulated variables.')
	
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

		

		# we only want up to 4 plots per figure 
		numVars = len(self.sim[0,:])

		#fig_list = np.empty(numVars, dtype=object)
		if (numVars % 4 == 0): 
			numFigs = int(numVars / 4)
		else:
			numFigs = int(numVars / 4) + 1
		#print (str(numRows))

		i = 0
		n = 1
		while (n <= numFigs):
			fig = plt.figure(figsize=(15,15))
			fig.suptitle('Model Variables Plot ' + str(n) 
				+ ' of ' + str(numFigs), fontsize=fs, 
				fontweight='bold', x = 0.85, color = 'navy')
			# plot four subplots per figure
			ax_list = np.empty(4, dtype=object)
			ax_index = 0
			# plot variables 0-3, 4-7, 8-11, etc.
			if (i+3 < len(self.sim[0,:])): # not at end of sims to plot
				endNum = i+3
			else:
				endNum = len(self.sim[0,:])
			for p in range(i, endNum+1):
				j = 0
				found = 0
				# match variable details to this simulated variable
				while (found == 0):
					if (self.vars[j].get_symbol() == self.eqs[p].get_symbol()):
						found = 1
						break
					j = j + 1
				ax_list[ax_index] = fig.add_subplot(2,2,ax_index+1, 
					title = str(self.vars[j].get_desc()) + ' (' +
							str(self.vars[j].get_symbol()) + ')',
					xlabel = 'Time (' + 
					self.vars[len(self.sim[0,:])].get_units() + ')',
					ylabel = str(self.vars[j].get_units())
				)
				ax_list[ax_index].plot(self.time, self.sim[:,p], 
						color='black', label=str(p))
				ax_index = ax_index+1

			plt.subplots_adjust(top=0.91, bottom=0.06, 
			left = 0.1, right = 0.97, 
			wspace=0.3, hspace = 0.3)

			#plt.show()

			fig.savefig(fname + '_' + str(n) 
						+ '_of_' + str(numFigs))

			i = i + 4 # jump to next four variables
			n = n + 1


	def plot_comps(self, fname):
		""" Plot each component in its own subplot"""
	
		print ('Plotting simulated components.')
	
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

		# we only want up to 4 plots per figure 
		numComps = len(self.comps)

		if (numComps % 4 == 0): 
			numFigs = int(numComps / 4)
		else:
			numFigs = int(numComps / 4) + 1
		
		i = 0 # component number
		n = 1 # figure number
		while (n <= numFigs):
			fig = plt.figure(figsize=(15,15))
			fig.suptitle('Model Component Plot ' + str(n) 
				+ ' of ' + str(numFigs), fontsize=fs, 
				fontweight='bold', x = 0.85, color = 'navy')
			# plot four subplots per figure
			ax_list = np.empty(4, dtype=object)
			ax_index = 0
			# plot components 0-3, 4-7, 8-11, etc.
			if (i+3 < len(self.comp_sim)): # not at end of components to plot
				endNum = i+3
			else:
				endNum = len(self.comp_sim)
			for p in range(i, endNum): # for each subplot  is this figure
				#j = 0
				#found = 0
				# match component symbol details to this simulated component
				#while (found == 0):
				#	if (self.comps[j].get_symbol() == self.eqs[p].get_symbol()):
				#		found = 1
				#		break
				#	j = j + 1
				print(str(p))
				ax_list[ax_index] = fig.add_subplot(2,2,ax_index+1, 
					title = str(self.comps[p].get_desc()) + ' (' +
							str(self.comps[p].get_symbol()) + ')',
					xlabel = 'Time (' + 
					self.vars[len(self.sim[0,:])].get_units() + ')',
					ylabel = str(self.comps[p].get_units())
				)
				ax_list[ax_index].plot(self.time, self.comp_sim[p], 
						color='black', label=str(p))
				ax_index = ax_index+1

			plt.subplots_adjust(top=0.91, bottom=0.06, 
			left = 0.1, right = 0.97, 
			wspace=0.3, hspace = 0.3)

			#plt.show()

			fig.savefig(fname + '_' + str(n) 
						+ '_of_' + str(numFigs))

			i = i + 4 # jump to next four variables
			n = n + 1










	def write_model(self,mfile):
		"""Method to write a model function to mfile that can be used
			by the ODE integrator. 
		"""	
		
		print("Writing model to: " + mfile)

		f = open(mfile, 'w') # overwrite current model file
		f.write('# this file was written by the\n')
		f.write('# write_models method of class Model\n')
		f.write('# to encode the model: ' + self.name + '\n')
		f.write('# file written on: ')
		f.write(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")+'\n')
		f.write('\n')
		f.write('import numpy as np\n')
		f.write('\n')
		f.write('def model():\n')
		f.write('\n')
		f.write('\t# parameters\n')
		for par in self.pars: # for each parameter
			f.write('\t' + par.get_symbol() + 
					' = ' + str(par.get_value()) + 
					' # ' + par.get_desc() + '\n')
		f.write('\n')
		f.write('\tdef step(y,t):\n')
		f.write('\t\t# set up model variables:\n')
		f.write('\t\t(')
		i = 0
		while (i < len(self.eqs)-1): #  
			f.write(self.eqs[i].get_symbol() + ', ')
			i = i + 1
		f.write(self.eqs[i].get_symbol() + ') = y\n')
		f.write('\n')
		f.write('\t\t# set up model equations:\n')
		for eq in self.eqs:
			f.write('\t\t' + eq.get_lhs() + ' = ' + 
					eq.get_rhs() + '\n')
		f.write('\n')
		f.write('\t\tmodel = np.array([')
		i = 0
		while (i < len(self.eqs)-1): #  
			f.write(self.eqs[i].get_lhs() + ', ')
			i = i + 1
		f.write(self.eqs[i].get_lhs() + '], dtype=float)\n')
		f.write('\n')
		f.write('\t\treturn model\n')
		f.write('\n')
		f.write('\treturn step\n')

		f.close()


	def write_calc_comps(self, ccfile):
		"""Method to write calc_comp.py to calculate components,
		 if there are any
		"""
		if self.comps is not None:
			print("Writing model components to: " + ccfile)

		f = open(ccfile, 'w') # overwrite current model file
		f.write('# this file was written by the\n')
		f.write('# write_calc_comps method of class Model\n')
		f.write('# to encode the components for model: ' 
				+ self.name + '\n')
		f.write('# file written on: ')
		f.write(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")+'\n')
		f.write('\n')
		f.write('import numpy as np\n')
		f.write('\n')
		f.write('def calc_comps(y):\n')
		f.write('\n')
		f.write('\t# parameters\n')
		for par in self.pars: # for each parameter
			f.write('\t' + par.get_symbol() + 
					' = ' + str(par.get_value()) + 
					' # ' + par.get_desc() + '\n')
		f.write('\n')
		f.write('\t# set up model variables:\n')
		#f.write('\t(')
		i = 0
		while (i < len(self.eqs)): #  
			f.write('\t'+self.eqs[i].get_symbol() + ' = ' +
				'y[:,' + str(i) + ']\n')
			i = i + 1
		f.write('\n')
		f.write('\t# components\n')
		f.write('\tcomps = list()\n')
		for comp in self.comps:
			# write component and symbol to file
			f.write('\t' + comp.get_symbol() + ' = ' +
					comp.get_equation() + 
					' # ' + comp.get_desc() + '\n')
			f.write('\tcomps.append(' + comp.get_symbol() +
					')\n')
		f.write('\n')
		f.write('\treturn comps\n')

		f.close()