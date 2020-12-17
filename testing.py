

# code to test Model class development

import model as m


### FOR TESTING
pfile = 'test_pars.txt' # file with parameter details
vfile = 'test_vars.txt' # file with variable details
efile = 'test_eqs.txt'	# file with model equations
cfile = 'test_comps.txt' # file with model components
spfile = 'sim_plots'	# file name stem for simulation plots
cpfile = 'comp_plots'	# file name stem for component plots
mfile = 'mymodel.py' # this specific file name is required because 
					 #  it is imported into class model
ccfile = 'mycomps.py' # this specific file name is required because 
					 #  it is imported into class model
outfile = 'sim_comp_results.csv'	# file to write simulations to 

#test = m.Model(efile)
test = m.Model(efile, cfile)
test.write_model(mfile)
test.run_model()
#test.write_calc_comps(ccfile)
test.calc_model_comps()
#print(test)
test.plot_sims(spfile)
test.plot_comps(cpfile)
#test.par_print_to_file(pfile)
#test.var_print_to_file(vfile)
test.sim_print_to_file(outfile)

