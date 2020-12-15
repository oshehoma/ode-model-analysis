

# code to test Model class development

import model as m


### FOR TESTING
pfile = 'test_pars.txt' # file with parameter details
vfile = 'test_vars.txt' # file with variable details
efile = 'test_eqs.txt'	# file with model equations
spfile = 'sim_plots'	# file name stem for simulation plots
mfile = 'mymodel.py' # this file name is required because 
					 #  it is imported into class model
test = m.Model(efile)
test.write_model(mfile)
test.run_model()
#print(test)
test.plot_sims(spfile)
#test.par_print_to_file(pfile)
#test.var_print_to_file(vfile)