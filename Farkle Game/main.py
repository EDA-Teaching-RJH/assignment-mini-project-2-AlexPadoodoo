# Main Farkle Python Function

import random #Simulate the dice rolling
from farkle_lib import Validator, calculate_score #Imports the custom library functions
import csv #Used for saving and loading game data
import os #Used for checking if the save file exists

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
        self.history_file = "farkle_history.csv" #File to save game history

def play_turn(self):
    turn_score = 0
    dice_to_roll = 6

    while True:
        print(f"\n Rolling {dice_to_roll} dice...")

        roll = [random.randint(1, 6) for i in range(dice_to_roll)]