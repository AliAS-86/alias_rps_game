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
        self.game_announcement(ann_type="General", msg=f"Hello {self.player_1_name} and {self.player_2_name}, you are going to play {self.num_of_games} games with {self.num_of_rounds_per_game} round(s) each. Good luck!!! \n(Enter q, exit, bye, quit at any point of the game to exit the game)")
        self.game_engine(self.game_mode, self.player_1_name, self.player_2_name, self.num_of_games, self.num_of_rounds_per_game)


    def get_player_name(self, player, mode=None):
        """Docustring placeholder for class"""
        player_name = ""
        # print(f"game mode from get_player_name: {mode}")
        computer_names_list = ["superman", "ironman", "spiderman", "capitan america", "antman", "the flash", "batman", "the flash"]
        if mode == "1" or not mode:
            player_name = input(f"Please enter player {player} name: ")
        elif mode == "2":
            player_name = random.choice(computer_names_list)
        
        return player_name
  
    def get_game_mode(self):
        """Docustring placeholder for class"""
        is_valid = False
        while not is_valid:
            status, user_input = utls.validated_input("\nIs this game going to be:\n1) 2P (2 humans) or\n2) 1P (human vs Computer)\n3) q to exit the game\nenter 1 or 2 or q\n", "game_mode_val_data")
            if not status:
                self.game_announcement(ann_type="Warning", msg="Invalid input, please try again")
                
            elif status:
                is_valid = True
        return user_input
    
    def get_num_of_games(self):
        """a function that asks the user how many games they want to play"""
        is_valid = False
        while not is_valid:  
            try:
                user_input = int(input("Hello players, How many games are you planning to play? "))
                if user_input <= 0:
                    self.game_announcement(ann_type="Warning", msg="Invalid input, please enter a positive number that is 1 or higher or q to exit")
                # print(f"user_input: {user_input}, input type: {type(user_input)}")
                else:
                    is_valid = True
            except ValueError:
                self.game_announcement(ann_type="Warning", msg="Invalid input, please try again by entering a number")

        return user_input
                
    
    def get_num_of_rounds_per_game(self):
        """a function that asks the user how many rounds per game they want to play"""
        is_valid = False
        while not is_valid:    
            try:
                user_input = int(input("Hello players, How many rounds per game are you planning to play? "))
                # validation = utls.input_validator(user_input, int)
                if user_input <= 0:
                    self.game_announcement(ann_type="Warning", msg="Invalid input, please enter a positive number that is 1 or higher or q to exit")
                else:
                    is_valid = True
                
            except ValueError:    
                self.game_announcement(ann_type="Warning", msg="Invalid input, please try again by entering a number")
        return user_input
    
    def game_announcement(self,ann_type=None ,msg=None):
        """Docustring placeholder for class"""

        print(f"{ann_type} announcement: {msg}")
    
    def game_engine(self, mode, player_1, player_2, games, rounds):
        """Docustring placeholder for class"""
        
        game_counter = 1
        player_1_total_score = 0
        player_2_total_score = 0

        while game_counter <= games:
            round_counter = 1
            player_1_score = 0
            player_2_score = 0
            round_winner = ""
            while round_counter <= rounds:
                round_result = self.round_execution(mode, player_1, player_2)
                if round_result == player_1:
                    player_1_score += 1
                    self.game_announcement(ann_type="Score", msg=f"current score now: {player_1}: {player_1_score} / {player_2}: {player_2_score}")

                elif round_result == player_2:
                    player_2_score += 1
                    self.game_announcement(ann_type="Score", msg=f"current score now: {player_1}: {player_1_score} / {player_2}: {player_2_score}")

                elif round_result == "Tie":
                    self.game_announcement(ann_type="Score", msg=f"current score now: {player_1}: {player_1_score} / {player_2}: {player_2_score}")
                round_counter += 1
            if player_1_score > player_2_score:
                round_winner = player_1
                player_1_total_score += 1
            elif player_1_score < player_2_score:
                round_winner = player_2
                player_2_total_score += 1
            elif player_1_score == player_2_score:
                round_winner = "No winner"
            self.game_announcement(ann_type="Round", msg=f"All {rounds} reound(s) of game {game_counter} of {games} are done...")
            self.game_announcement(ann_type="Round", msg=f"Game {game_counter} of {games}:\nRound winner: {round_winner}\nGame standings:\n{player_1}: {player_1_total_score}\n{player_2}: {player_2_total_score}")
            round_counter = 1
            game_counter += 1
            player_1_score = 0
            player_2_score = 0

        if player_1_total_score > player_2_total_score:
            self.game_announcement(ann_type="Game", msg=f"All games have been played\n{player_1} is the winner with a final score of {player_1_total_score}")
        elif player_1_total_score < player_2_total_score:
            self.game_announcement(ann_type="Game", msg=f"All games have been played\n{player_2} is the winner with a final score of {player_2_total_score}")
        elif player_1_total_score == player_2_total_score:
            self.game_announcement(ann_type="Game", msg="All games have been played\nThere is no winner, it's a Tie")
        
        self.game_announcement(ann_type="Game", msg="This is the end of the game, thanks for playing")    
    
    def get_play(self, player):
        """Docustring placeholder for class"""
        is_valid = False
        while not is_valid:
            status, user_input = utls.validated_input(f"{player}, please enter your play (rock, paper, scissor): ", "plays_data")
            # validation = utls.data_validator(play, key="plays_data", target_json="validation_data.json")

            if status == 0:
                self.game_announcement(ann_type="Warning", msg="Invalid play, please retry by entering rock, paper, or scissor")
            elif status == 1:
                is_valid = True
        return user_input
            

    def get_auto_play(self):
        """Docustring placeholder for class"""
        play = ["rock", "paper", "scissor"]
        return random.choice(play)
    
    def round_execution(self, mode, player_1, player_2):
        """Docustring placeholder for class"""
        player_1_play, player_2_play = self.get_round_plays(mode, player_1, player_2)
        winner = self.determine_winner(player_1, player_2, player_1_play, player_2_play)
        self.game_announcement(ann_type="Round", msg=f"{player_1}'s play: {player_1_play}, {player_2}'s play: {player_2_play}\nThis rounds go to {winner}")
        return winner
        
    def get_round_plays(self, mode, player_1, player_2):
        """Placeholder"""
        player_1_play = self.get_play(player_1)
        player_2_play = ""
        if mode == "1":
            player_2_play = self.get_play(player_2)
        elif mode == "2":
            player_2_play = self.get_auto_play()
        
        return player_1_play, player_2_play
        
    def determine_winner(self, player_1, player_2, player_1_play, player_2_play):
        """Placeholder"""
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
