import random


class Round:

    def __init__(self):
        self.counter = 0
        self.fail_count = 6
        self.word = self.get_random_word()
        self.hidden_output = len(self.word) * '_ '
        self.output_list = [
            '0',
            '1',
            '2',
            '3',
            '4',
            '5',
            '6'
        ]

    def get_random_word(self):
        words_file = open("words.txt", "r")
        words_list = []
        for w in words_file.readlines():
            if w != '\n':
                words_list.append(w.strip().lower())
        words_file.close()
        return random.choice(words_list)


    def check_position(self, letter):
        indexes = []
        for i in range(len(self.word)):
            if letter == self.word[i]:
                indexes.append(i)
        return indexes


    def change_output(self, letter):
        print(self.output_list[self.counter])
        print('Тут должна быть строка с состоянием угадываемогом слова')


    def check_fail(self):
        pass




# hidden_word = len(secret_word) * '_'
# secret_word = get_random_word()
# print(hidden_word, secret_word)
# letter = input('Введите букву:')

# if letter_in_word():
#     for i in range(len(secret_word)):
#         if letter == secret_word[i]:
#             hidden_word.find(letter)



round = Round()

while round.counter < round.fail_count:
    letter = input('Введите букву:')
    if letter in round.word:
        list_of_indexes = round.check_position(letter)



        change_output()
        check_uotput()
    else:
        counter += 1
        draw_hangman()
        check_fail()