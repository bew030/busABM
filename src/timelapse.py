import numpy as np
import random
from matplotlib import pyplot, colors
from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector
from numpy.random import choice

# mesa imports
from mesa_geo import GeoAgent, GeoSpace
from mesa.time import BaseScheduler
from mesa import datacollection
from mesa import Model

# shapely imports
from shapely.geometry import Polygon, Point, LineString
import shapely

# data analysis imports
import geopandas as gpd
import pandas as pd
import numpy as np

# plotting imports
import matplotlib as plt

from PIL import Image
import glob
import os

import re

def timelapse_step_model(input_source, output_source): 
    '''
    function that lets us timelpase the model. We are assuming that there is a simulation_images folder that allows
    you to save all the images. IT IS BEST TO ONLY RUN THIS FUNCTION ONCE AND THEN CLEAR THE FOLDER OF ALL THE IMAGES.
    The final model will be saved as 'gif_of_model.png'. An example gif can be found in the visualization folder.
    - model: the model that is being visualized
    - num-breathes: the numbers of steps that you want visualized. This method will display steps 0 all the way
    until num_breathes
    '''
    frames = []
    imgs = glob.glob(input_source+"*.png")
    filler_list = []
    for i in imgs: 
        filler_list.append(re.findall('\d+', i)[0])
    filler_list.sort(key = int)
    for i in range(len(filler_list)):
        filler_list[i] = input_source+filler_list[i]+'.png'

    for i in filler_list:
        new_frame = Image.open(i)
        frames.append(new_frame)

    os.makedirs(os.path.split(output_source)[0], exist_ok=True)

    # Save into a GIF file that loops forever
    frames[0].save(output_source + 'gif_of_model.gif', format='GIF',
                   append_images=frames[1:],
                   save_all=True,
                   duration=300, loop=0)