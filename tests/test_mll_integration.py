#! /usr/bin/env python3

import csv
import pytest
import subprocess
import numpy as np
import pandas as pd
from pathlib import Path

@pytest.mark.parametrize('exp, bool_argv',
                         [(4, ['--no-ext-test', '--no-ratios']), # currently, only 3 samples per submission are tested
                          (3, ['--ext-test', '--no-ratios']),
                          # can't test ratios with 29-nuc set since ratios weren't defined for this set
                          #(11, ['--no-ext-test', '--ratios']),
                          #(3, ['--ext-test', '--ratios'])
                          ]
                         )
def test_integration(tmpdir, exp, bool_argv):
    const_argv = ['JobDir', '0.05', './tests/sample10sim.pkl', './tests/sfcompo2.pkl']
    outfile = tmpdir.join('output')
    cmd_list = ['./mll_calc/mll_pred.py'] + const_argv + [outfile, '0', '10'] + bool_argv
    subprocess.run(cmd_list)
    # Just testing # of lines in final output for now
    with open(outfile + '.csv', 'r') as f: 
        reader = csv.reader(f)
        obs_lines = len(list(reader))
    assert obs_lines == exp
