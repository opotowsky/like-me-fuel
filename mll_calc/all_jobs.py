#! /usr/bin/env python3

uncs = [0.05,]# 0.1, 0.15, 0.2]
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

train_d2 = {'parent_dir' : 'train_d2_hpge',
            'ext_test' : '--no-ext-test',
            'ratios' : '--no-ratios',
            'train_pkl' : 'd2_hpge_spectra_peaks_trainset.pkl',
            'test_pkl' : 'null'
            }

train_d4 = {'parent_dir' : 'train_d4_nai',
            'ext_test' : '--no-ext-test',
            'ratios' : '--no-ratios',
            'train_pkl' : 'd4_nai_spectra_peaks_trainset.pkl',
            'test_pkl' : 'null'
            }

train_d5 = {'parent_dir' : 'train_d5_labr3',
            'ext_test' : '--no-ext-test',
            'ratios' : '--no-ratios',
            'train_pkl' : 'd5_labr3_spectra_peaks_trainset.pkl',
            'test_pkl' : 'null'
            }

train_d6 = {'parent_dir' : 'train_d6_sri2',
            'ext_test' : '--no-ext-test',
            'ratios' : '--no-ratios',
            'train_pkl' : 'd6_sri2_spectra_peaks_31trainset.pkl',
            'test_pkl' : 'null'
            }

d1_n31 = {'parent_dir' : 'train_d1_hpge_n31',
          'ext_test' : '--no-ext-test',
          'ratios' : '--no-ratios',
          'train_pkl' : 'd1_hpge_spectra_31peaks_trainset.pkl',
          'test_pkl' : 'null'
          }

d2_n31 = {'parent_dir' : 'train_d2_hpge_n31',
          'ext_test' : '--no-ext-test',
          'ratios' : '--no-ratios',
          'train_pkl' : 'd2_hpge_spectra_31peaks_trainset.pkl',
          'test_pkl' : 'null'
          }

train_d3 = {'parent_dir' : 'train_d3_czt',
            'ext_test' : '--no-ext-test',
            'ratios' : '--no-ratios',
            'train_pkl' : 'd3_czt_spectra_31peaks_trainset.pkl',
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

parent_jobs = [train_d6]
