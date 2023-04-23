from word_generator import Word_Generator
from draw_hangman import DrawHangman
from game_exceptions import CharCountException, CharLanguageException, SameCharException
import re



class Game:
    def __init__(self):
        # Инициализация начальных переменных
        self.is_started = False
        self.max_errors = 6
        # Инициализация алафита для дальнейшей проверки
        a = ord('а')
        self.alphabet = ''.join([chr(i) for i in range(a,a+6)] + [chr(a+33)] + [chr(i) for i in range(a+6,a+32)])
    

    def initialize_game(self):
        # Инициализация игры
        self.successfull_attempts = 0
        self.error_count = 0
        self.error_chars = []
        self.is_started = True
        self.word = Word_Generator().generate_word()
        self.field = list('_' * len(self.word))

    def game_process(self):
        self.initialize_game()
        while self.is_started:
            if self.error_count > 0:
                print(self.error_hangman_state)
            print('\n' + f'Прогресс {"".join(self.field)}\tКоличество ошибок: {self.error_count}')
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
                self.successfull_attempts += 1
                print(f'Буква {user_char}, есть в загаданном слове! :)')
                char_indxs = [i.start() for i in re.finditer(user_char, self.word)]
                for i in char_indxs:
                    self.field[i] = user_char
                if "".join(self.field) == self.word:
                    print(f'Ты победил! Загаданное слово - {self.word}. :)')
                    print(f'Потрачено ходов {self.successfull_attempts + self.error_count}')
                    self.is_started = False
            else:
                print(f'Буквы {user_char} нет в загаданном слове, ты ошибся :(')
                self.error_count += 1
                self.error_chars.append(user_char)
                self.error_hangman_state = DrawHangman().get_hangman_state(self.error_count)
                if self.error_count == self.max_errors:
                    print(self.error_hangman_state)
                    print('Слишком много ошибок, игра окончена! :(')
                    print(f'Было загадано слово {self.word}')
                    self.is_started = False


