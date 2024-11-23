"""Docustring placeholder for module"""
import random

import utilities as utls

class RpcGame:
    """Docustring placeholder for class"""
    def __init__(self):   
        self.game_mode = None
        self.player_1_name = None
        self.player_2_name = None
        self.num_of_games = None
        self.num_of_rounds_per_game = None
        
    def setup_game(self):
        """Function to get game and players infor"""
        self.game_mode = self.get_game_mode()
        self.player_1_name = self.get_player_name(1, mode="1")
        self.player_2_name = self.get_player_name(2, mode=self.game_mode)
        self.num_of_games = self.get_num_of_games()
        self.num_of_rounds_per_game = self.get_num_of_rounds_per_game()
        self.game_announcement()
        self.game_engine(self.game_mode, self.player_1_name, self.player_2_name, self.num_of_games, self.num_of_rounds_per_game)


    def get_player_name(self, player, mode=None):
        """Docustring placeholder for class"""
        player_name = ""
        # print(f"game mode from get_player_name: {mode}")
        computer_names_list = ["superman", "ironman", "spiderman", "capitan america", "antman", "the flash", "batman", "the flash"]
        if mode == "1" or not mode:
            player_name = utls.input_with_interruption(f"Please enter player {player} name: ")
        elif mode == "2":
            player_name = random.choice(computer_names_list)
        
        return player_name
  
    def get_game_mode(self):
        """Docustring placeholder for class"""
        is_valid = False
        while not is_valid:
            user_input = utls.input_with_interruption("\nIs this game going to be:\n1) 2P (2 humans) or\n2) 1P (human vs Computer)\n3) q to exit the game\nenter 1 or 2 or q\n")
            trimmed_user_input = utls.spaces_trimmer(user_input)
            validation = utls.data_validator(trimmed_user_input, key="game_mode_val_data", target_json="validation_data.json")

            if not validation:
                # print(f"user_input from get_game_mode: {user_input}")
                print("Invalid input, please try again")
                # print(f"user_input from get_game_mode when validation failed: {user_input}")
            elif validation:
                is_valid = True
        return user_input
    
    def get_num_of_games(self):
        """a function that asks the user how many games they want to play"""
        is_valid = False
        while not is_valid:  
            try:
                user_input = int(utls.input_with_interruption("Hello players, How many games are you planning to play? "))
                if user_input <= 0:
                    print("Invalid input, please enter a positive number that is 1 or higher or q to exit")
                # print(f"user_input: {user_input}, input type: {type(user_input)}")
                else:
                    is_valid = True
            except ValueError:
                print("Invalid input, please try again by entering a number")

        return user_input
                
    
    def get_num_of_rounds_per_game(self):
        """a function that asks the user how many rounds per game they want to play"""
        is_valid = False
        while not is_valid:    
            try:
                user_input = int(utls.input_with_interruption("Hello players, How many rounds per game are you planning to play? "))
                # validation = utls.input_validator(user_input, int)
                if user_input <= 0:
                    print("Invalid input, please enter a positive number that is 1 or higher or q to exit")
                else:
                    is_valid = True
                
            except ValueError:    
                print("Invalid input, please try again by entering a number")
        return user_input
    
    def game_announcement(self, msg=None):
        """Docustring placeholder for class"""
        if msg is None:
            print(f"Hello {self.player_1_name} and {self.player_2_name}, you are going to play {self.num_of_games} games with {self.num_of_rounds_per_game} round(s) each. Good luck!!! \n(Enter q, exit, bye, quit at any point of the game to exit the game)")
        if msg:
            print(msg)
    
    def game_engine(self, mode, player_1, player_2, games, rounds):
        """Docustring placeholder for class"""
        # print(f"games data type: {type(games)}")
        game_counter = 1
        player_1_total_score = 0
        player_2_total_score = 0
        # game_winner = ""
        while game_counter <= games:
            round_counter = 1
            player_1_score = 0
            player_2_score = 0
            round_winner = ""
            while round_counter <= rounds:
                round_result = self.round_execution(mode, player_1, player_2)
                if round_result == player_1:
                    player_1_score += 1
                    print(f"current score now: {player_1}: {player_1_score} / {player_2}: {player_2_score}")

                elif round_result == player_2:
                    player_2_score += 1
                    print(f"current score now: {player_1}: {player_1_score} / {player_2}: {player_2_score}")

                elif round_result == "Tie":
                    print(f"current score now: {player_1}: {player_1_score} / {player_2}: {player_2_score}")
                
                round_counter += 1
            if player_1_score > player_2_score:
                round_winner = player_1
                player_1_total_score += 1
            elif player_1_score < player_2_score:
                round_winner = player_2
                player_2_total_score += 1
            elif player_1_score == player_2_score:
                round_winner = "No winner"
            print(f"All {rounds} reound(s) of game {game_counter} of {games} are done...")
            print(f"Game {game_counter} of {games}:\nRound winner: {round_winner}\nGame standings:\n{player_1}: {player_1_total_score}\n{player_2}: {player_2_total_score}")
            round_counter = 1
            game_counter += 1
            player_1_score = 0
            player_2_score = 0

        if player_1_total_score > player_2_total_score:
            self.game_announcement(f"All games have been played\n{player_1} is the winner with a final score of {player_1_total_score}")
        elif player_1_total_score < player_2_total_score:
            self.game_announcement(f"All games have been played\n{player_2} is the winner with a final score of {player_2_total_score}")
        elif player_1_total_score == player_2_total_score:
            self.game_announcement("All games have been played\nThere is no winner, it's a Tie")
        
        self.game_announcement(msg="This is the end of the game, thanks for playing")    
    
    @staticmethod
    def get_play(player):
        """Docustring placeholder for class"""
        is_valid = False
        while not is_valid:
            play = utls.input_with_interruption(f"{player}, please enter your play (rock, paper, scissor): ")
            validation = utls.data_validator(play, key="plays_data", target_json="validation_data.json")

            if not validation:
                print("Invalid play, please retry by entering rock, paper, or scissor")
            elif validation:    
                print(f"{player} picked {play}")
                is_valid = True
        return play
            

    @staticmethod
    def get_auto_play(player):
        """Docustring placeholder for class"""
        play = ["rock", "paper", "scissor"]
        pick = random.choice(play)
        print(f"{player} picked {pick}")
        return pick
    
    @staticmethod
    def round_execution(mode, player_1, player_2):
        """Docustring placeholder for class"""
        player_1_play = RpcGame.get_play(player_1)
        if mode == "1":
            player_2_play = RpcGame.get_play(player_2)
        elif mode == "2":
            player_2_play = RpcGame.get_auto_play(player_2)
        if (player_1_play == "paper" and player_2_play == "rock") or (player_1_play == "scissor" and player_2_play == "paper") or (player_1_play == "rock" and player_2_play == "scissor"):
            return player_1
        if (player_2_play == "paper" and player_1_play == "rock") or (player_2_play == "scissor" and player_1_play == "paper") or (player_2_play == "rock" and player_1_play == "scissor"):
            return player_2
        if player_1_play == player_2_play:
            return "Tie"
    
def main():
    """Docustring"""
    new_game = RpcGame()
    new_game.setup_game()

if __name__ == "__main__":
    main()
