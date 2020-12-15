

# code to test Model class development

import model as m


### FOR TESTING
pfile = 'test_pars.txt' # file with parameter details
vfile = 'test_vars.txt' # file with variable details
test = m.Model('SIRD', pfile, vfile)
print(test)
test.plot()
test.par_print_to_file(pfile)
test.var_print_to_file(vfile)