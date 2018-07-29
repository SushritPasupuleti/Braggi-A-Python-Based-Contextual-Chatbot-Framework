import json
from rest_api import views
from rest_api.Braggi_Engine import *
from rest_api.Braggi_Engine import Run

def parse_input(raw_input):
    '''Takes in data from the user request and runs ML'''
    raw_input = json.dumps(raw_input)
    processed_out = json.loads(raw_input)

    braggi_in = processed_out['user_in']

    processed_out['braggi_out'] = (Run.Run_Model(braggi_in))

    print(processed_out)
    return processed_out
