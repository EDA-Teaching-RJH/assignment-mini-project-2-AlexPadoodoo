# Main Farkle Python Function

import random #Simulate the dice rolling
from farkle_lib import Validator, calculate_score #Imports the custom library functions

class Entity:
    def __init__(self, name):
        self.name = name  #Stores the name of the player

# Subclass representing the human player

class Player(Entity):
    def __init__(self, name):
        super().__init__(name)  #Sets a name
        self.total_score = 0 #Sets the player's game score to zero

class FarkleGame:
    def __init__(self, player_name):
        if not Validator.is_valid_name(player_name): 
            player_name = "Player"  #Sets a default name if validation fails

        self.player = Player(player_name) #Creates a new player object
        self.win_threshold = 2000 # Sets the goal to 2000 points