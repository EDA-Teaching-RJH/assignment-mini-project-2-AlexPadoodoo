import re # Import the regular expression library for pattern matching
from collections import Counter # Import Counter to easily count the dice occurences

#Function to implement Farkle scoring rules...
def calculate_score(dice):
    counts = Counter(dice)
    score = 0  #Sets the score to zero
    scoring_dice_count = 0 #Tracks how many dice were used to calculate the score

    for num, count in counts.items():    # Iterates through each unique die number and its frequency
        if count >= 3:
            three_score = 1000 if num == 1 else num * 100
            tier_multiplier = 2 ** (count - 3)
            score += three_score * tier_multiplier # Add the calculated triple and quadruple score
            scoring_dice_count += count # Marks all these dice as used for scoring
        else:
            if num == 1:
                score += count * 100
                scoring_dice_count += count #Marks the dice as used
            elif num == 5:
                score += count * 50
                scoring_dice_count += count
    return score, scoring_dice_count # Returns both the score and the number of dice used
            