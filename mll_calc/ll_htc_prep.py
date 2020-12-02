#! /usr/bin/env python3

import sys
import csv
import numpy as np
import pandas as pd
from mll_calc.all_jobs import parent_jobs, kid_jobs
from mll_calc.mll_pred import format_XY

def row_calcs():
    train_db = '~/sims_n_results/final_sims_nov2020/not-scaled_nuc29.pkl'
    train_set = format_XY(train_db)
    db_rows = len(train_set.index)
    max_jobs = 2400
    n_rows = db_rows // max_jobs
    init_rows = np.arange(0, db_rows, n_rows).tolist()
    end_rows = init_rows[1:]
    end_rows.append(db_rows+1)
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
    fname = parent_dir + '_full_ll_params.txt'
    with open(fname, 'w') as f:
        w = csv.writer(f) 
        for kid_dir, unc in zip(kid_jobs['job_dirs'], kid_jobs['uncs']):
            job_dir = parent_dir + '/' + kid_dir
            init_rows, end_rows = row_calcs()
            for i in range(0, len(init_rows)):
                job = [job_dir, unc, 
                       parent_job['train_pkl'], parent_job['test_pkl'],
                       str(i).zfill(4), init_rows[i], end_rows[i],
                       parent_job['ext_test']
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
