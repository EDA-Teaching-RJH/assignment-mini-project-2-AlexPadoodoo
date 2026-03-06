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

        roll_score, scoring_count = calculate_score(roll) #Calculate score to see how many points have been rolled
        if roll_score == 0:
            print("***********************************")
            print("BUST! You lost your turn points.")
            print("***********************************")
            return 0
        turn_score += roll_score   #Adds roll points to total score
        dice_to_roll -= scoring_count #Remove the dice used for scoring

        if dice_to_roll = 0:
            print("All dice have been scored! You get 6 new dice.")
            dice_to_roll = 6 #Resets to 6 dice for the next roll
            print(f"Current Turn score: {turn_score}")