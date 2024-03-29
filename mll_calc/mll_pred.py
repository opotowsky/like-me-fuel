#! /usr/bin/env python3

import sys
import pickle
import argparse
import numpy as np
import pandas as pd
import scipy.stats as stats

def like_calc(X, y_test, unc):
    """
    Given a simulated entry with uncertainty and a test entry, calculates the
    likelihood that they are the same. 
    
    Parameters
    ----------
    X : numpy array (train DB) of nuclide measurements for simulated entry
    y_test : numpy array (single row) of nuclide measurements for test
             ("measured") entry
    unc : float representing flat uncertainty percentage, or 0.0 indicated
          counting error

    Returns
    -------
    like: likelihood that the test entry is the simulated entry

    """
    # TODO UNTESTED CODE (but not recently in use)
    idx = np.nonzero(y_test)[0]
    y_test = y_test[idx]
    X = X[:, idx]
    # unc arg of 0 indicates for the script to use sqrt(counts) uncertainty
    if unc == 0.0:
        std = np.sqrt(X)    
    else:
        std = unc * X
    like = np.prod(stats.norm.pdf(X, loc=y_test, scale=std), axis=1)
    return like

def ll_calc(X, y_test, unc):
    """
    Given a simulated entry with uncertainty and a test entry, calculates the
    log-likelihood that they are the same. 

    Parameters
    ----------
    X : numpy array (train DB) of nuclide measurements for simulated entry
    y_test : numpy array (single row) of nuclide measurements for test
             ("measured") entry
    unc : float representing flat uncertainty percentage, or 0.0 indicated
          counting error

    Returns
    -------
    ll: numpy array of log-likelihoods that the test entry is the simulated 
        entry for each entry in the DB

    """
    idx = np.nonzero(y_test)[0]
    y_test = y_test[idx]
    X = X[:, idx]
    # unc arg of 0 indicates for the script to use sqrt(counts) uncertainty
    if unc == 0.0:
        std = np.sqrt(X) 
    else:
        std = unc * X
    ll = np.sum(stats.norm.logpdf(X, loc=y_test, scale=std), axis=1)
    return ll

def unc_calc(X, y_test, unc):
    """
    Given a simulated entry and a test entry with uniform uncertainty,
    calculates the uncertainty in the log-likelihood calculation. 

    Parameters
    ----------
    X : numpy array (train DB) of nuclide measurements for simulated entry
    y_test : numpy array (single row) of nuclide measurements for test
             ("measured") entry
    unc : float representing flat uncertainty percentage, or 0.0 indicated
          counting error

    Returns
    -------
    ll_unc: numpy array of log-likelihood uncertainties for each DB entry

    """
    idx = np.nonzero(y_test)[0]
    y_test = y_test[idx]
    X = X[:, idx]
    # unc arg of 0 indicates for the script to use sqrt(counts) uncertainty
    if unc == 0.0:
        sim_unc_sq = X
        tst_unc_sq = y_test
    else:
        sim_unc_sq = (unc * X)**2
        tst_unc_sq = (unc * y_test)**2
    unc_array = ((X - y_test) / sim_unc_sq)**2 * (sim_unc_sq + tst_unc_sq)
    np.nan_to_num(unc_array, copy=False, nan=0.0, posinf=0.0, neginf=0.0)
    unc_array = np.array(unc_array, dtype=np.float64)
    ll_unc = np.sqrt(np.sum(unc_array, axis=1))
    return ll_unc

def ratios(XY, ratio_list, labels):
    """
    Given a dataframe with entries (rows) that contain nuclide measurements and
    some labels, calculate the predetermined ratios of the measurements.

    Parameters
    ----------
    XY : dataframe of spent fuel entries containing nuclide measurements and 
         their labels
    ratio_list : list of nuclide ratios
    labels : list of label titles in the dataframe

    Returns
    -------
    XY_ratios : dataframe of spent fuel entries containing nuclide measurement 
                ratios and their labels

    """

    XY_ratios = XY.loc[:, labels].copy()
    for ratio in ratio_list: 
        nucs = ratio.split('/')
        XY_ratios[ratio] = XY[nucs[0]] / XY[nucs[1]]
    XY_ratios.replace([np.inf, -np.inf], 0, inplace=True)
    XY_ratios.fillna(0, inplace = True)
    # reorganize columns
    cols = ratio_list + labels
    XY_ratios = XY_ratios[cols]
    return XY_ratios

def format_pred(pred_row, lbls, nonlbls, cdf_cols):
    """
    This separates off the formatting of the pred_ll dataframe from the 
    get_pred function for cleanliness. 

    Parameters
    ----------
    pred_row : single-row dataframe including nuclide measurements, the 
               prediction (i.e., the predicted labels), and all saved log-
               likelihoods
    lbls : list of labels that are predicted
    nonlbls : list of reactor parameters that aren't being predicted
    cdf_cols : list of new LogLL columns added to prediction for CDF plot

    Returns
    -------
    pred_row : single-row dataframe including the prediction (i.e., predicted 
               labels), LLmax, LLUnc, and a list of LLs and their Uncs to 
               populate a CDF
    
    """
    lbls = lbls + nonlbls
    pred_lbls = ["pred_" + s for s in lbls] 
    pred_row.rename(columns=dict(zip(lbls, pred_lbls)), inplace=True)
    pred_lbls.extend(cdf_cols)
    pred_row = pred_row.loc[:, pred_lbls]

    return pred_row

