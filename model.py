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
#import matplotlib.pyplot as plt 	# import the plotting tools
from scipy.integrate import solve_ivp	# ODE integrator


class Model:
	"""Class containing all information about a model simulation:
		Parameters (descriptions, units, and values),
		Variables (description, units, and initial conditions),
		model equations, and simulation results. 

	"""

	class Parameter:
		"""Class containing information about a parameter:
			description of parameter,
			units, and
			value.
		"""
		pass


	class Variable:
		"""Class containing informaiton about a variable:
			description of variable,
			units, and 
			value.
		"""
		pass

	def __init__(self):
		"""Initialize this Model instance by:
			setting up array of Parameters,
			setting up array of Variables, and
			simulating the model
		"""
		pass
	
	
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

	def model(self):
		"""Model function used by the ODE integrator"""
		
		def step(y, t):
			"""Function to integrate the model. 
				The model equations go here
			"""
			pass







