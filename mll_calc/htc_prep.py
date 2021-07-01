#! /usr/bin/env python3

import sys
import csv
import argparse
import numpy as np
import pandas as pd
from mll_calc.all_jobs import parent_jobs, kid_jobs

def row_calcs(ext_test):
    if 'no' in ext_test:
        #db_rows = 450240
        #max_jobs = 9750
        db_rows = 90048 * 4
        max_jobs = 978 * 4
    else:
        db_rows = 505
        max_jobs = 10
    n_rows = db_rows // max_jobs
    init_rows = np.arange(0, db_rows, n_rows).tolist()
    end_rows = init_rows[1:]
    # TODO took out +1 below because had index 1 too high last time
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

def make_paramstxt(parent_job, kid_jobs):
    parent_dir = parent_job['parent_dir']
    fname = parent_dir + '_params.txt'
    init_rows, end_rows = row_calcs(parent_job['ext_test'])
    for unc_num, (kid_dir, unc) in enumerate(zip(kid_jobs['job_dirs'], kid_jobs['uncs'])):
        if parent_dir == 'train_nuc29': 
            fname = parent_dir + '_' + str(unc_num) + '_params.txt'
        #with open(fname, 'w') as f:
        with open(fname, 'a') as f:
            w = csv.writer(f)
            job_dir = parent_dir + '/' + kid_dir
            for i in range(0, len(init_rows)):
                job = [job_dir, unc, 
                       parent_job['train_pkl'], parent_job['test_pkl'],
                       str(i).zfill(4), init_rows[i], end_rows[i],
                       parent_job['ext_test'], parent_job['ratios']
                       ]
                w.writerow(job)    
    return

def main():
    """
    Reads all the job descriptions from all_jobs.py and populates the necessary
    params_mll_calc.txt files
    
    """
    for parent_job in parent_jobs:
        make_paramstxt(parent_job, kid_jobs)
    return
    
if __name__ == "__main__":
    main()
