#! /usr/bin/env python3

# detectors
#uncs = [0.0,]
#job_dirs = ['Job2_unc0.0',]

# activities
#uncs = [0.01,]
#job_dirs = ['Job2_unc0.01',]

# nuclide masses
uncs = [0.01, 0.05, 0.1, 0.15, 0.2]
job_dirs = ['Job' + str(i) + '_unc' + str(unc) for i, unc in enumerate(uncs)]

# sfcompo
#uncs = [0.01,]
#job_dirs = ['Job0_unc0.01',]


kid_jobs = {'job_dirs' : job_dirs,
            'uncs' : uncs,
            }

train_act7 = {'parent_dir' : 'train_act7',
              'ext_test' : '--no-ext-test',
              'ratios' : '--no-ratios',
              'train_pkl' : 'nuc7_activities_scaled_1g_reindex.pkl',
              'test_pkl' : 'null'
              }

train_act12 = {'parent_dir' : 'train_act12',
              'ext_test' : '--no-ext-test',
              'ratios' : '--no-ratios',
              'train_pkl' : 'nuc12_activities_scaled_1g_reindex.pkl',
              'test_pkl' : 'null'
              }

train_act32 = {'parent_dir' : 'train_act32',
               'ext_test' : '--no-ext-test',
               'ratios' : '--no-ratios',
               'train_pkl' : 'nuc32_activities_scaled_1g_reindex.pkl',
               'test_pkl' : 'null'
               }

d1_long = {'parent_dir' : 'train_d1_hpge_long',
           'ext_test' : '--no-ext-test',
           'ratios' : '--no-ratios',
           'train_pkl' : 'd1_hpge_spectra_long_peaks_trainset.pkl',
           'test_pkl' : 'null'
           }

d2_long = {'parent_dir' : 'train_d2_hpge_long',
           'ext_test' : '--no-ext-test',
           'ratios' : '--no-ratios',
           'train_pkl' : 'd2_hpge_spectra_long_peaks_trainset.pkl',
           'test_pkl' : 'null'
           }

d3_long = {'parent_dir' : 'train_d3_czt_long',
           'ext_test' : '--no-ext-test',
           'ratios' : '--no-ratios',
           'train_pkl' : 'd3_czt_spectra_long_peaks_trainset.pkl',
           'test_pkl' : 'null'
           }

d4_long = {'parent_dir' : 'train_d4_nai_long',
           'ext_test' : '--no-ext-test',
           'ratios' : '--no-ratios',
           'train_pkl' : 'd4_nai_spectra_long_peaks_trainset.pkl',
           'test_pkl' : 'null'
           }

d5_long = {'parent_dir' : 'train_d5_labr3_long',
           'ext_test' : '--no-ext-test',
           'ratios' : '--no-ratios',
           'train_pkl' : 'd5_labr3_spectra_long_peaks_trainset.pkl',
           'test_pkl' : 'null'
           }

d6_long = {'parent_dir' : 'train_d6_sri2_long',
           'ext_test' : '--no-ext-test',
           'ratios' : '--no-ratios',
           'train_pkl' : 'd6_sri2_spectra_long_peaks_trainset.pkl',
           'test_pkl' : 'null'
           }

d1_short = {'parent_dir' : 'train_d1_hpge_short',
            'ext_test' : '--no-ext-test',
            'ratios' : '--no-ratios',
            'train_pkl' : 'd1_hpge_spectra_short_peaks_trainset.pkl',
            'test_pkl' : 'null'
            }

d2_short = {'parent_dir' : 'train_d2_hpge_short',
            'ext_test' : '--no-ext-test',
            'ratios' : '--no-ratios',
            'train_pkl' : 'd2_hpge_spectra_short_peaks_trainset.pkl',
            'test_pkl' : 'null'
            }

