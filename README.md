# ode-model-analysis

The purpose of this project is to generate object oriented Python code for analysis of models of biological systems implemented as ordinary differential equations. This code is designed to be reusable with 'any' (most?/some?) ordinary differential equation system. 

Here is how the code breaksdown:


class ModelEnsemble --> to be written: this class will hold experimental data, multiple instances of class Model (which are are the same model sysem but with a unique set of parameters and/or variables), methods to fit sims to data, and methods and functions to plot and print this information to files. 

class Model --> captures a single instance of a model: equations, a unique set of parameters and initial conditions, descriptions and units of paameters and variables, simulation results, including tracking of specific components (e.g. a single term of an equation) in the model and has methods and functions to plot and print this information to files. 
  Currently, class Model has multiple areas within the single file that require updating for a new model system. I'm brainstorming how to best restructure    the code so that it is more user-friendly. 
  class Model attributes:
  
    
  class Model functions:
  
  
  Code that must change with each new model system:
  
  
  These classes are used by class Model:
  class Parameter

  class Variable


