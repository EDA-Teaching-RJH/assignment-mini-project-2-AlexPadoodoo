# Main Farkle Python Function

import random #Simulate the dice rolling
from farkle_lib import Validator, calculate_score #Imports the custom library functions

class Entity:
    def __init__(self, name):
        self.name = name  #Stores the name of the player
        