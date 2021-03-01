# this file was written by the
# write_calc_comps method of class Model
# to encode the components for model: SIRD Model  
# file written on: 01-Mar-2021 (13:33:52.154778)

import numpy as np
import math

def calc_comps(y, pars):

	# parameters
	beta = pars[0] #0.09090909090909091: Average rate of infection
	gamma = pars[1] #0.06896551724137931: Average rate of recovery
	mu = pars[2] #0.0008: Average rate of death
	N = pars[3] #368010.0: Total number of people in the population

	# set up model variables:
	S = y[0,:]
	I = y[1,:]
	R = y[2,:]
	D = y[3,:]

	# components
	comps = list()
	c1 = beta*S*I/N # rate at which people are becoming infected
	comps.append(c1)
	c2 = gamma*I # rate at which people are recovering
	comps.append(c2)
	c3 = mu*I # rate at which people are dying
	comps.append(c3)

	return comps
