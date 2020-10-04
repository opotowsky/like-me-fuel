#! /usr/bin/env python3

import sys
import pickle
import argparse
import numpy as np
import pandas as pd
import scipy.stats as stats

def like_calc(y_sim, y_mes, std):
    """
    Given a simulated entry with uncertainty and a test entry, calculates the
    likelihood that they are the same. 
    
    Parameters
    ----------
    y_sim : series of nuclide measurements for simulated entry
    y_mes : series of nuclide measurements for test ("measured") entry
    std : standard deviation for each entry in y_sim

    Returns
    -------
    like: likelihood that the test entry is the simulated entry

    """
    y_sim = y_sim[y_mes>0]
    std = std[y_mes>0]
    y_mes = y_mes[y_mes>0]
    like = np.prod(stats.norm.pdf(y_sim, loc=y_mes, scale=std))
    return like

def get_ll(XY, test_sample, unc, lbls, nonlbls):
    """
    Given a database of spent fuel entries and a test sample (nuclide
    measurements only), calculates the likelihood of that sample against every
    database entry. Returns LL information as a dataframe.

    Parameters
    ----------
    XY : dataframe with nuclide measurements and reactor parameters
    test_sample : series of a sample to be predicted (nuclide measurements 
                  only)
    unc : float that represents the simulation uncertainty in nuclide 
          measurements
    lbls : list of reactor parameters to be predicted
    nonlbls : list of reactor parameters that aren't being predicted

    Returns
    -------
    XY : training set dataframe with likelihood column added

    """
    ll_name = 'LL'
    X = XY.drop(lbls+nonlbls, axis=1).copy()
    XY[ll_name] = X.apply(lambda row: like_calc(row, test_sample, unc*row), axis=1)
    return XY

def ll_testset(XY, test, unc, lbls, nonlbls):
    """
    Given a database of spent fuel entries containing a nuclide vector and the
    reactor operation parameters, and an equally formatted database of test
    cases to predict, this function loops through the test database to perform
    a likelihood calcuation for entries in the training database

    Parameters
    ----------
    XY : dataframe with nuclide measurements and reactor parameters
    test : dataframe with test cases to predict in same format as train
    unc : float that represents the simulation uncertainty in nuclide 
          measurements
    lbls : list of reactor parameters to be predicted
    nonlbls : list of reactor parameters that aren't being predicted

    Returns
    -------
    ll_df : dataframe that includes all training set information and
            a column of the likelihood calculation for each entry
    
    """
    for sim_idx, row in test.iterrows():
        test_sample = row.drop(lbls)
        test_answer = row[lbls]
        ll_df = get_ll(XY, test_sample, unc, lbls, nonlbls)
    return ll_df

def convert_g_to_mgUi(XY, Y_list):
    """
    Converts nuclides from ORIGEN simulations measured in grams to 
    concentrations measured in mg / gUi

    Parameters
    ----------
    XY : dataframe of origen sims with nuclides measured in grams
    Y_list : list of columns in DB that are not features (nuclides) 

    Returns
    -------
    XY : dataframe of origen sims with nuclides measured in mg / gUi
    
    """
    
    nucs = XY.columns[~XY.columns.isin(Y_list)].tolist()
    # [x (g) / 1e6 (gUi)] * [1000 (mg) / 1 (g)] = x / 1000
    XY[nucs] = XY[nucs].div(1000, axis=0)
    return XY

def format_XY(db_path):
    """
    Fetches training database given a filepath

    Parameters
    ----------
    db_path : path to pkl file containing training database

    Returns
    -------
    XY : cleaned and formatted training database
    
    """
    XY = pd.read_pickle(db_path)
    if 'total' in XY.columns:
        XY.drop('total', axis=1, inplace=True)
    XY = XY.loc[XY['Burnup'] > 0]
    XY.reset_index(inplace=True, drop=True)
    return XY

def parse_args(args):
    """
    Command-line argument parsing

    Parameters
    ----------
    args : 

    Returns
    -------
    XY : cleaned and formatted training database

    """
    parser = argparse.ArgumentParser(description='Performs maximum likelihood calculations for reactor parameter prediction.')
    
    # local filepaths, FYI:
    # train_db = '~/sims_n_results/simupdates_aug2020/not-scaled_nucXX.pkl'
    # test_db = '~/sfcompo/format_clean/sfcompo_nucXX.pkl'
    
    parser.add_argument('outdir', metavar='output-directory',  
                        help='directory in which to organize output csv')
    parser.add_argument('sim_unc', metavar='sim-uncertainty', type=float,
                        help='value of simulation uncertainty (in fraction) to apply to likelihood calculations')
    parser.add_argument('train_db', metavar='reactor-db', 
                        help='file path to a training set')
    parser.add_argument('test_db', metavar='testing-set', 
                        help='file path to an external testing set')
    parser.add_argument('outfile', metavar='csv-output',  
                        help='name for csv output file')
    parser.add_argument('db_rows', metavar='db-interval', nargs=2, type=int, 
                        help='indices of the database interval for the job')
    
    return parser.parse_args(args)

def main():
    """
    Given a database of spent fuel entries (containing nuclide measurements and
    labels of reactor operation parameters of interest for prediction) and a
    testing database containing spent fuel entries formatted in the same way,
    this script calculates the maximum log-likelihood of each test sample
    against the database for a prediction. The errors of those predictions are
    then calculated and saved as a CSV file.
    
    """
    
    args = parse_args(sys.argv[1:])

    # training set
    XY = format_XY(args.train_db)
    XY = XY.iloc[args.db_rows[0]:args.db_rows[1]]
    
    lbls = ['ReactorType', 'CoolingTime', 'Enrichment', 'Burnup', 
            'OrigenReactor']
    nonlbls = ['AvgPowerDensity', 'ModDensity', 'UiWeight']
    
    test = pd.read_pickle(args.test_db)
    # In-script test: order of columns must match:
    xy_cols = XY.columns.tolist()
    #for col in nonlbls: xy_cols.remove(col)
    #if xy_cols != test.columns.tolist():
    #    if sorted(xy_cols) == sorted(test.columns.tolist()):
    #        test = test[xy_cols]
    #    else:
    #        sys.exit('Feature sets are different')
    # converting train DB to match units in sfcompo DB
    #XY = convert_g_to_mgUi(XY, lbls+nonlbls)
        
    unc = float(args.sim_unc)
    ll_df = ll_testset(XY, test, unc, lbls, nonlbls)

    fname = args.outfile + '.csv'
    ll_df.to_csv(fname)

    return

if __name__ == "__main__":
    main()
