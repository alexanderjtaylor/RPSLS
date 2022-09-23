

from user import User
from ai import AI


class Game():

    def __init__(self):
        pass

    def run_game(self):
        self.display_welcome()
        self.whos_playing()

    def display_welcome(self):
        print("Welcome to Rock Paper Scissors Lizard Spock")

        print("Each game with be best 2 out of 3")
        print("Use number keys to make your selection")

        print("Scissors cuts paper")
        print("Paper covers rock")
        print("Rock crushes lizard")
        print("Lizard poisons Spock")
        print("Spock smashes scissors")
        print("Scissors decapitates lizard")
        print("Lizard eats paper")
        print("Paper disproves Spock")
        print("Spock vaporizes rock")
        print("Rock crushes scissors")

    def whos_playing(self):
        self.num_players = input("How many players? 1, 2, or 3 for a surprise ")

        if self.num_players == "1":
            self.player1 = User("Player 1")
            self.player2 = AI("CPU")
        elif self.num_players == "2":
            self.player1 = User("Player 1")
            self.player2 = User("Player 2")
        elif self.num_players == "3":
            self.player1 = AI("CPU1")
            self.player2 = AI("CPU2")
        else:
            print("Invaild entry...")

        print("Choose 0 for Rock")
        print("Choose 1 for Paper")
        print("Choose 2 for Scissors")
        print("Choose 3 for Lizard")
        print("Choose 4 for Spock")

    # def battle_phase(self):
    #     self.player1.chosen_gesture

       

