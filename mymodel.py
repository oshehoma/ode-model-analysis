# this file was written by the
# write_models method of class Model
# to encode the model: SIRD Model  
# file written on: 01-Mar-2021 (13:33:52.154347)

import numpy as np
import math

def model(t,y,pars):

	# parameters
	beta = pars[0] #0.09090909090909091: Average rate of infection
	gamma = pars[1] #0.06896551724137931: Average rate of recovery
	mu = pars[2] #0.0008: Average rate of death
	N = pars[3] #368010.0: Total number of people in the population

	# set up model variables:
	(S, I, R, D) = y

	# set up model equations:
	dSdt = -beta*S*I/N
	dIdt = beta*S*I/N - gamma*I - mu*I
	dRdt = gamma*I
	dDdt = mu*I

	model = np.array([dSdt, dIdt, dRdt, dDdt], dtype=float)

	return model
