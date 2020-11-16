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

class visualizer():
    def specific_step_model(model, breath_num): 
        '''
        this function takes in a model and returns the environment at a specific step. It takes in the following 
        parameters:
        - model: the model that is being visually represented
        - breath_num: the step that is being represented
        '''
        nmodel = model
        i = 0
        for x in range(breath_num):
            nmodel.step()
            i += 1
        agents = nmodel.schedule.agents
        infected = gpd.GeoSeries(map(lambda a: a.shape, [agent for agent in agents if agent.infected]))
        not_infected = gpd.GeoSeries(map(lambda a: a.shape, [agent for agent in agents if not agent.infected]))
        basemap = infected.plot(c="red", label = "infected")
        not_infected.plot(c="green", label = "uninfencted", ax = basemap)
        basemap.legend(bbox_to_anchor=(1.05, 1))
        basemap.title.set_text('Infections on the Bus: Step '+str(i))
        basemap.set_xlabel('Seat Column')
        basemap.set_ylabel('Seat Row')
        basemap.set_xticks(list(range(0,model.max_columns,model.seat_dist)))
        basemap.set_yticks(list(range(0,model.max_rows,model.seat_dist)))

    def visualize_step_model(model, num_breathes): 
        '''
        a method that helps us visualize multiple steps of the model.
        - model: the model that is being visualized
        - num-breathes: the numbers of steps that you want visualized. This method will display steps 0 all the way
        until num_breathes
        '''
        nmodel = model
        agents = nmodel.schedule.agents
        infected = gpd.GeoSeries(map(lambda a: a.shape, [agent for agent in agents if agent.infected]))
        not_infected = gpd.GeoSeries(map(lambda a: a.shape, [agent for agent in agents if not agent.infected]))
        basemap = infected.plot(c="red", label = "infected")
        not_infected.plot(c="green", label = "uninfencted", ax = basemap)
        basemap.legend(bbox_to_anchor=(1.05, 1))
        basemap.title.set_text('Infections on the Bus: Step 0')
        basemap.set_xlabel('Seat Column')
        basemap.set_ylabel('Seat Row')
        basemap.set_xticks(list(range(0,model.max_columns,model.seat_dist)))
        basemap.set_yticks(list(range(0,model.max_rows,model.seat_dist)))
        pyplot.close(basemap.get_figure())
        for x in range(num_breathes):
            nmodel.step()
            agents = nmodel.schedule.agents
            infected = gpd.GeoSeries(map(lambda a: a.shape, [agent for agent in agents if agent.infected]))
            not_infected = gpd.GeoSeries(map(lambda a: a.shape, [agent for agent in agents if not agent.infected]))
            basemap = infected.plot(c="red", label = "infected")
            not_infected.plot(c="green", label = "uninfencted", ax = basemap)
            basemap.legend(bbox_to_anchor=(1.05, 1))
            basemap.title.set_text('Infections on the Bus: Step '+ str(x+1))
            basemap.set_xlabel('Seat Column')
            basemap.set_ylabel('Seat Row')
            basemap.set_xticks(list(range(0,model.max_columns,model.seat_dist)))
            basemap.set_yticks(list(range(0,model.max_rows,model.seat_dist)))
            pyplot.close(basemap.get_figure())

    def timelapse_step_model(model, num_breathes): 
        '''
        function that lets us timelpase the model. We are assuming that there is a simulation_images folder that allows
        you to save all the images. IT IS BEST TO ONLY RUN THIS FUNCTION ONCE AND THEN CLEAR THE FOLDER OF ALL THE IMAGES.
        The final model will be saved as 'gif_of_model.png'. An example gif can be found in the visualization folder.
        - model: the model that is being visualized
        - num-breathes: the numbers of steps that you want visualized. This method will display steps 0 all the way
        until num_breathes
        '''
        nmodel = model
        agents = nmodel.schedule.agents
        infected = gpd.GeoSeries(map(lambda a: a.shape, [agent for agent in agents if agent.infected]))
        not_infected = gpd.GeoSeries(map(lambda a: a.shape, [agent for agent in agents if not agent.infected]))
        basemap = infected.plot(c="red", label = "infected")
        not_infected.plot(c="green", label = "uninfencted", ax = basemap)
        basemap.legend(bbox_to_anchor=(1.05, 1))
        basemap.title.set_text('Infections on the Bus: Step 0')
        basemap.set_xlabel('Seat Column')
        basemap.set_ylabel('Seat Row')
        basemap.set_xticks(list(range(0,model.max_columns,model.seat_dist)))
        basemap.set_yticks(list(range(0,model.max_rows,model.seat_dist)))
        basemap.get_figure().savefig('simulation_images/0.png', bbox_inches='tight')
        pyplot.close(basemap.get_figure())
        for x in range(num_breathes):
            nmodel.step()
            agents = nmodel.schedule.agents
            infected = gpd.GeoSeries(map(lambda a: a.shape, [agent for agent in agents if agent.infected]))
            not_infected = gpd.GeoSeries(map(lambda a: a.shape, [agent for agent in agents if not agent.infected]))
            basemap = infected.plot(c="red", label = "infected")
            not_infected.plot(c="green", label = "uninfencted", ax = basemap)
            basemap.legend(bbox_to_anchor=(1.05, 1))
            basemap.title.set_text('Infections on the Bus: Step '+ str(x+1))
            basemap.set_xlabel('Seat Column')
            basemap.set_ylabel('Seat Row')
            basemap.set_xticks(list(range(0,model.max_columns,model.seat_dist)))
            basemap.set_yticks(list(range(0,model.max_rows,model.seat_dist)))
            basemap.get_figure().savefig('simulation_images/'+str(x+1)+'.png', bbox_inches='tight')
            pyplot.close(basemap.get_figure())
        frames = []
        imgs = glob.glob("simulation_images/*.png")
        filler_list = []
        for i in imgs: 
            filler_list.append(re.findall('\d+', i)[0])
        filler_list.sort(key = int)
        for i in range(len(filler_list)):
            filler_list[i] = 'simulation_images/'+filler_list[i]+'.png'

        for i in filler_list:
            new_frame = Image.open(i)
            frames.append(new_frame)

        # Save into a GIF file that loops forever
        frames[0].save('gif_of_model.gif', format='GIF',
                    append_images=frames[1:],
                    save_all=True,
                    duration=300, loop=0)