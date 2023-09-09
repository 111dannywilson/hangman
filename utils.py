from random import choice
from string import ascii_lowercase

from words import words

# VARIABLES
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
            return list(valid_words)
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
        return choice(words)

    # Turn every letter to "_"
    def hide_random_word(self, random_word: str):
        return ["_" for _ in random_word]

    # Check if input can be found in word
    def check_existence(self, word: list, letter: str):
        return {
            "status": letter in word,
            "position": word.index(letter) if letter in word else False,
        }

    # Checking if user choice already in selected words
    def chosen(self, collection_data: set, user_choice: str):
        """If choice already taken, score does not deduct"""
        if user_choice not in collection_data:
            collection_data.add(user_choice)
            return False
        # print(f"{user_choice} already chosen")
        return True

    # Assigning scores based on difficulty level
    def score_selection(self, mode: str):
        if mode == "easy":
            return 3
        if mode == "medium":
            return 4
        return 6 if mode == "hard" else 2


class MultiplayerFunctionalities:
    # Check if user's input is in random word
    def validate_user_input(self, player, player_type):
        while True:
            player_choice = input(f"{player} {[player_type]} guess a letter: ").lower()
            if len(player_choice) > 1 or player_choice.strip() == "":
                print(f"{player_type} select only one letter or at least one letter")
                continue
            if player_choice in ascii_lowercase:
                return player_choice
            print(f"{player_type} select a valid letter")

    # Getting the position correct guesses
    def get_word_position(
        self, list_random_word: list, dashed_random_word: list, check_user_choice: dict
    ):
        if check_user_choice["status"]:
            position_of_letter = check_user_choice["position"]
            dashed_random_word[position_of_letter] = list_random_word[
                position_of_letter
            ]
            list_random_word[position_of_letter] = "_"

    # Storing wrongly chosen words
    def chosen_words(
        self, user_choice: str, list_random_word: list, collection_data: set
    ):
        if user_choice not in list_random_word:
            collection_data.add(user_choice)

    # Choosing winner and draw Logic
    def check_winner(self, p1_score: int, p1_name: str, p2_score: int, p2_name: str):
        if p1_score == 0 and p2_score == 0:
            print("Draw no one won")
            exit()
        if p1_score > 0 and p2_score == 0:
            print(f"Player 1 wins [{p1_name}]")
            exit()
        if p2_score > 0 and p1_score == 0:
            print(f"Player 2 wins [{p2_name}]")
            exit()


# Hangman functionalities instance
functionalities = Functionalities()
# Multiplayer functionalities
multiplayer_functionalities = MultiplayerFunctionalities()
