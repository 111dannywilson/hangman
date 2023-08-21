from utils import functionalities, selected_letters


# Hangman Logic
def main():
    # Selection of difficulty | wrong input equals random difficulty
    difficulty_level = input("Difficulty level (easy, medium, hard): ")

    # Selecting scores and words based on difficulty level
    score = functionalities.score_selection(difficulty_level)
    words = functionalities.clean_words(difficulty_level)
    # Assigning random word
    random_word = functionalities.generate_random_word(words)
    list_random_word = [ch for ch in random_word]
    dashed_random_word = functionalities.hide_random_word(random_word)
    print(random_word)

    user_choice = ""
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
        # Handles the absence of users choice
        if not check_user_choice["status"]:
            score -= 1
            selected_letters.add(user_choice)
            print(f"'{user_choice}' not in word or no longer exists")
        # if user_choice in selected_letters:
        #     score += 1
        #     print(f"{user_choice} already chosen")
        # Handles the presence of users choice
        if check_user_choice["status"]:
            position_of_letter = check_user_choice["position"]
            dashed_random_word[position_of_letter] = list_random_word[
                position_of_letter
            ]
            list_random_word[position_of_letter] = "_"
        # Game over logic
        if score == 0:
            print(f"You run out of scores, the correct word was '{random_word}'")
            break
        # Checking if guessed words is equal to random word
        if "".join(dashed_random_word) == random_word:
            print(f"You won, the word is {random_word}")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass


# Features
# 1. Score won't decrease if choice already exist in chosen words
