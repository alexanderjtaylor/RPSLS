from player import Player
from time import sleep

class User(Player):
    
    def __init__(self, name):
        super().__init__(name)
        
    def choose_gesture(self):
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        valid_entry = False
        while valid_entry == False:
            num_chosen = int(input("Enter your pick: "))
            if num_chosen == 0 or num_chosen == 1 or num_chosen == 2 or num_chosen == 3 or num_chosen == 4:
                self.chosen_gesture = gesture_list[num_chosen]
                sleep(1)
                print(f"{self.name} has chosen {self.chosen_gesture}")
                valid_entry = True
            else:
                print("Invalid entry... try again.")