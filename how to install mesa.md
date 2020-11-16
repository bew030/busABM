# SPECIAL THANKS TO MY MENTOR GROUP FOR FIGURING OUT HOW TO INSTALL MESA
ORIGINAL GITHUB REFERENCE CAN BE FOUND HERE: https://github.com/covABM/QuickstartABM

# QuickstartABM
How to get started with MESA Agent Based Modeling

## Installation
### Install GeoPandas
Here I strongly recommand building a fresh new environment for this project with Anaconda, download Anaconda with link:
https://www.anaconda.com/products/individual <br>
To create a fresh python 3.7 environment, open Anaconda Prompt and do:
```shell
conda create -n myenv python=3.7
```
Replace `myenv` with the environment name.

To activate the new environment, do:
```shell
conda activate myenv
```

#### If you are using a Mac/Linux Machine:
install GeoPandas with:
```shell
pip install geopandas
```
#### If you are using a Windows Machine: 
To avoid several version conflicts GeoPandas raises, I recommand downloading the dependent libraries' wheel files with the following link:
https://drive.google.com/drive/folders/1NHOd7DQsXjBxoUZg0mrziF2HKiPoRDIn?usp=sharing

Unzip and locate your download directory with Anaconda Prompt and <b> FIRST </b> install GDAL with:
```shell
pip install GDAL-3.1.2-cp37-cp37m-win_amd64.whl
```
Then <b> SECOND </b> install Fiona with:
```shell
pip install Fiona-1.8.13-cp37-cp37m-win_amd64.whl
```
Install the remaining packages with no specified order:
```shell
pip install pyproj-2.6.1.post1-cp37-cp37m-win_amd64.whl
pip install Rtree-0.9.4-cp37-cp37m-win_amd64.whl
pip install Shapely-1.7.0-cp37-cp37m-win_amd64.whl
```
Now you can install GeoPandas with:
```shell
pip install geopandas
```
### Install Matplotlib
We are currently using Matplotlib to visualize our model <br>
Install matplotlib with:
```shell
pip install matplotlib
```
### Install MESA
Install ABM package MESA with:
```shell
pip install mesa
```
### Install MESA-geo
#### If you are using a Mac Machine: <br>
Install rtree <b> FIRST </b> with `conda` (there seems to exist a distribution issue with `pip` specificly to Mac):
```shell
conda install rtree
```
Install geospatial-enabled MESA extension mesa-geo with: <br>
```shell
pip install mesa-geo
```

### Install Jupyter
Since we create a new Anaconda environment, Jupyter is not default installed:
```shell
pip install jupyter
```

## Getting started
The interactive example is in the notebook `QuickstartABM.ipynb` <br>
I recommand checking out MESA's documentation and examples, which is very well documented: <br>
https://mesa.readthedocs.io/en/master/tutorials/intro_tutorial.html <br>
MESA-geo also have some examples that could be useful, but I'd rather recommand talk to me first since it's not as clear as MESA's: <br>
https://github.com/Corvince/mesa-geo


