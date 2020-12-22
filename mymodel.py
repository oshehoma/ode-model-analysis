# this file was written by the
# write_models method of class Model
# to encode the model: SIRD Model  
# file written on: 22-Dec-2020 (10:12:13.829576)

import numpy as np

def model():

	# parameters
	beta = 0.09090909090909091 # Average rate of infection
	gamma = 0.06896551724137931 # Average rate of recovery
	mu = 0.0008 # Average rate of death
	N = 368010.0 # Total number of people in the population

	def step(y,t):
		# set up model variables:
		(S, I, R, D) = y

		# set up model equations:
		dSdt = -beta*S*I/N
		dIdt = beta*S*I/N - gamma*I - mu*I
		dRdt = gamma*I
		dDdt = mu*I

		model = np.array([dSdt, dIdt, dRdt, dDdt], dtype=float)

		return model

	return step
