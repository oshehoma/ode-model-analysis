# ode-model-analysis

The purpose of this project is to generate object oriented Python code for analysis of models of biological systems implemented as ordinary differential equations. This code is designed to be reusable with 'any' (most?/some?) ordinary differential equation system. 

Code requires three input files (variables, parameters, and model equations) and uses these files to generate mymodel.py. This is the model system file used by the ode integrator to simulate the model. 

Run testing.py to run the demonstration model. 

Here is how the code breaks down:

class ModelEnsemble --> to be written: this class will hold experimental data, multiple instances of class Model (which are are the same model sysem but with a unique set of parameters and/or variables), methods to fit sims to data, and methods and functions to plot and print this information to files. 

class Model --> captures a single instance of a model: equations, a unique set of parameters and initial conditions, descriptions and units of paameters and variables, simulation results, including tracking of specific components (e.g. a single term of an equation) in the model and has methods and functions to plot and print this information to files. 
  States (ie variables):
    name: name of model (as a string)
    pars: list of class Parameter objects 
    vars: list of class Variable objects
    ic: list of initial conditions
    time: numpy array of time steps
    sim: simulation results after integrating the model 
    NOT YET: comps, compNames, compUnits: model components (parts of equations), and associated names and units
  
  Behaviors (ie methods):
    par_print_to_file: print parameters to file 
    var_print_to_file: print variables to file. 
    sim_print_to_file: in progress -> goal of this is to print simulation and component results to file
    plot_sims: plot simulation results (change in each variable over time); four variables per figure
    write_model: write model file for ode solver to use. currently, model file is written to mymodel.py. this filename cannot change or code will not run (as class Model imports mymodel)
    run_model: simulate the model and save in self.sim (see States)
    NOT YET: plot_comps
    

  These classes are used by class Model:
  class Parameter - symbol, unit, value, and description
  class Variable - symbol, unit, initial condition, and description 
  class Equation - left and right hand side of a differential equation and the symbol of the variable it is modeling
  MAYBE: class Component contain values that can change over time based on a particular combination of parameters and variables  
  
  
