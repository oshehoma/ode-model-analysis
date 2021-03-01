########################################################################
#	Conner I Sandefur 												   #
#	Created: 12/16/2020												   #
#	Updated: 12/22/2020												   #
# 	Description: This file contains the Component class      		   #
#		and a function to generate a list of class Component objects   #
#		from an input file											   #
########################################################################


class Component(object):
	"""Class containing information about a component:
		a symbol,
		equation for the component,
		units, and
		description.
	"""
	
	def __init__(self, s, u, e, d):
		self.sym = s
		self.eq = e
		self.units = u
		self.desc = d


	def __str__(self):
		#return ''.join( (self.sym, ' = ', '{:.15}'.format(self.value),
		#	' (', self.units, ') ', 'which is the ', self.desc)  )
		return ''.join( (self.sym, ' : ', str(self.eq),
			' (', self.units, ') ', 'which is the ', self.desc)  )

	
	def get_equation(self):
		"""Function to return equation for this Component"""
		return self.eq


	def get_symbol(self):
		"""Function to return symbol for this Component"""
		return self.sym

	
	def get_units(self):
		"""Function to return units for this Component"""
		return self.units


	def get_desc(self):
		"""Function to return description for this Component"""
		return self.desc


	def get_info(self):
		"""Function to return comma delimited Component attributes"""
		return ','.join( (self.sym, self.units,
					str(self.value), self.desc) )
				

def load_comps(file):
	""" Function to load array of class Component in comma-separated
		file of format:
		c_symbol, c_units, c_equation, c_description where
		c_symbol is the symbol used for the component by the model,
		c_units are the units for the component,
		c_equation is the (initial) value of the component,
		c_description is the description of the component,
		and the first line is the header line
	"""
	comps = list()
	f = open(file, 'r')
	f.readline() # skip the header line
	for l in f:
		comps.append(Component(l.split(',')[0].strip(), l.split(',')[1].strip(),
						l.split(',')[2].strip(), l.split(',')[3].strip().strip('\n')))
	f.close()
	return comps


