#! /usr/bin/env python3

uncs = [0.0,]# 0.1, 0.15, 0.2]
job_dirs = ['Job1_unc0.0',]
#uncs = [0.05,]
#job_dirs = ['Job0_unc0.05',]
#job_dirs = ['Job' + str(i) + '_unc' + str(unc) for i, unc in enumerate(uncs)]


kid_jobs = {'job_dirs' : job_dirs,
            'uncs' : uncs,
            }

train_act4 = {'parent_dir' : 'train_act4',
              'ext_test' : '--no-ext-test',
              'ratios' : '--no-ratios',
              'train_pkl' : 'nuc4_activities_scaled_1g_reindex.pkl',
              'test_pkl' : 'null'
              }

train_act9 = {'parent_dir' : 'train_act9',
              'ext_test' : '--no-ext-test',
              'ratios' : '--no-ratios',
              'train_pkl' : 'nuc9_activities_scaled_1g_reindex.pkl',
              'test_pkl' : 'null'
              }

train_act32 = {'parent_dir' : 'train_act32',
               'ext_test' : '--no-ext-test',
               'ratios' : '--no-ratios',
               'train_pkl' : 'nuc32_activities_scaled_1g_reindex.pkl',
               'test_pkl' : 'null'
               }

d1_n113 = {'parent_dir' : 'train_d1_hpge_n113',
           'ext_test' : '--no-ext-test',
           'ratios' : '--no-ratios',
           'train_pkl' : 'd1_hpge_spectra_113peaks_trainset.pkl',
           'test_pkl' : 'null'
           }

d2_n113 = {'parent_dir' : 'train_d2_hpge_n113',
           'ext_test' : '--no-ext-test',
           'ratios' : '--no-ratios',
           'train_pkl' : 'd2_hpge_spectra_113peaks_trainset.pkl',
           'test_pkl' : 'null'
           }

d3_n113 = {'parent_dir' : 'train_d3_czt_n113',
           'ext_test' : '--no-ext-test',
           'ratios' : '--no-ratios',
           'train_pkl' : 'd3_czt_spectra_113peaks_trainset.pkl',
           'test_pkl' : 'null'
           }

d4_n113 = {'parent_dir' : 'train_d4_nai_n113',
           'ext_test' : '--no-ext-test',
           'ratios' : '--no-ratios',
           'train_pkl' : 'd4_nai_spectra_113peaks_trainset.pkl',
           'test_pkl' : 'null'
           }

d5_n113 = {'parent_dir' : 'train_d5_labr3_n113',
           'ext_test' : '--no-ext-test',
           'ratios' : '--no-ratios',
           'train_pkl' : 'd5_labr3_spectra_113peaks_trainset.pkl',
           'test_pkl' : 'null'
           }

d6_n113 = {'parent_dir' : 'train_d6_sri2_n113',
           'ext_test' : '--no-ext-test',
           'ratios' : '--no-ratios',
           'train_pkl' : 'd6_sri2_spectra_113peaks_trainset.pkl',
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

d3_n31 = {'parent_dir' : 'train_d3_czt_n31',
          'ext_test' : '--no-ext-test',
          'ratios' : '--no-ratios',
          'train_pkl' : 'd3_czt_spectra_31peaks_trainset.pkl',
          'test_pkl' : 'null'
          }

d4_n31 = {'parent_dir' : 'train_d4_nai_n31',
          'ext_test' : '--no-ext-test',
          'ratios' : '--no-ratios',
          'train_pkl' : 'd4_nai_spectra_31peaks_trainset.pkl',
          'test_pkl' : 'null'
          }

d5_n31 = {'parent_dir' : 'train_d5_labr3_n31',
          'ext_test' : '--no-ext-test',
          'ratios' : '--no-ratios',
          'train_pkl' : 'd5_labr3_spectra_31peaks_trainset.pkl',
          'test_pkl' : 'null'
          }

d6_n31 = {'parent_dir' : 'train_d6_sri2_n31',
          'ext_test' : '--no-ext-test',
          'ratios' : '--no-ratios',
          'train_pkl' : 'd6_sri2_spectra_31peaks_trainset.pkl',
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

parent_jobs = [d1_auto, d2_auto, d3_auto, d4_auto, d5_auto, d6_auto]
