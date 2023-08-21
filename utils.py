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
            return False

        # Setting difficulty level
        word_difficulty = {
            "easy": [word for word in valid_words if len(word) <= 4],
            "medium": [word for word in valid_words if 5 <= len(word) <= 9],
            "hard": [word for word in valid_words if len(word) >= 10],
        }

        # Return words based on difficulty level
        return word_difficulty.get(mode, "")

    # Random select a random word
    def generate_random_word(self):
        self.random_word = choice(words)
        return self.random_word

    # Turn every letter to "_"
    def hide_random_word(self, random_word: str):
        self.random_word = ["_" for _ in random_word]
        return self.random_word

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
            else score == 4
            if mode == "medium"
            else 6
            if mode == "hard"
            else 2
        )
        return score


functionalities = Functionalities()


# Hangman Logic
def main():
    # Selection of difficulty | wrong input equals random difficulty
    difficulty_level = input("Difficulty level (easy, medium, hard): ")

    # Selecting scores and words based on difficulty level
    score = functionalities.score_selection(difficulty_level)
    words = functionalities.clean_words(difficulty_level)
    # Assigning random word
    random_word = functionalities.generate_random_word()
    list_random_word = [ch for ch in random_word]
    dashed_random_word = functionalities.hide_random_word(random_word)
    print(random_word)

    user_choice = ""
    while True:
        print(score)
        print(dashed_random_word)
        user_choice = input("Guess a letter in the word: ")
        check_user_choice = functionalities.check_existence(
            list_random_word, user_choice
        )
        # Handles the absence of users choice
        if not check_user_choice["status"]:
            score -= 1
            selected_letters.add(user_choice)
            print(f"{user_choice} not in word")
        # Handles the presence of users choice
        if check_user_choice["status"]:
            position_of_letter = check_user_choice["position"]
            print(position_of_letter)
            dashed_random_word[position_of_letter] = list_random_word[
                position_of_letter
            ]
            list_random_word[position_of_letter] = "_"
        # Game over logic
        if score == 0:
            print("You run out of scores")
            break
        # Checking if guessed words is equal to random word
        if "".join(dashed_random_word) == random_word:
            print("You won")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
