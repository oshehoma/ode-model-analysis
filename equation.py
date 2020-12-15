########################################################################
#	Conner I Sandefur 												   #
#	Created: 12/15/2020												   #
#	Updated: 12/15/2020												   #			
# 	Description: This file contains the Equation class      		   #

	### AND FUNCTIONS/METHODS and maybe a Component class?
########################################################################


class Equation(object):
	"""Class containing information about a differential equation:
		a symbol
		description of variable,
		units, and
		value.
	"""
	
	#l = dIdt
	#r = beta*S*I/N - gamma*I - mu*I   # might make this a list?
										#  of class Components?
	#s = I
	
	def __init__(self, l, r):
		self.lhs = l
		self.rhs = r
		# pull out variable symbol from lhs 
		self.sym = self.lhs.split('d')[1]



	def __str__(self):
		return ''.join( (self.lhs, ' = ', self.rhs, ' which is the change over time for ', self.sym)  )

	
	def get_lhs(self):
		"""Function to return left hand side of this Equation"""
		return self.lhs


	def get_symbol(self):
		"""Function to return symbol of the variable 
			change over time captured by this Equation"""
		return self.sym

	
	def get_rhs(self):
		"""Function to return right hand side for this Equation"""
		return self.rhs


def load_eqs(file):
	""" Function to load array of class Equation in file of format:
			#model name
			#variables input file name 
			#parameters input file name
			equation1,
			.....
			equationX
			where equations have the form
			dVdt = combinations of variables & parameters
				   driving change in variable V over time (t)
	"""

	eqs = list()

	#f = list()
	#f.append('dSdt = -beta*S*I/N')
	#f.append('dIdt = beta*S*I/N - gamma*I - mu*I')
	#f.append('dRdt = gamma*I')
	#f.append('dDdt = mu*I')
	
	
	f = open(file, 'r')
	f.readline() # skip the header lines
	f.readline()
	f.readline()
	for l in f:
		eqs.append(Equation(l.split('=')[0].strip(), 
			(l.split('=')[1].strip()).strip('\n')))
						
	f.close()
	return eqs


