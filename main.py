import contextlib

from utils import functionalities, multiplayer_functionalities, selected_letters

print(
    """
1. Press(1) for single player
2. Pres s(2) for multiplayer
3. Press(3) for single player vs computer
4. Press(4) for computer vs computer
"""
)

selected_game_mode = None

while True:
    with contextlib.suppress(KeyboardInterrupt):
        # game_mode = input("Choose game mode: ")
        game_mode = "2"
        selected_game_mode = functionalities.choose_game_mode(game_mode)
        # Validating game mode selection
        if not selected_game_mode["status"]:
            print(selected_game_mode["message"])
            continue
        print(f"{selected_game_mode['message']}")
        break
with contextlib.suppress(KeyboardInterrupt):
    # Selection of difficulty | wrong input equals random difficulty
    # difficulty_level = input("Difficulty level (easy, medium, hard): ")
    difficulty_level = "easy"

    # Selecting scores and words based on difficulty level
    words = functionalities.clean_words(difficulty_level)
    # Assigning random word
    random_word = functionalities.generate_random_word(words)
    list_random_word = list(random_word)
    # Hiding random word
    dashed_random_word = functionalities.hide_random_word(random_word)


# Hangman Logic
def single_player():
    print(random_word)
    score = functionalities.score_selection(difficulty_level)
    while True:
        # Score board and used letters board
        print(
            f"Remaining score: {score}, wrong letters you have chosen: {selected_letters}"
        )
        print(dashed_random_word)
        user_choice = input("Guess a letter in the word: ").lower()
        if len(user_choice) > 1:
            print("Select only one letter")
            continue
        check_user_choice = functionalities.check_existence(
            list_random_word, user_choice
        )
        if check_user_choice["status"]:
            position_of_letter = check_user_choice["position"]
            dashed_random_word[position_of_letter] = list_random_word[
                position_of_letter
            ]
            list_random_word[position_of_letter] = "_"
        # Handles the absence of users choice
        if not check_user_choice["status"]:
            chosen = functionalities.chosen(selected_letters, user_choice, score)
            if not chosen:
                print(f"'{user_choice}' not in word or no longer exists")
                score -= 1
            if chosen:
                print(f"'{user_choice} already taken'")
        # Game over logic
        if score == 0:
            print(f"You run out of scores, the correct word was '{random_word}'")
            break
        # Checking if guessed words is equal to random word
        if "".join(dashed_random_word) == random_word:
            print(f"You won, the word is {random_word}")
            break


def multiplayer():
    # Getting user names
    # player_1 = input("Player 1 input your name: ").capitalize()
    # player_2 = input("Player 2 input your name: ").capitalize()
    player_1 = "111"
    player_2 = "222"
    # Random word
    print(random_word)
    # List random word for both players
    (
        player1_list_random_words,
        player2_list_random_words,
    ) = list_random_word, list(random_word)
    score = functionalities.score_selection(difficulty_level)
    print(score)
    # Dashed words for player 1
    player_1_dashed_words = dashed_random_word
    # Dashed words for player 2
    player_2_dashed_words = functionalities.hide_random_word(random_word)
    while True:
        print()
        # Score board and used letters board
        print(
            f"Remaining score: {score}, wrong letters you have chosen: {selected_letters}"
        )

        print(f"Player One board ->  {player1_list_random_words}")
        print(f"Player Two board -> {player2_list_random_words}")
        print()
        # Showing dashed words
        print(f"{player_1}(player 1) dashed words")
        print(player_1_dashed_words)
        print()
        print(f"{player_2}(player 2) dashed words")
        print(player_2_dashed_words, "******88")

        # Player one choice
        player1_choice = multiplayer_functionalities.validate_user_input(
            "player1", f"{player_1}"
        )
        # Checking if player one has already chosen a letter
        check_player1_choice = functionalities.check_existence(
            list_random_word, player1_choice
        )
        # Replacing correct guessed word with "_" in list random word
        multiplayer_functionalities.get_word_position(
            player1_list_random_words, player_1_dashed_words, check_player1_choice
        )

        print()
        # Player two choice
        player2_choice = multiplayer_functionalities.validate_user_input(
            "player2", f"{player_2}"
        )
        check_player2_choice = functionalities.check_existence(
            list_random_word, player2_choice
        )
        # Replacing correct guessed word with "_" in list random word
        multiplayer_functionalities.get_word_position(
            player2_list_random_words, player_2_dashed_words, check_player2_choice
        )


def computer_vs_single_player():
    print("computer vs single player")


def computer_vs_computer():
    print("computer vs computer")


if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt):
        if selected_game_mode["mode"] == "single player":
            single_player()
        if selected_game_mode["mode"] == "multiplayer":
            multiplayer()
        if selected_game_mode["mode"] == "computer vs single player":
            computer_vs_single_player()
        if selected_game_mode["mode"] == "computer vs computer":
            computer_vs_computer()


# Features
# 1. Score won't decrease if choice already exist in chosen words
