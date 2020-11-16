

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#

import sys
import json
import pandas as pd

sys.path.insert(0, 'src')
from passengerBusABM import busAgent, NaiveModel
from visualization import visualize_step_model
from timelapse import timelapse_step_model



def main(targets): 

    abm_config = json.load(open('config/abm_params.json'))
    model_config = json.load(open('config/model_params.json'))
    visualization_config = json.load(open('config/visualization_params.json'))


    # makes the bus-passenger ABM
    if 'abm' in targets: 
        busABM = NaiveModel(busAgent, **abm_config)

    if 'model' in targets: 
        visualize_step_model(busABM, **model_config)

    if 'visualize' in targets:
        timelapse_step_model(**visualization_config)



      
        
if __name__ == '__main__':

    targets = sys.argv[1:]
    main(targets)