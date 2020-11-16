# Overview 
_Created by Bernard Wong and Ziqian Cui_

COVID-19 has drastically changed the way we live our lives. As of October 2020, there have been 45.5 million cases in the world and around 1.19 million deaths, making it one of the worst epidemics in history. There have been large efforts made in order to slow the spread of the disease and a lot of research is being done to find a vaccine. However, until a vaccine is created, it’s important to understand how the virus works and how it spreads in order to prevent future epidemics from happening. One of the largest industries affected by COVID-19 has been the transportation industry; as mandated quarantines were set around the world and more and more people became fearful of infection, the airline industry has lost nearly 314 billion USD. New research supports airborne transmission being one of the largest factors of the spread of the disease, and with public transports generally being small areas with recirculating air, it’s important to understand how the virus is spread and how air conditions can affect it. In doing so we can set effective guidelines that enable air to be cleaner and prevent the spread of these respiratory droplets, thus minimizing the transmission of COVID-19. 

# Navigating the Repository 
There are a lot of folders within the repository. If you're interested in seeing our project overview document, it can be found in the references folder or can be found [here](https://github.com/bew030/domain_project_template/blob/main/references/SIMULATING%20AIRBORNE%20TRANSMISSION%20OF%20SARS-CoV-2%20AMONGST%20BUS%20RIDERS%20-%20checkpoint%201.pdf). A list of our references along with the paper we're replicating can also be found in the references folder or can be found [here](https://github.com/bew030/domain_project_template/blob/main/references/references.md). 

There's a variety of packages that you need to import. One of the most important ones is mesa, which requires multiple steps. We've attached instructions for installing the package, which can be found [here](https://github.com/bew030/domain_project_template/blob/main/config/how%20to%20install%20mesa.md). Everything else in the folder is stub code, but our package installs all other necessary packages. 

Currently our notebook is the best reference for running the code (our run.py is just stub code). THIS IS THE FILE THAT YOU SHOULD INITIALLY READ THROUGH IN ORDER TO BEST UNDERSTAND OUR WORK. You can take a look at the notebook [here](https://github.com/bew030/domain_project_template/blob/main/notebooks/Example%20Notebook.ipynb). Later in the future we'll have our run code run well so that you can just immediately run it in the terminal. However, our code has been properly packaged and can be imported in the terminal. If you'd like to take a look at the package, the code is located [here](https://github.com/bew030/domain_project_template/tree/main/src/packages). 

# Using the Code 

run the following code in your Jupyter Notebook: 

```python 
from packages import busABM
from packages import visualizer
```

Run the following code in your Terminal: 

```python
pip install packages
```

The packages are divided into two things, [busABM](https://github.com/bew030/domain_project_template/tree/main/src/packages/busABM) which contains the class that creates the agents and the environments and the [visualizer](https://github.com/bew030/domain_project_template/tree/main/src/packages/visualizer) which contains methods that help visualize interactions and steps. 

# The Data 
The research paper we’re replicating is an observational study that studies a worship event and the bus travel that followed shortly after. The event had initially started off with 300 individuals with only one having COVID-191. After the event, 128 of the 300 individuals travelled by bus, with 60 participants going in bus one and 68 going in bus two. Both busses had relatively similar conditions: the air conditioning system was on a heating and recirculating mode, weather conditions were the same, and passengers remained seated during the whole duration on both busses. 
After the initial participant began to experience symptoms and received the diagnosis of COVID-19, the rest of the participants began to get tested. It was found that none of the individuals in bus one were infected but 24 individuals in bus two were infected (leading to a 35.3% infection rate). Surprisingly, of the 172 individuals who did not travel by bus after the event, only 7 were infected (leading to a 4% infection rate). Even more surprising was that the 24 individuals that were infected on bus two were scattered amongst the bus, rather than grouped closely together. A visual representation of these results can be seen below in Figure 1. 
As mentioned within the research paper, the much larger infection rate within the bus along with the lack of a significantly increased risk depending on seat location suggests that the airborne spread of the virus most likely plays a significant role in the transmission of the disease. This data is extremely helpful in our investigation and will help us better simulate the airborne transmission of the disease within a small location. By simulating the transmission of COVID-19 within the air based on these findings, we can hopefully develop an accurate simulation that can then later be applied to larger areas. 

<p align="center">
	<img src="https://github.com/bew030/domain_project_template/blob/main/src/images/results.png" />
</p>

# Visualizations 
An example of a timelapse of the steps can be seen here. 2 people are initially infected and has a 50% chance of breathing, 30% chance of coughing, and 20% chance of sneezing. If they breath, people 1 foot away have a 5% chance of being infected. If they cough, people 2 feet away have a 5% chance of being infected. If they sneeze, people 6 feet away have a 5% chance of being infected. Each step is a 'breath' action. 

<p align="center">
	<img src="https://github.com/bew030/domain_project_template/blob/main/src/images/gif_of_model.gif" />
</p>

# Work Division
Bernard worked on the packaging, github organizing and the visualizations. Ziqian worked on the agent and environment modeling. 
