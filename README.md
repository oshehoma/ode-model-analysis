# ode-model-analysis

The purpose of this project is to generate object oriented Python code for analysis of models of biological systems implemented as ordinary differential equations. This code is designed to be reusable with ordinary differential equation systems. 

The code requires three input files (variables, parameters, and model equations) and an optional fourth file for components. 

class Model uses the following classes: Parameter, Variable, Equation, and Component. These classes hold things like symbols, values, units, etc. for model parameters, variables, and ordinary differential equations. Components are terms of equations of interest to the modeler. 

Using the three input files, the code can write a Python model file for use by an ODE solver or a previously written model file can be used. Additionally, a Python file to calculate components can be written using class Model or a previously written file may be used. 

Run testing.py to run the demonstration model.

class Model --> captures a single instance of a model: equations, a unique set of parameters and initial conditions, descriptions and units of parameters and variables, simulation results, including tracking of specific components (e.g. a single term of an equation) in the model and has methods and functions to plot and print this information to files. 
  States (ie variables):
    name: name of model (as a string)
    pars: list of class Parameter objects 
    vars: list of class Variable objects
    eqs: list of class Equation objects
    comps: list of class Component objects (if component input file is provided)
    ic: list of initial conditions
    time: numpy array of time steps
    sim: simulation results after integrating the model 
      
  Behaviors (ie methods):
    par_print_to_file: print list of Parameters to file (in same format as input file)
    var_print_to_file: print list of Variables to file (in same format as input file)
    sim_print_to_file: print simulation results to file
    comp_print_to_file: print component results to file (if component input file is provided)
    plot_sims: plot simulation results (change in each variable over time); four variables per figure
    plot_comps: plot component results; four components per figure
    write_model: write model file for ode solver to use. currently, model file is written to mymodel.py. this filename cannot change or code will not run (as class Model imports mymodel)
    write_calc_component: write Python function to calculate components. currently, component calculation file is written to mycomps.py. this filename cannot change or code will not run (as class Model imports mycomps)
    run_model: simulate the model and save in self.sim (see States)
    
    
  These classes are used by class Model:
  class Parameter - symbol, unit, value, and description
  class Variable - symbol, unit, initial condition, and description 
  class Equation - left and right hand side of a differential equation and the symbol of the variable it is modeling
  class Component - a term from a differenttial equation, unit, and description
