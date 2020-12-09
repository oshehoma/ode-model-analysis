########################################################################
#	Conner I Sandefur 												   #
#	Created: 12/09/2020												   #
#	Updated: 12/09/2020												   #			
# 	Description: This file contains the Parameter class      		   #
#		and function to generate an array of class Parameter from      #
#		an input file 												   #
########################################################################


class Parameter:
	"""Class containing information about a parameter:
		a symbol,
		description of parameter,
		units, and
		value.
	"""
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
		"""Function to return value of this Parameter"""
		return self.value


	def get_symbol(self):
		"""Function to return symbol for this Parameter"""
		return self.sym


	def get_info(self):
		"""Function to return comma delimited Parameter attributes"""
		return ','.join( (self.sym, self.units, 
					str(self.value), self.desc) )
				

def load_pars(file):
	""" Function to load array of class Parameters in comma-separated
		file of format:
		p_symbol, p_units, p_value, p_description where
		p_symbol is the symbol used for the parameter by the model,
		p_units are the units for the parameter,
		p_value is the value of the parameter,
		p_description is the description of the parameter, 
		and the first line is the header line
	"""

	pars = list()
	f = open(file, 'r')
	f.readline() # skip the header line
	for l in f:
		pars.append(Parameter(l.split(',')[0], l.split(',')[1], 	
						float(l.split(',')[2]), l.split(',')[3].strip('\n')))
	f.close()
	return pars


