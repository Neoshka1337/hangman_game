from game import Game

progress = True
game = Game()

while progress:
    answer = input('1 - Начать новую игру\n2 - Выйти\n')
    if answer == '1':
        game.start_game()
    elif answer == '2':
        progress = False
