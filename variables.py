########################################################################
#	Conner I Sandefur 												   #
#	Created: 12/09/2020												   #
#	Updated: 12/09/2020												   #			
# 	Description: This file contains the Variable class      		   #
#		and function to generate an array of class Variable format     #
#		an input file  												   #
########################################################################


class Variable:
	"""Class containing information about a variable:
		a symbol,
		description of variable,
		units, and
		value.
	"""
	sym = 'I'
	value = 100
	desc = 'Infected individuals'
	units = 'Number of individuals'

	def __init__(self, s, u, v, d):
		self.sym = s
		self.units = u
		self.value = v
		self.desc = d


	def __str__(self):
		#return ''.join( (self.sym, ' = ', '{:.15}'.format(self.value), 
		#	' (', self.units, ') ', 'which is the ', self.desc)  )
		return ''.join( (self.sym, ' = ', str(self.value), 
			' (', self.units, ') ', 'which is the ', self.desc)  )

	
	def get_value(self):
		"""Function to return value of this Varameter"""
		return self.value


	def get_symbol(self):
		"""Function to return symbol for this Varameter"""
		return self.sym


	def get_info(self):
		"""Function to return comma delimited Varameter attributes"""
		return ','.join( (self.sym, self.units, 
					str(self.value), self.desc) )
				

def load_vars(file):
	""" Function to load array of class Variables in comma-separated
		file of format:
		v_symbol, v_units, v_value, v_description where
		v_symbol is the symbol used for the variable by the model,
		v_units are the units for the parameter,
		v_value is the (initial) value of the variable,
		v_description is the description of the variable, 
		and the first line is the header line
	"""

	vars = list()

	N = 368010			# census 2019 sum across 13 counties
	I0 = 100		# number of active cases from first day of data set
	R0 = 150	# number of recovered individuals from first day of data set
	D0 = 10		# number of deceased individuals from 
						#first day of data set
	S0 = N-I0-R0-D0		# number of susceptible based on 
						#case data and 2019 census
	
	f = list()
	f.append(','.join(('I', 'Number of individuals', str(I0), 'Infected individuals')))
	f.append(','.join(('R', 'Number of individuals', str(R0), 'Recovered individuals')))
	f.append(','.join(('D', 'Number of individuals', str(D0), 'Deceased individuals')))
	f.append(','.join(('S', 'Number of individuals', str(S0), 'Suscetible individuals')))
	f.append(','.join(('t', 'days', str(100), 'Time')))
	#f = open(file, 'r')
	#f.readline() # skip the header line
	for l in f:
		vars.append(Variable(l.split(',')[0], l.split(',')[1], 	
						float(l.split(',')[2]), l.split(',')[3].strip('\n')))
	#f.close()
	return vars