def ll_cdf(pred_ll, ll_df):
    """
    Returns a single-row dataframe with the prediction/MaxLogLL with 8 new
    columns of log-likelihoods that can populate a CDF, which includes the 2nd
    largest LogLL, and 7 percentiles that should give a decent picture of the
    CDF curve. (and all corresponding uncertainties)

    Parameters
    ----------
    pred_ll : single-row dataframe including nuclide measurements, the 
              prediction (i.e., the predicted labels), and maxLL/LLUnc
    ll_df : two-column dataframe including log-likelihood calculations and 
            their uncertainties for a given test sample calculation against 
            entire training db

    Returns
    -------
    pred_ll : single-row dataframe including nuclide measurements, the 
              prediction (i.e., the predicted labels), and all saved log-
              likelihoods (Max and CDF-relevant)
    cdf_cols : list of column names that are the new LogLL columns added for 
               CDF

    """
    old_cols = pred_ll.columns.values.tolist()

    # First, grab adjacent LL value to MaxLL
    cols = ll_df.columns.values.tolist()
    maxs = ll_df.nlargest(2, cols[0])
    pred_ll['2ndMaxLogLL'] = maxs[cols[0]].iloc[1]
    pred_ll['2ndMaxLLUnc'] = maxs[cols[1]].iloc[1]
    
    # Second, add columns with percentiles in the col name 
    quants = [0.9998, 0.9988, 0.95, 0.9, 0.5, 0.1, 0.01]
    for quant in quants:
        quant_df = ll_df.quantile(quant)
        pred_ll['CDF_LogLL_' + str(quant)] = quant_df.loc[cols[0]]
        pred_ll['CDF_LLUnc_' + str(quant)] = quant_df.loc[cols[1]]
    
    new_cols = pred_ll.columns.values.tolist()
    cdf_cols = [col for col in new_cols if col not in old_cols]

    return pred_ll, cdf_cols

def get_pred(XY, test_sample, unc, lbls, nonlbls):
    """
    Given a database of spent fuel entries and a test sample (nuclide
    measurements only), calculates the log-likelihood (and LL-uncertainty) of
    that sample against every database entry.  Determines the max LL, and
    therefore the corresponding prediction in the database.  Also determines a
    list of LL measurements that populate a CDF. Returns that prediction and LL
    information as a single row dataframe.

    Parameters
    ----------
    XY : dataframe with nuclide measurements and reactor parameters
    test_sample : numpy array of a sample to be predicted (nuclide measurements 
                  only)
    unc : float that represents the simulation uncertainty in nuclide 
          measurements
    lbls : list of reactor parameters to be predicted
    nonlbls : list of reactor parameters that aren't being predicted

    Returns
    -------
    pred_ll : single-row dataframe including the prediction (i.e., predicted 
              labels), its max log-likelihood/uncertainty, and a list of 
              log-likelihoods and their uncertainties to populate a CDF

    """
    ll_name = 'MaxLogLL'
    unc_name = 'MaxLLUnc'
    X = XY.drop(lbls+nonlbls, axis=1).copy().to_numpy()
    XY[ll_name] = ll_calc(X, test_sample, unc)
    XY[unc_name] = unc_calc(X, test_sample, unc)

    pred_row = XY.loc[XY.index == XY[ll_name].idxmax()].copy()
    pred_ll, cdf_cols = ll_cdf(pred_row, XY[[ll_name, unc_name]]) 
    cdf_cols = [ll_name, unc_name] + cdf_cols
    pred_ll = format_pred(pred_ll, lbls, nonlbls, cdf_cols)
    
    # need to delete calculated columns so next test sample can be calculated
    XY.drop(columns=[ll_name, unc_name], inplace=True)
    
    return pred_ll

