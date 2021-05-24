#! /usr/bin/env python3

import csv
import sys
import argparse
import numpy as np

def get_params_info(sub_type):
    # copied some stuff in from all_jobs related to partially failed submissions
    if sub_type == 'd3_n31':
        unc = 0.0
        job_dir = 'Job1_unc0.0'
        parent_job = {'parent_dir' : 'train_d3_czt_n31',
                      'ext_test' : '--no-ext-test',
                      'ratios' : '--no-ratios',
                      'train_pkl' : 'd3_czt_spectra_31peaks_trainset.pkl',
                      'test_pkl' : 'null'
                      }
    elif sub_type == 'act9':
        unc = 0.05
        job_dir = 'Job0_unc0.05'
        parent_job = {'parent_dir' : 'train_act9',
                      'ext_test' : '--no-ext-test',
                      'ratios' : '--no-ratios',
                      'train_pkl' : 'nuc9_activities_scaled_1g_reindex.pkl',
                      'test_pkl' : 'null'
                      }
    else:
        sys.exit()

    return unc, job_dir, parent_job

def row_calcs():
    db_rows = 440594
    max_jobs = 9750
    n_rows = db_rows // max_jobs
    init_rows = np.arange(0, db_rows, n_rows).tolist()
    end_rows = init_rows[1:]
    end_rows.append(db_rows)
    ################################################
    ################ In-script test ################
    ################################################
    if db_rows % n_rows == 0:
        total_jobs = db_rows // n_rows
    else:
        total_jobs = db_rows // n_rows + 1
    if len(init_rows) != total_jobs or len(end_rows) != total_jobs:
        print(total_jobs, len(init_rows), len(end_rows))
        sys.exit('total expected jobs does not equal one of db_row lists')
    ################################################
    return init_rows, end_rows

def main():
    """   
    for scenario with large # failed jobs, parse failed jobs and only save
    those in the params.txt file

    """
    parser = argparse.ArgumentParser(description='Parses failed jobs and saves those in a params.txt file')
    parser.add_argument('failed', metavar='failed-jobs-list',
                        help='list of failed jobs')
    parser.add_argument('sub_descrip', metavar='submission-description', choices=['act9', 'd3_n31'],
                        help='to which submission are you referring')
    args = parser.parse_args(sys.argv[1:])

    fail_file = args.failed
    with open(fail_file, 'r') as f:
        fail_idxs = f.readlines()
    fail_idxs = [i.rstrip() for i in fail_idxs]

    unc, unc_dir, parent_job = get_params_info(args.sub_descrip)
    parent_dir = parent_job['parent_dir']
    fname = parent_dir + '_params.txt'
    init_rows, end_rows = row_calcs()
    with open(fname, 'w') as f:
        w = csv.writer(f) 
        job_dir = parent_dir + '/' + unc_dir
        for i in range(0, len(init_rows)):
            if str(i).zfill(4) in fail_idxs:                
                job = [job_dir, unc, 
                       parent_job['train_pkl'], parent_job['test_pkl'],
                       str(i).zfill(4), init_rows[i], end_rows[i],
                       parent_job['ext_test'], parent_job['ratios']
                       ]
                w.writerow(job)    
    return
    
if __name__ == "__main__":
    main()