d3_short = {'parent_dir' : 'train_d3_czt_short',
            'ext_test' : '--no-ext-test',
            'ratios' : '--no-ratios',
            'train_pkl' : 'd3_czt_spectra_short_peaks_trainset.pkl',
            'test_pkl' : 'null'
            }

d4_short = {'parent_dir' : 'train_d4_nai_short',
            'ext_test' : '--no-ext-test',
            'ratios' : '--no-ratios',
            'train_pkl' : 'd4_nai_spectra_short_peaks_trainset.pkl',
            'test_pkl' : 'null'
            }

d5_short = {'parent_dir' : 'train_d5_labr3_short',
            'ext_test' : '--no-ext-test',
            'ratios' : '--no-ratios',
            'train_pkl' : 'd5_labr3_spectra_short_peaks_trainset.pkl',
            'test_pkl' : 'null'
            }

d6_short = {'parent_dir' : 'train_d6_sri2_short',
            'ext_test' : '--no-ext-test',
            'ratios' : '--no-ratios',
            'train_pkl' : 'd6_sri2_spectra_short_peaks_trainset.pkl',
            'test_pkl' : 'null'
            }

d1_auto = {'parent_dir' : 'train_d1_hpge_auto',
           'ext_test' : '--no-ext-test',
           'ratios' : '--no-ratios',
           'train_pkl' : 'd1_hpge_spectra_auto_peaks_trainset.pkl',
           'test_pkl' : 'null'
           }

d2_auto = {'parent_dir' : 'train_d2_hpge_auto',
           'ext_test' : '--no-ext-test',
           'ratios' : '--no-ratios',
           'train_pkl' : 'd2_hpge_spectra_auto_peaks_trainset.pkl',
           'test_pkl' : 'null'
           }

d3_auto = {'parent_dir' : 'train_d3_czt_auto',
           'ext_test' : '--no-ext-test',
           'ratios' : '--no-ratios',
           'train_pkl' : 'd3_czt_spectra_auto_peaks_trainset.pkl',
           'test_pkl' : 'null'
           }

d4_auto = {'parent_dir' : 'train_d4_nai_auto',
           'ext_test' : '--no-ext-test',
           'ratios' : '--no-ratios',
           'train_pkl' : 'd4_nai_spectra_auto_peaks_trainset.pkl',
           'test_pkl' : 'null'
           }

d5_auto = {'parent_dir' : 'train_d5_labr3_auto',
           'ext_test' : '--no-ext-test',
           'ratios' : '--no-ratios',
           'train_pkl' : 'd5_labr3_spectra_auto_peaks_trainset.pkl',
           'test_pkl' : 'null'
           }

d6_auto = {'parent_dir' : 'train_d6_sri2_auto',
           'ext_test' : '--no-ext-test',
           'ratios' : '--no-ratios',
           'train_pkl' : 'd6_sri2_spectra_auto_peaks_trainset.pkl',
           'test_pkl' : 'null'
           }

train_nuc29 = {'parent_dir' : 'train_nuc29',
               'ext_test' : '--no-ext-test',
               'ratios' : '--no-ratios',
               'train_pkl' : 'sim_grams_nuc29.pkl',
               'test_pkl' : 'null'
               }

sfco_10ratio = {'parent_dir' : 'sfco10ratio',
                'ext_test' : '--ext-test',
                'ratios' : '--ratios',
                'train_pkl' : 'sim_grams_nuc15.pkl',
                'test_pkl' : 'sfcompo_nuc15.pkl'
                }

sfco_nuc29 = {'parent_dir' : 'sfco_nuc29',
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

#parent_jobs = [d1_auto, d2_auto, d3_auto, d4_auto, d5_auto, d6_auto,
#               d1_short, d2_short, d3_short, d4_short, d5_short, d6_short,
#               d1_long, d2_long, d3_long, d4_long, d5_long, d6_long]
#parent_jobs = [train_act7, train_act12, train_act32]
parent_jobs = [train_nuc29,]
#parent_jobs = [sfco_nuc29,]