def mll_testset(XY, test, ext_test, unc, lbls, nonlbls):
    """
    Given a database of spent fuel entries containing a nuclide vector and the
    reactor operation parameters, and an equally formatted database of test
    cases to predict, this function loops through the test database to perform
    a series of predictions.  It first formats the test sample for prediction,
    then gathers all the predictions from the test database entries

    Parameters
    ----------
    XY : dataframe with nuclide measurements and reactor parameters
    test : dataframe with test cases to predict in same format as train
    ext_test : boolean indicating which of external test set or LOOV is being 
               performed
    unc : float that represents the simulation uncertainty in nuclide 
          measurements
    lbls : list of reactor parameters to be predicted
    nonlbls : list of reactor parameters that aren't being predicted

    Returns
    -------
    pred_df : dataframe with ground truth and predictions
    
    """
    pred_df = pd.DataFrame()
    for sim_idx, row in test.iterrows():
        if ext_test:
            test_sample = row.drop(lbls)
            test_answer = row[lbls]
            pred_ll = get_pred(XY, test_sample.to_numpy(), unc, lbls, nonlbls)
            all_lbls = lbls
        else:
            test_sample = row.drop(lbls+nonlbls)
            test_answer = row[lbls+nonlbls]
            pred_ll = get_pred(XY.drop(sim_idx), test_sample.to_numpy(), unc, lbls, nonlbls)
            all_lbls = lbls + nonlbls
        if pred_df.empty:
            pred_df = pd.DataFrame(columns = pred_ll.columns.to_list())
        pred_df = pred_df.append(pred_ll)
    pred_df = pd.concat([test.loc[:, all_lbls].rename_axis('sim_idx').reset_index(),
                         pred_df.rename_axis('pred_idx').reset_index()
                         ], axis=1)
    return pred_df

def check_traindb_equal(final, db_path, arg_ratios, ratio_list, lbls):
    """
    Checks at end of script that the database was not altered
    
    Parameters
    ----------
    final : training database dataframe at end of script
    db_path : path to pkl file containing training database
    arg_ratios : Boolean arg indicating whether or not nuclide ratios are being used
    ratio_list : list of ratios being created
    lbls : all non-features (prediction labels and non-prediction labels)
    
    """
    initial = pd.read_pickle(db_path)
    if arg_ratios == True:
        initial = ratios(initial, ratio_list, lbls)
    if not initial.equals(final):
        sys.exit('Final training database does not equal initial database')
    return

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
    
    parser.add_argument('outdir', metavar='output-directory',  
                        help='directory in which to organize output csv')
    parser.add_argument('sim_unc', metavar='sim-uncertainty', type=float,
                        help='value of simulation uncertainty (in fraction) to apply to likelihood calculations')
    parser.add_argument('train_db', metavar='reactor-db', 
                        help='file path to a training set, e.g. /mnt/researchdrive/BOX_INTERNAL/opotowsky/*.pkl')
    parser.add_argument('test_db', metavar='testing-set', 
                        help='file path to an external testing set, e.g. ~/sfcompo/format_clean/sfcompo_nucXX.pkl')
    parser.add_argument('outfile', metavar='csv-output',  
                        help='name for csv output file')
    parser.add_argument('db_rows', metavar='db-interval', nargs=2, type=int, 
                        help='indices of the database interval for the job')
    parser.add_argument('--ext-test', dest='ext_test', action='store_true',
                        help='execute script with external testing set by providing file path to a testing set')
    parser.add_argument('--no-ext-test', dest='ext_test', action='store_false',
                        help='do not execute script with external testing set')
    parser.add_argument('--ratios', dest='ratios', action='store_true',
                        help='compute isotopic ratios instead of using concentrations')
    parser.add_argument('--no-ratios', dest='ratios', action='store_false', 
                        help='compute using concentrations instead of isotopic ratios')
    
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
    XY = pd.read_pickle(args.train_db)
    if 'total' in XY.columns:
        XY.drop('total', axis=1, inplace=True)
    
    lbls = ['ReactorType', 'CoolingTime', 'Enrichment', 'Burnup', 
            'OrigenReactor']
    nonlbls = ['AvgPowerDensity', 'ModDensity', 'UiWeight']
    
    # testing set
    if args.ext_test == True:
        test = pd.read_pickle(args.test_db)
        # In-script test: order of columns must match:
        xy_cols = XY.columns.tolist()
        for col in nonlbls: xy_cols.remove(col)
        if xy_cols != test.columns.tolist():
            if sorted(xy_cols) == sorted(test.columns.tolist()):
                test = test[xy_cols]
            else:
                sys.exit('Feature sets are different')
        # slice test set
        test = test.iloc[args.db_rows[0]:args.db_rows[1]]
        # converting train DB to match units in sfcompo DB
        XY = convert_g_to_mgUi(XY, lbls+nonlbls)
    else: 
        test = XY.iloc[args.db_rows[0]:args.db_rows[1]]
        # this is a fix for the now too-large db to test every entry
        # 3 lines per job, with max_jobs currently set to 9900
        # (~6% of db is tested)
        #test = test.sample(3)
        
    # TODO: need some better way to handle varying ratio lists
    tamu_list = ['cs137/cs133', 'cs134/cs137', 'cs135/cs137', 'ba136/ba138', 
                 'sm150/sm149', 'sm152/sm149', 'eu154/eu153', 'pu240/pu239', 
                 'pu241/pu239', 'pu242/pu239'
                 ]
    ratio_list = tamu_list
    if args.ratios == True:
        XY = ratios(XY, ratio_list, lbls+nonlbls)
        test = ratios(test, ratio_list, lbls)
    
    unc = float(args.sim_unc)
    pred_df = mll_testset(XY, test, args.ext_test, unc, lbls, nonlbls)
    
    fname = args.outfile + '.csv'
    pred_df.to_csv(fname)

    return

if __name__ == "__main__":
    main()
