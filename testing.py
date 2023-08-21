import unittest
from utils import words, functionalities


# Testing class
class TestHangman(unittest.TestCase):
    # Set up test
    def setUp(self):
        self.words = words
        self.random_word = functionalities.generate_random_word()
        self.choice = "a"

    # Test if words exist
    def test_words_existence(self):
        self.assertIsNotNone(self.words)

    # Test for type of words
    def test_words_type(self):
        self.assertIsInstance(self.words, list)

    # Test if random word exist
    def test_random_word_existence(self):
        self.assertIsNotNone(self.random_word)

    # Test for type of random word
    def test_random_word_type(self):
        self.assertIsInstance(self.random_word, str)

    # Test if generate_random_word return anything
    def test_random_words_returns_something(self):
        self.assertIsNotNone(functionalities.generate_random_word())

    # Test for user input
    def test_existence_of_user_input(self):
        self.assertIsNotNone(self.choice)

    # Test for length of user input
    def test_user_input_length(self):
        self.assertEqual(len(self.choice), 1)


if __name__ == "__main__":
    unittest.main()
