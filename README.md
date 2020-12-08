# ode-model-analysis

The purpose of this project is to generate object oriented Python code for analysis of models of biological systems implemented as ordinary differential equations. 

Currently, I am working on a Model class that encapsulates model equations, a unique set of parameter and variable initiaal conditino values, descriptions of those parameters and variables and corresponding units, and simulation results obtained after integrating the model using the parameter and variable initial condition values. 

My current thinking is that the simulation results of a given Model class can then be compared to experimental data that is stored in the parent class, which is still to be determined/written.
