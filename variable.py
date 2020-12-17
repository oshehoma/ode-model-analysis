########################################################################
#	Conner I Sandefur 												   #
#	Created: 12/09/2020												   #
#	Updated: 12/16/2020												   #			
# 	Description: This file contains the Variable class      		   #
#		and function to generate an array of class Variable format     #
#		from an input file											   #
########################################################################


class Variable(object):
	"""Class containing information about a variable:
		a symbol,
		description of variable,
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
		"""Function to return value of this Variable"""
		return self.value


	def get_symbol(self):
		"""Function to return symbol for this Variable"""
		return self.sym

	
	def get_units(self):
		"""Function to return units for this Variable"""
		return self.units


	def get_desc(self):
		"""Function to return description for this Variable"""
		return self.desc


	def get_info(self):
		"""Function to return comma delimited Variable attributes"""
		return ','.join( (self.sym, self.units, 
					str(self.value), self.desc) )
				

def load_vars(file):
	""" Function to load array of class Variable in comma-separated
		file of format:
		v_symbol, v_units, v_value, v_description where
		v_symbol is the symbol used for the variable by the model,
		v_units are the units for the variable,
		v_value is the (initial) value of the variable,
		v_description is the description of the variable, 
		and the first line is the header line
	"""
	vars = list()
	f = open(file, 'r')
	f.readline() # skip the header line
	for l in f:
		vars.append(Variable(l.split(',')[0], l.split(',')[1], 	
						float(l.split(',')[2]), l.split(',')[3].strip('\n')))
	f.close()
	return vars


