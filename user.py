from player import Player

class User(Player):
    
    def __init__(self, name):
        super.__init__(name)
        
    def choose_gesture(self):
        self.chosen_gesture = input("Enter your pick: ")
        print(f"{self.name} has chosen {self.chosen_gesture}")