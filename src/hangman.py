from Round import Round
import sys


def start_game():
    param = input(
"""\nЕсли хотите поиграть, нажмите 1.
Чтобы выйти из игры, нажмите 2.
""")
    if param == '1':
        print("\033[H\033[J")
        return Round()
    elif param == '2':
        sys.exit('Увидимся в следующий раз.')
    else:
        print("\033[H\033[J")
        print('Вы ввели неверный параметр.')
        return start_game()


try:
    while True: 
        round = start_game()
        round.change_output('r')
        
        while round.counter < round.fail_count and not round.check_win():
            letter = input('\n\nЗагадано слово на русском языке. Введите букву:')
            round.change_output(letter)

        if round.check_win():
            print('\n\nПоздравляю с победой!')
        else:
            print('\n\nВы проиграли. Загаданное слово:', round.word)

except FileNotFoundError:
    print('Словарь не найден.')
except IndexError:
    print('Ошибка индексирования.')