

# code to test Model class development

import model as m

### FOR TESTING
pfile = 'test_pars.txt' # file with parameter details
vfile = 'test_vars.txt' # file with variable details
efile = 'test_eqs.txt'	# file with model equations
cfile = 'test_comps.txt' # file with model components
spfile = 'sim_plots'	# file name stem for simulation plots
cpfile = 'comp_plots'	# file name stem for component plots
outfile = 'sim_comp_results.csv'	# file to write simulations to
mfile = 'mymodel.py'  # file to write model to
ccfile = 'mycomps.py' # file to write components to

#test = m.Model(efile)
step = 1 # step size to use for solver
runToSS = False # set to True to run model for a long time to steady state
test = m.Model(efile, step, runToSS, cfile)
    

#test = m.Model(efile, cfile)

# creating model and comp files:
#test.write_model(mfile)
#test.write_calc_comps(ccfile)
runMe = 1

# run and plot model
if (runMe == 1):
    test.run_model()
    test.plot_sims(spfile)
    test.plot_comps(cpfile)
    test.sim_print_to_file(outfile)