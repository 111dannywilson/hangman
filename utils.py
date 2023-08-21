from random import choice
from string import ascii_letters
from words import words

# VARIABLES
letters = ascii_letters
selected_letters = set()


class Functionalities:
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

    # Check if input can be found in word
    def check_existence(self, word: list, letter: str):
        return {
            "status": letter in word,
            "position": word.index(letter) if letter in word else False,
        }

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


functionalities = Functionalities()
