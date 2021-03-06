########################################################################
#	Conner I Sandefur 												   #
#	Created: 12/15/2020												   #
#	Updated: 12/29/2020												   #			
# 	Description: This file contains the Equation class      		   #
#		and a function to generate a list of class Equation objects    #
#		from an input file											   #
########################################################################


class Equation(object):
	"""Class containing information about a differential equation
		or a term in a differential equation (for simplication)
		a symbol 
		right hand side of the equation
		left hand side of the equation
		when Equation is a term, symbol is same has left hand side
	"""
	
	
	def __init__(self, l, r):
		self.lhs = l
		self.rhs = r
		if (l[0] == 'd'): # this is a differential equation
			# pull out variable symbol from lhs 
			self.sym = self.lhs.split('d')[1]
			self.diffEq = True
		else: # this is a term
			self.sym = self.lhs
			self.diffEq = False


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


	def isDiffEq(self):
		"""Function to return value of diffEq"""
		return self.diffEq


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

	f = open(file, 'r')
	f.readline() # skip the header lines
	f.readline()
	f.readline()
	for l in f:
		#print(l)
		eqs.append(Equation(l.split('=')[0].strip(), 
			(l.split('=')[1].strip()).strip('\n')))
						
	f.close()
	return eqs


