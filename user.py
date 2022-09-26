from player import Player

class User:
    
    def __init__(self, name):
        super().__init__()
        
    def choose_gesture(self):
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        num_chosen = int(input("Enter your pick: "))
        self.chosen_gesture = gesture_list[num_chosen]
        print(f"{self.name} has chosen {self.chosen_gesture}")