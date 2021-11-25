# author: Luke Collins
# date: 2021-11-25

"""
This script runs preprocessed data through Wilcoxon rank-sum tests
for significance of difference of median substance_use_total
between 'pre' and 'post' datasets.

Usage: stat_tests.py --data_path = <dir> --output = <file>
Options:
--data_path=<dir>  path to dir in which preprocessed data is stored
--output=<file>  file to write csv output [default: './stat_tests_output.csv']
"""

from docopt import docopt
import pandas as pd
from scipy.stats import ranksums
import glob

opt = docopt(__doc__)

def main(data_path, output_file):
    """
    Performs Wilcoxon rank-sum tests on pre/post data files
    -----
    data_path: str
        path to dir in which preprocessed data csvs are stored
    output_file: str
        path to dir in which csv output of stat tests will be written.
        default val is './stat_tests_output.csv'
    Returns
    -----
    None
    """
    # read the datasets
    preprocessed_data = [datafile.split('\\')[-1] for datafile in glob.glob(data_path + '\*.csv')] # '..\..\data\*.csv'
    pre_datasets = [x for x in preprocessed_data if 'pre' in x]
    post_datasets = [x for x in preprocessed_data if 'post' in x]

    results = {}
    for i in range(len(pre_datasets)):
        # analysis\preprocessing\*.csv
        pre = pd.read_csv('../../data/%s' % pre_datasets[i])['substance_use_total']
        post = pd.read_csv('../../data/%s' % post_datasets[i])['substance_use_total']
        test_statistic, p_val = ranksums(pre, post, alternative='two-sided')
        results[pre_datasets[i].split('_')[0]] = {'test_statistic': test_statistic,
                                                  'p_value': p_val}

    pd.DataFrame(results).T.to_csv(output_file)


if __name__ == "__main__":
    data_path = opt["<dir>"]
    output_file = opt["<file>"]
    main(data_path, output_file)