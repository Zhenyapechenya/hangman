import random


def get_random_word():
    words_file = open("words.txt", "r")
    words_list = []

    for w in words_file.readlines():
        if w != '\n':
            words_list.append(w.strip().lower())

    print(words_list)
    print(random.choice(words_list))
    words_file.close()

get_random_word()


