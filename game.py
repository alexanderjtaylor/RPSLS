
from user import User
from ai import AI
from time import sleep


class Game():

    def __init__(self):
        self.player1 = User("Player 1")
        self.player2 = AI("CPU")

    def run_game(self):
        self.display_welcome()
        self.whos_playing()
        self.battle_phase()
        self.display_winner()
        self.play_again()

    def display_welcome(self):
        print("Welcome to Rock Paper Scissors Lizard Spock")
        sleep(1)
        print("Each game with be best 2 out of 3")
        print("Use number keys to make your selection")
        sleep(1)
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
        valid_user_entry = False
        while valid_user_entry == False:
            self.num_players = input("How many players? 1, 2, or 3 for a surprise ")
            sleep(1)
            print("Choose 0 for Rock")
            print("Choose 1 for Paper")
            print("Choose 2 for Scissors")
            print("Choose 3 for Lizard")
            print("Choose 4 for Spock")
            sleep(1)
            if self.num_players == "1":
                self.player1 = User("Player 1")
                self.player2 = AI("CPU")
                valid_user_entry = True
            elif self.num_players == "2":
                self.player1 = User("Player 1")
                self.player2 = User("Player 2")
                valid_user_entry = True
            elif self.num_players == "3":
                self.player1 = AI("CPU1")
                self.player2 = AI("CPU2")
                valid_user_entry = True
            else:
                print("Invalid entry...")


    def battle_phase(self):
        while self.player1.rounds_won < 2 and self.player2.rounds_won < 2:
            self.player1.choose_gesture()
            self.player2.choose_gesture()
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
        sleep(1)
        print(f"{winner} is the winner!")

    def play_again(self):
        play_again_user_input = input("Do you want to play again? ('y'/'n'): ")
        if play_again_user_input == "y":
            self.run_game()
        elif play_again_user_input == "n":
            pass
        else:
            print("Invalid entry...")