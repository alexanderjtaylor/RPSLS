import random


# from player import Player

class AI:

    def __init__(self, name):
        self.name = name
        self.rounds_won = 0
    
    def choose_gesture(self):
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        num_chosen = random.randint(0,4)
        self.chosen_gesture = gesture_list[num_chosen]
        print(f"{self.name} has chosen {self.chosen_gesture}")