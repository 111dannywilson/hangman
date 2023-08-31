from random import choice
from string import ascii_letters, digits

from words import words

# VARIABLES
letters = ascii_letters
# Selected Letters for single player
selected_letters = set()
# Selected letters for multi players
player1_selected_words = set()
player2_selected_words = set()


class Functionalities:
    # Output
    def data_output(self, status, message, mode):
        return {"status": status, "message": message, "mode": mode}

    # Choosing game mode
    def choose_game_mode(self, game_mode: str):
        if game_mode not in ["1", "2", "3", "4"]:
            return self.data_output(False, "Please input a valid option", None)
        if game_mode == "1":
            return self.data_output(True, "single player selected", "single player")
        if game_mode == "2":
            return self.data_output(True, "multiplayer selected", "multiplayer")
        if game_mode == "3":
            return self.data_output(
                True, "computer vs single player selected", "computer vs single player"
            )
        if game_mode == "4":
            return self.data_output(
                True, "computer vs computer selected", "computer vs computer"
            )

    # Remove words with " " and "-"... and sets difficulty level
    def clean_words(self, mode):
        difficulty_levels = ["easy", "medium", "hard"]
        valid_words = [word for word in words if " " not in word and "_" not in word]

        # Checking if difficulty mode is valid
        if mode not in difficulty_levels:
            print("Random difficulty selected")
            random_words = [word for word in valid_words]
            return random_words
        # Setting difficulty level
        word_difficulty = {
            "easy": [word for word in valid_words if len(word) <= 4],
            "medium": [word for word in valid_words if 5 <= len(word) <= 9],
            "hard": [word for word in valid_words if len(word) >= 10],
        }

        # Return words based on difficulty level
        return word_difficulty.get(mode, "")

    # Random select a random word
    def generate_random_word(self, words):
        random_word = choice(words)
        return random_word

    # Turn every letter to "_"
    def hide_random_word(self, random_word: str):
        random_word = ["_" for _ in random_word]
        return random_word
        s

    # Check if input can be found in word
    def check_existence(self, word: list, letter: str):
        return {
            "status": letter in word,
            "position": word.index(letter) if letter in word else False,
        }

    # Checking if user choice already in selected words
    def chosen(self, collection_data: set, user_choice: str, score: int):
        """If choice already taken, score does not deduct"""
        if user_choice not in collection_data:
            collection_data.add(user_choice)
            return False
        if user_choice in collection_data:
            # print(f"{user_choice} already chosen")
            return True

    # Assigning scores based on difficulty level
    def score_selection(self, mode: str):
        score = (
            3
            if mode == "easy"
            else 4
            if mode == "medium"
            else 6
            if mode == "hard"
            else 2
        )
        return score


class MultiplayerFunctionalities:
    # Initializing players word collection
    def __init__(self, player1_selected_words: set, player2_selected_words: set):
        self.player1_selected_words = player1_selected_words
        self.player2_selected_words = player2_selected_words

    # Check if user's input is in random word
    def validate_user_input(self, player, player_type):
        while True:
            player_choice = input(f"{player} {[player_type]} guess a letter: ")
            if len(player_choice) > 1 or player_choice.strip() == "":
                print(f"{player_type} select only one letter or at least one letter")
            else:
                return player_choice
                break

    # Getting the position correct guesses
    def get_word_position(self, list_random_word: str, dashed_random_word: list, check_user_choice:dict):
        if check_user_choice["status"]:
            position_of_letter = check_user_choice["position"]
            dashed_random_word[position_of_letter] = list_random_word[
                position_of_letter
            ]
            list_random_word[position_of_letter] = "_"
    
# Hangman functionalities instance
functionalities = Functionalities()
# Multiplayer functionalities
multiplayer_functionalities = MultiplayerFunctionalities(player1_selected_words, player2_selected_words)
