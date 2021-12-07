# Author: Mel Liow
# Created: 2021-12-07
# Last updated: 2021-12-07

# Copyright (c) Jupyter Development Team.
ARG BASE_CONTAINER=jupyter/minimal-notebook
FROM $BASE_CONTAINER

# Install Python 3 packages
RUN conda install --quiet -y -c conda-forge \
    "numpy=1.21.*" \
    "pandas=1.3.*" \
    "docopt=0.6.*" \
    "altair=4.1.*" \
    "altair_saver" \
    "matplotlib=3.5.*" \
    "scipy=1.7.*" \
    "ipykernel=6.5.*" \
    "requests=2.24.*"

RUN pip install \
    "jupyter-book==0.12.*" \
    "altair-data-server==0.4.*"
    
