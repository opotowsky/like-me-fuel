#! /usr/bin/env python3

import sys
import csv
import argparse
import numpy as np
import pandas as pd
from mll_calc.all_jobs import parent_jobs, kid_jobs
from mll_calc.mll_pred import format_XY

def row_calcs(ext_test, test_db):
    test_set = format_XY(test_db)
    db_rows = len(test_set.index)
    if 'no' in ext_test:
        max_jobs = 8000 # only bc this allows same # of calcs as on other sets
        #max_jobs = 40
    else:
        # because sfco has 505 entries
        max_jobs = 1
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

def make_paramstxt(parent_job, kid_jobs, test_db):
    parent_dir = parent_job['parent_dir']
    fname = parent_dir + '_params.txt'
    init_rows, end_rows = row_calcs(parent_job['ext_test'], test_db)
    with open(fname, 'w') as f:
        w = csv.writer(f) 
        for kid_dir, unc in zip(kid_jobs['job_dirs'], kid_jobs['uncs']):
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
    parser = argparse.ArgumentParser(description='Performs maximum likelihood calculations for reactor parameter prediction.')
    
    # possible filepaths, FYI:
    # /mnt/researchdrive/BOX_INTERNAL/opotowsky/some/folder/*.pkl
    # '~/sims_n_results/simupdates_aug2020/not-scaled_nucXX.pkl'
    # '~/sims_n_results/final_sims_nov2020/not-scaled_nucXX.pkl'
    # '~/sfcompo/format_clean/sfcompo_nucXX.pkl'    
    parser.add_argument('testdb', metavar='test-database',  
                        help='full filepath to testing database (sfco or trainset)')
    args = parser.parse_args(sys.argv[1:])
    
    for parent_job in parent_jobs:
        make_paramstxt(parent_job, kid_jobs, args.testdb)
    return
    
if __name__ == "__main__":
    main()
