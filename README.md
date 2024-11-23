RPS Game requires 2 players, 1 must be human.
- 2 human players available under 2P mode
- 1 human player vs computer under 1P mode
when intiailizing a new game:
- Game mode from get_game_mode @staticmethod
    Expected inputs:
    - 1 for 2P mode
    - 2 for 1P mode
- Players names:
    - if 2P mode: get 1P and 2P names using get_player_name @staticmethod
    - if 1P mode: get 1P name using get_player_name @staticmethod
    - if 1P mode: get a random name for the computer using get_player_name @staticmethod
- How many games players wants to play?
    - Ask players to input the number of games they want to play during the session using num_of_games @staticmethod
- How many rounds per game the players want to play?
    - Ask players to input the number of rounds per game using num_of_rounds_per_game @staticmethod
- Once the above finished during the game initiation an announcement of the above data to be performed using the game_announcement instance method