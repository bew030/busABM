'''
sleepsdk.py is a package that compiles all the necessary methods for sleep manipulation regarding the data from the wearable 
device. Use the included final notebook to access the methods and test them. 

Last modified: September 7th. 2018
'''

__author__ = 'Bernard Wong'

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

class busABM():
    class busAgent(GeoAgent):
        '''
        This class is a representation of the agents within the bus AKA the bus passengers. Each passenger has a 
        unique ID, is placed in a specific model (or bus environment), and has a shape or location within the bus 
        environment. Along with that, each agent has an infected parameter that is false by default.
        There are a few conditions that are currently preset:
        - airborneProb: airborne probability is the probability that the user breathes, coughs, or sneezes. We 
        have it set at 50% for breathing, 30% for coughing, and 20% for sneezing, but in the future we hope to allow 
        these parameters to be changed based on user inputs. 
        - draw: this is part of the step function and essentially selects which neighbors can be potentially infected. 
        We decided to make breathing affect any neighbors 1 foot away, coughing affect any neighbors 2 feet away, and 
        sneezing affect any neighbors 6 feet away. This is based off of the research and papers that we found.
        '''
        def __init__(self, unique_id, model, shape):
            super().__init__(unique_id, model, shape)
            self.infected = False
            self.airborneProb = [.5,.3,.2]
            
        def step(self):
            draw = choice([1,3,6],1,p=self.airborneProb)[0]
            if (self.infected == True):
                self.__infect(draw)
        
        def __infect(self, infect_dist):
            neighbors = self.model.grid.get_neighbors_within_distance(self, infect_dist)
            for neighbor in neighbors:
                if neighbor.unique_id != self.unique_id:
                    if (neighbor.infected == False):
                        infected_bool = choice([True,False], p = [.05,.95])
                        neighbor.infected = infected_bool


    class NaiveModel(Model):
        '''
        this class represents the environment that the agents are present in, and the steps are the steps in the 
        agent based model. There are a few parameters that are included in this class:
        - agent_class: this is basically what the agent is, which in our case is the busAgent that we created earlier
        - dim_bus: these are the dimensions of the bus. the format is a list: [num_left_columns, num_middle_columns, 
        num right_columns, num_rows]. There will not be passengers in the middle column; this is simply to provide 
        some area between passengers (which is realistic amongst the bus).
        - distance_seats: this sets the distance between seats in feet. This will affect how close the passangers are 
        to each other and thus affect the rate of infection 
        - num_infected: this is the number of people initially infected
        '''
        def __init__(self, agent_class, dim_bus, distance_seats,num_infected):
            
            # mesa required attributes
            self.running = True 
            self.grid = GeoSpace() 
            self.schedule = BaseScheduler(self) # scheduler dictates model level agent behavior, aka. step function

            # variables used for later functions that need descriptions of the model
            self.max_columns = (dim_bus[0]+dim_bus[1]+dim_bus[2])*distance_seats
            self.max_rows = dim_bus[3]*distance_seats
            self.seat_dist = distance_seats
            
            i = 1
            for x in range(0,dim_bus[0]*distance_seats, distance_seats):
                for y in range(0,dim_bus[3]*distance_seats, distance_seats):
                    pnt = Point(x,y)
                    i += 1
                    a = agent_class(model=self, shape=pnt, unique_id="na" + str(i))
                    self.grid.add_agents(a)
                    self.schedule.add(a)
            for x in range((dim_bus[0]+dim_bus[1])*distance_seats,
                        (dim_bus[0]+dim_bus[1]+dim_bus[2])*distance_seats, distance_seats):
                for y in range(0,dim_bus[3]*distance_seats, distance_seats):
                    pnt = Point(x,y)
                    i += 1
                    a = agent_class(model=self, shape=pnt, unique_id="na" + str(i))
                    self.grid.add_agents(a)
                    self.schedule.add(a)
            infected_agents = random.sample(self.grid.agents,num_infected)
            for i in infected_agents:
                i.infected = True
                
        def step(self):
            '''        
            step function of the model that would essentially call the step function of all agents
            '''
            self.schedule.step()
            self.grid._recreate_rtree() # this is some history remaining issue with the mesa-geo package
            # what this does is basically update the new spatial location of the agents to the scheduler deliberately