

# code to run ASL model, plot simulations, and some components

import model as m

pfile = 'asl_pars.txt' # file with parameter details
vfile = 'asl_vars.txt' # file with variable details
efile = 'asl_eqs_simplified.txt'	# file with model equations
cfile = 'asl_comps.tab' # file with model components
mfile = 'mymodel.py'
ccfile = 'mycomps.py'
spfile = 'asl_sim_plots'	# file name stem for simulation plots
cpfile = 'asl_comp_plots'	# file name stem for component plots
outfile = 'asl_sim_comp_results.csv'	# file to write simulations to

step = 1 # same time step as time unit
test = m.Model(efile, 1)
#test = m.Model(efile, 1, cfile)
#test.write_model(mfile)
test.run_model()
#test.write_calc_comps(ccfile)
#test.calc_model_comps()
test.plot_sims(spfile)
#test.plot_comps(cpfile)
#test.sim_print_to_file(outfile)