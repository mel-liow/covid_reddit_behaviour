# author: Maeve Shi
#date: 2021-11-24

"""
This script performs exploratory data visualization on a given dataset

Usage: eda/visualization.py --data_path=<data_path> --outputfile=<outputfile>
Options:
--data_path=<data_path>           Specify the path of the input data.
--outputfile=<outputfile>         Specify the place to save the images.
"""

# import relevant modules
import altair as alt
from docopt import docopt
import pandas as pd
import numpy as np
from altair_saver import save
import os

alt.data_transformers.enable('data_server')
alt.renderers.enable('mimetype')

opt = docopt(__doc__)


def main(data_path, outputfile):
    """
    calls visualization function to create charts and bars from the dataset
    and save them as png files at a specified location.
    -----
    data_path: str
        path of the input dataset
    outputfile: str
        path to save the output images
    Returns
    -----
    None
    """
    # read the dataset
    data = pd.read_csv(data_path)
    #creat path of the output img if the path doesn't exist
    if not os.path.exists(os.path.dirname(outputfile)):
        os.makedirs(os.path.dirname(outputfile))
    #get the distribution of the target feature
    histograms(data, outputfile)


def histograms(data, outputfile):
    """
    create histograms of given features to obtain the distribution,
    and then save the figure as png file to outputfile location.
    -----
    data: pandas dataframe
    outputfile: str
      path to save the output images.
    Returns:
    -----
    None
    """
    #create histogram of given column/feature
    hist = (
        alt.Chart(data).mark_bar(opacity=0.8).encode(
        x=alt.X('substance_use_total', bin=alt.Bin(maxbins=30)),
        y='count()')
    )

    #save the file
    save(hist, outputfile + "/histogram.png")


if __name__ == "__main__":
    main(opt["--data_path"], opt["--outputfile"])

