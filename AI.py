from random import random
from player import Player

class AI(Player):

    def __init__(self, name):
        super.__init__(name)
    
    def choose_gesture(self):
        self.chosen_gesture = self.gesture(random.randint(0,4))
        print(f"{self.name} has chosen {self.chosen_gesture}")