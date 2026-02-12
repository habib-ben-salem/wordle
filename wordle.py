import random

class Wordle:
    def __init__(self):
        self.words = []
        self.load_words()
        self.word_to_guess = random.choice(self.words)

    def load_words(self):
        with open('words.txt', 'r') as file:
            self.words = [line.strip() for line in file.readlines()]

    def validate_guess(self, guess):
        return guess in self.words

    def start_game(self):
        # existing game logic
        pass

    def display_ui(self):
        # existing UI styling
        pass
