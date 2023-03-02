from Round import Round


try:
    round = Round()
    print("\033[H\033[J")
    print(round.output_list[0])
    
    while round.counter < round.fail_count and not round.check_win():
        letter = input('\n\nЗагадано слово на русском языке. Введите букву:')
        round.change_output(letter)

    if round.check_win():
        print('\n\nПоздравляю с победой!')
    else:
        print('\n\nВы проиграли. Загаданное слово:', round.word)

except FileNotFoundError:
    print('Словарь не найден')
except IndexError:
    print('Ошибка индексирования')