import random
import os, sys


class Word_Generator():
    def __init__(self):
        self.generated_word = ''
        self.word_list_path = f'{os.path.dirname(os.path.realpath(__file__))}\words.txt'

    def generate_word(self):
        self.generated_word = random.choice(list(open(self.word_list_path,  encoding='utf-8')))
        if len(self.generated_word) < 3 or len(self.generated_word) > 8 or self.generated_word[0].istitle():
            self.generate_word()
        return self.generated_word.rstrip()



