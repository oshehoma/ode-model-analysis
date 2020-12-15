# ode-model-analysis

The purpose of this project is to generate object oriented Python code for analysis of models of biological systems implemented as ordinary differential equations. This code is designed to be reusable with 'any' (most?/some?) ordinary differential equation system. 

Here is how the code breaksdown:


class ModelEnsemble --> to be written: this class will hold experimental data, multiple instances of class Model (which are are the same model sysem but with a unique set of parameters and/or variables), methods to fit sims to data, and methods and functions to plot and print this information to files. 

class Model --> captures a single instance of a model: equations, a unique set of parameters and initial conditions, descriptions and units of paameters and variables, simulation results, including tracking of specific components (e.g. a single term of an equation) in the model and has methods and functions to plot and print this information to files. 
  States (ie variables):
    name: name of model (as a string)
    pars: list of class Parameter objects 
    vars: list of class Variable objects
    ic: list of initial conditions, the code for defining these is currently unique to a specific model and hardcoded within class Model <-- so this is something that would be helpful to restructure 
    time: numpy array of time steps, where the step size is hardcoded in but the total simulation time is included in the variables input file
    sim: simulation results after integrating the model during setup
    comps, compNames, compUnits: model components (parts of equations), and associated names and units
  
  Behaviors (ie methods):
    par_print_to_file: print parameters to file (not sure why this would ever be used; I only used it to convert my hardcoded parameters into a file to use as input
    var_print_to_file: print variables to file. currently ,this generates an input file of variables and initial conditions to load into the list of class Variable and shouldn't be used again. it could be used to write simulation results perhaps. or maybe the simulation results should be stored in the Variable objects?
   sim_print_to_file: in progress -> goal of this is to print simulation and component results to file
   plot: plot simulation results (change in each variable over time) and component results (change in terms of equations over time)
   model: model system used by integrator
   calculate: calculate different terms/components in the system using the simulation results. this is completely dependent on what types of analysis are of interest and not even necessary for certain situations. could try making this an input file too
   








  Currently, class Model has multiple areas within the single file that require updating for a new model system. I'm brainstorming how to best restructure    the code so that it is more user-friendly.
  
  **********************************
  ** Begin restructuring thoughts **
  **********************************
  class Model requires two files, one containing parameter details and the other containing variable details, with values unique to this model instance. The parameter and variable lists are unique to each model system. I could state that these two files need to be ordered in such a way that class Model can assume the first variable in the file is the first variable in the set of model equations (and similarly for the parameters) but this feels like something I could easily screw up in ordering my variable and parameter files. So the only other option I see right now (which is what I have done) is to add identifying which parameter/variable goes where directly into sections of the code where it is necessary, which is multiple spots right now.....unless I can store this information someplace else in class Model as an attribute when loading the files maybe....
  
 One idea: I could have a third input file of model equations -- I really don't like the idea of a zillion input files but it's no different from hard coding each model system and also three isn't a zillion.    
 
 Would the computer write the .py files then? This still requires restructuring the code to compartmentalize things.   But this would allow for adding model components to the diagnostics more easily perhaps.....
 
 Try sketching out classes and connections again now that I have a better idea of what inputs and code change with each model system
  
  
  **********************************
  **  End restructuring thoughts  **
  **********************************
  
  
  
  
  Code that must change with each new model system:
  
  
  These classes are used by class Model:
  class Parameter

  class Variable

  
  class Component contain values that can change over time based on a particular combination of parameters and variables  
  
  
  class Equation contain components that are combined together to capture the change in a variable over time
