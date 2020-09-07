#! /usr/bin/env python3

uncs = [0.05, 0.1, 0.15, 0.2]
job_dirs = ['Job' + str(i) + '_unc' + str(unc) for i, unc in enumerate(uncs)]

kid_jobs = {'job_dirs' : job_dirs,
            'uncs' : uncs,
            'rows_per_job' : 1
            }

train_15 = {'parent_dir' : 'train15',
            'ext_test' : '--no-ext-test',
            'ratios' : '--no-ratios', 
            'train_pkl' : 'sim_grams_nuc15.pkl',
            'test_pkl' : 'sfcompo_nuc15.pkl'
            }

train_29 = {'parent_dir' : 'train29',
            'ext_test' : '--no-ext-test',
            'ratios' : '--no-ratios',
            'train_pkl' : 'sim_grams_nuc29',
            'test_pkl' : 'sfcompo_nuc29.pkl'
            }

#tamu_ratio = {'parent_dir' : 'tamuRatio',
#              'ext_test' : '--no-ext-test',
#              'ratios' : '--ratios'
#              }

sfco_15 = {'parent_dir' : 'sfco15',
           'ext_test' : '--ext-test',
           'ratios' : '--no-ratios',
           'train_pkl' : 'sim_grams_nuc15.pkl',
           'test_pkl' : 'sfcompo_nuc15.pkl'
           }

sfco_29 = {'parent_dir' : 'sfco29',
           'ext_test' : '--ext-test',
           'ratios' : '--no-ratios',
           'train_pkl' : 'sim_grams_nuc29.pkl',
           'test_pkl' : 'sfcompo_nuc29.pkl'
           }

#parent_jobs = [train_15, train_29, sfco_15, sfco_29]
parent_jobs = [train_15, train_29]
