# this file was written by the
# write_calc_comps method of class Model
# to encode the components for model: SIRD Model  
# file written on: 17-Dec-2020 (10:47:24.536672)

import numpy as np

def calc_comps(y):

	# parameters
	beta = 0.09090909090909091 # Average rate of infection
	gamma = 0.06896551724137931 # Average rate of recovery
	mu = 0.0008 # Average rate of death
	N = 368010.0 # Total number of people in the population

	# set up model variables:
	S = y[:,0]
	I = y[:,1]
	R = y[:,2]
	D = y[:,3]

	# components
	comps = list()
	c1 = beta*S*I/N # rate at which people are becoming infected
	comps.append(c1)
	c2 = gamma*I # rate at which people are recovering
	comps.append(c2)
	c3 = mu*I # rate at which people are dying
	comps.append(c3)

	print (comps)
	print(len(comps[0]))
	
	print (y)

	return comps
