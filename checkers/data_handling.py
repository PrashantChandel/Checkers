import pygame
import json

def get_name():
    with open('checkers/data.json') as DB:
        data_dict = json.loads(DB.read())
        return data_dict["Name"]
    
def set_name(name):
    data_dict = []
    with open('checkers/data.json', 'r') as DB:
        data_dict = json.loads(DB.read())
    with open('checkers/data.json', 'w') as DB:
        data_dict["Name"] = str(name)
        json.dump(data_dict, DB)