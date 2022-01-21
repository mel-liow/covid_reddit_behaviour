# Author: Mel Liow
# Created: 2021-12-07
# Last updated: 2021-12-07

FROM continuumio/miniconda3

# Update package list
RUN apt-get update -y

# Install development tools
RUN apt-get install gcc python3-dev chromium-driver -y

# Install GNU make
RUN apt-get install make -y

# Install Python packages

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
    "altair-data-server==0.4.*" \
    "jupyter-book==0.12.*"

