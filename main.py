from utils import functionalities, letters


def main():
    random_word = functionalities.generate_random_word()
    print(random_word)
    list_random_word = [letter for letter in random_word]
    functionalities.hide_random_word(random_word)
    # Full word is going to the final users word
    wrong_words = set()
    hidden_words = functionalities.hide_random_word(random_word)
    full_word = ""
    while True:
        choice = input("choose a letter that could match")
        wrong_words.add(choice)
        if "".join(hidden_words) == random_word:
            print("you won")
            break

        if choice in wrong_words:
            print("Letter already chosen")

        if choice not in letters:
            print("input valid letter")
        # print(choice)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
