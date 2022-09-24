

from user import User
from ai import AI


class Game():

    def __init__(self):
        self.player1 = User("Player 1")
        self.player2 = AI("CPU")

    def run_game(self):
        self.display_welcome()
        self.whos_playing()
        self.battle_phase()
        self.display_winner()

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

        print("Choose 0 for Rock")
        print("Choose 1 for Paper")
        print("Choose 2 for Scissors")
        print("Choose 3 for Lizard")
        print("Choose 4 for Spock")

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


    def battle_phase(self):
        self.player1.chosen_gesture
        self.player2.chosen_gesture
        while self.player1.rounds_won < 2 and self.player2.rounds_won < 2:
            if self.player1.chosen_gesture == "Rock" and self.player2.chosen_gesture == "Lizard":
                self.player1.rounds_won += 1
                print(f"{self.player1.name} wins the round")
            elif self.player1.chosen_gesture == "Rock" and self.player2.chosen_gesture == "Scissors":    
                self.player1.rounds_won += 1
                print(f"{self.player1.name} wins the round")
            elif self.player1.chosen_gesture == "Paper" and self.player2.chosen_gesture == "Rock":    
                self.player1.rounds_won += 1
                print(f"{self.player1.name} wins the round")
            elif self.player1.chosen_gesture == "Paper" and self.player2.chosen_gesture == "Spock":    
                self.player1.rounds_won += 1
                print(f"{self.player1.name} wins the round")
            elif self.player1.chosen_gesture == "Scissors" and self.player2.chosen_gesture == "Paper":    
                self.player1.rounds_won += 1
                print(f"{self.player1.name} wins the round")
            elif self.player1.chosen_gesture == "Scissors" and self.player2.chosen_gesture == "Lizard":    
                self.player1.rounds_won += 1
                print(f"{self.player1.name} wins the round")
            elif self.player1.chosen_gesture == "Lizard" and self.player2.chosen_gesture == "Spock":    
                self.player1.rounds_won += 1
                print(f"{self.player1.name} wins the round")
            elif self.player1.chosen_gesture == "Lizard" and self.player2.chosen_gesture == "Paper":    
                self.player1.rounds_won += 1
                print(f"{self.player1.name} wins the round")
            elif self.player1.chosen_gesture == "Spock" and self.player2.chosen_gesture == "Scissors":    
                self.player1.rounds_won += 1
                print(f"{self.player1.name} wins the round")
            elif self.player1.chosen_gesture == "Spock" and self.player2.chosen_gesture == "Rock":    
                self.player1.rounds_won += 1
                print(f"{self.player1.name} wins the round")

            elif self.player2.chosen_gesture == "Rock" and self.player1.chosen_gesture == "Lizard":
                self.player2.rounds_won += 1
                print(f"{self.player2.name} wins the round")
            elif self.player2.chosen_gesture == "Rock" and self.player1.chosen_gesture == "Scissors":    
                self.player2.rounds_won += 1
                print(f"{self.player2.name} wins the round")
            elif self.player2.chosen_gesture == "Paper" and self.player1.chosen_gesture == "Rock":    
                self.player2.rounds_won += 1
                print(f"{self.player2.name} wins the round")
            elif self.player2.chosen_gesture == "Paper" and self.player1.chosen_gesture == "Spock":    
                self.player2.rounds_won += 1
                print(f"{self.player2.name} wins the round")
            elif self.player2.chosen_gesture == "Scissors" and self.player1.chosen_gesture == "Paper":    
                self.player2.rounds_won += 1
                print(f"{self.player2.name} wins the round")
            elif self.player2.chosen_gesture == "Scissors" and self.player1.chosen_gesture == "Lizard":    
                self.player2.rounds_won += 1
                print(f"{self.player2.name} wins the round")
            elif self.player2.chosen_gesture == "Lizard" and self.player1.chosen_gesture == "Spock":    
                self.player2.rounds_won += 1
                print(f"{self.player2.name} wins the round")
            elif self.player2.chosen_gesture == "Lizard" and self.player1.chosen_gesture == "Paper":    
                self.player2.rounds_won += 1
                print(f"{self.player2.name} wins the round")
            elif self.player2.chosen_gesture == "Spock" and self.player1.chosen_gesture == "Scissors":    
                self.player2.rounds_won += 1
                print(f"{self.player2.name} wins the round")
            elif self.player2.chosen_gesture == "Spock" and self.player1.chosen_gesture == "Rock":    
                self.player2.rounds_won += 1
                print(f"{self.player2.name} wins the round")

            elif self.player2.chosen_gesture == "Rock" and self.player1.chosen_gesture == "Rock":
                print("It's a tie! Try again.")
            elif self.player2.chosen_gesture == "Paper" and self.player1.chosen_gesture == "Paper":    
                print("It's a tie! Try again.")
            elif self.player2.chosen_gesture == "Scissors" and self.player1.chosen_gesture == "Scissors":    
                print("It's a tie! Try again.")
            elif self.player2.chosen_gesture == "Lizard" and self.player1.chosen_gesture == "Lizard":    
                print("It's a tie! Try again.")
            elif self.player2.chosen_gesture == "Spock" and self.player1.chosen_gesture == "Spock":    
                print("It's a tie! Try again.")

    def display_winner(self):
            if self.player1.rounds_won == 2:
                winner = self.player1.name
            else:
                winner = self.player2.name
            print(f"{winner} is the winner!")