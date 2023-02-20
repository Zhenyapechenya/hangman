import random


class Round:

    def __init__(self):
        self.counter = 0
        self.fail_count = 6
        self.word = self.get_random_word()
        self.hidden_output = len(self.word) * '_'
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
        if letter in round.word:
            for index in round.check_position(letter):
                self.hidden_output[index] = self.word[index]
        else:
            round.counter += 1
        print(self.output_list[self.counter])
        print(self.hidden_output)


    # def change_hangman(self):
    #     round.counter += 1
    #     print(self.output_list[self.counter])
    #     print(self.hidden_output)


    # def change_hidden_output(self, indexes):
    #     for index in indexes:
    #         self.hidden_output[index] = self.word[index]
    #     print(self.output_list[self.counter])
    #     print(self.hidden_output)


    def check_win(self):
        if self.hidden_output == self.word:
            return True
        else:
            return False
        

    def check_fail(self):
        pass


round = Round()

while round.counter < round.fail_count or round.check_win():
    letter = input('Введите букву:')
    round.change_output(letter)
    # letter = input('Введите букву:')
    # if letter in round.word:
    #     list_of_indexes = round.check_position(letter)
    #     round.change_hidden_output(list_of_indexes)
    # else:
    #     round.change_hangman()


