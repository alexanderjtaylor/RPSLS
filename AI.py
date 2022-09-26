import random
from player import Player
from time import sleep

class AI(Player):

    def __init__(self, name):
        super().__init__(name)
    
    def choose_gesture(self):
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        num_chosen = random.randint(0,4)
        self.chosen_gesture = gesture_list[num_chosen]
        sleep(1)
        print(f"{self.name} has chosen {self.chosen_gesture}")