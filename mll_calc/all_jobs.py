#! /usr/bin/env python3

uncs = [0.05, 0.1, 0.15, 0.2]
job_dirs = ['Job' + str(i) + '_unc' + str(unc) for i, unc in enumerate(uncs)]

kid_jobs = {'job_dirs' : job_dirs,
            'uncs' : uncs,
            }

test_acts = {'parent_dir' : 'test_acts',
             'ext_test' : '--no-ext-test',
             'ratios' : '--no-ratios',
             'train_pkl' : 'test.pkl',
             'test_pkl' : 'null'
             }

train_d1 = {'parent_dir' : 'train_d1_hpge',
            'ext_test' : '--no-ext-test',
            'ratios' : '--no-ratios',
            'train_pkl' : 'd1_hpge_spectra_peaks_trainset.pkl',
            'test_pkl' : 'null'
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
            'train_pkl' : 'sim_grams_nuc29.pkl',
            'test_pkl' : 'sfcompo_nuc29.pkl'
            }

sfco_10ratio = {'parent_dir' : 'sfco10ratio',
                'ext_test' : '--ext-test',
                'ratios' : '--ratios',
                'train_pkl' : 'sim_grams_nuc15.pkl',
                'test_pkl' : 'sfcompo_nuc15.pkl'
                }

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

train_pca29 = {'parent_dir' : 'pca_train29',
               'ext_test' : '--no-ext-test',
               'ratios' : '--no-ratios',
               'train_pkl' : 'sim_grams_nuc29.pkl',
               'test_pkl' : 'sfcompo_nuc29.pkl'
               }

sfco_pca29 = {'parent_dir' : 'pca_sfco29',
              'ext_test' : '--ext-test',
              'ratios' : '--no-ratios',
              'train_pkl' : 'sim_grams_nuc29.pkl',
              'test_pkl' : 'sfcompo_nuc29.pkl'
              }

good_train = {'parent_dir' : 'train_good',
              'ext_test' : '--no-ext-test',
              'train_pkl' : 'sim_grams_nuc29.pkl',
              'test_pkl' : 'train_good.pkl'
              }

bad_train = {'parent_dir' : 'train_bad',
             'ext_test' : '--no-ext-test',
             'train_pkl' : 'sim_grams_nuc29.pkl',
             'test_pkl' : 'train_bad.pkl'
             }

good_sfco = {'parent_dir' : 'sfco_good',
             'ext_test' : '--ext-test',
             'train_pkl' : 'sim_grams_nuc29.pkl',
             'test_pkl' : 'sfco_good.pkl'
             }

bad_sfco = {'parent_dir' : 'sfco_bad',
            'ext_test' : '--ext-test',
            'train_pkl' : 'sim_grams_nuc29.pkl',
            'test_pkl' : 'sfco_bad.pkl'
            }

#parent_jobs = [train_15, train_29, sfco_15, sfco_29, sfco_10ratio]
#parent_jobs = [train_29, sfco_29]
#parent_jobs = [good_train, bad_train, good_sfco, bad_sfco]
parent_jobs = [train_d1,]
