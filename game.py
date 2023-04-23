from word_generator import Word_Generator
from draw_hangman import DrawHangman
from game_exceptions import CharCountException, CharLanguageException, SameCharException
import re



class Game:
    def __init__(self):
        self.error_count = 0
        self.error_chars = []
        self.word = ''
        self.is_started = False
        self.field = ''
        self.max_errors = 6
        self.error_hangman_state = ''
        self.hangman_drawer = DrawHangman()
        a = ord('а')
        self.alphabet = ''.join([chr(i) for i in range(a,a+6)] + [chr(a+33)] + [chr(i) for i in range(a+6,a+32)])
    

    def start_game(self):
        self.error_count = 0
        self.error_chars = []
        self.is_started = True
        self.word = Word_Generator().generate_word()
        print(self.word)
        self.field = list('_' * len(self.word))
        while self.is_started:
            if self.error_count > 0:
                print(self.error_hangman_state)
            print(f'Прогресс {"".join(self.field)}        Количество ошибок: {self.error_count}')
            try:
                user_char = input('Введи букву: ').lower()
                if len(user_char) > 1:
                    raise CharCountException
                elif user_char not in self.alphabet:
                    raise CharLanguageException
                elif user_char in self.error_chars or user_char in self.field:
                    raise SameCharException
            except CharCountException:   
                print('Ты ввёл больше одной буквы!')
                continue
            except CharLanguageException:
                print('Можно вводить только буквы русского алфавита!')
                continue
            except SameCharException:
                print('Ты уже пытался ввести этот символ!')
                continue
            if user_char in self.word:
                print(f'Буква {user_char}, есть в загаданном слове! :)')
                char_indxs = [i.start() for i in re.finditer(user_char, self.word)]
                for i in char_indxs:
                    self.field[i] = user_char
                if "".join(self.field) == self.word:
                    print(f'Ты победил! Загаданное слово - {self.word}. :)')
                    print(f'Потрачено попыток {len(self.word) + self.error_count}')
                    self.is_started = False
            else:
                print(f'Буквы {user_char} нет в загаданном слове, ты ошибся :(')
                self.error_count += 1
                self.error_chars.append(user_char)
                self.error_hangman_state = self.hangman_drawer.get_hangmang_state(self.error_count)
                if self.error_count == self.max_errors:
                    print(self.error_hangman_state)
                    print('Слишком много ошибок, игра окончена! :(')
                    self.is_started = False


