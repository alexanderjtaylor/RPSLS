

from user import User
from ai import AI


class Game():

    def __init__(self):
        User()
        AI()

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