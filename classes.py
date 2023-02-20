import random


class Round:

    def __init__(self):
        self.counter = 0
        self.fail_count = 6
        self.word = self.get_random_word()
        self.hidden_output = self.define_hidden_output()
        self.output_list = [
            """
   ==============
   ||       |
   ||       |       
   ||      
   ||    
   ||   
   ||      
   ||      
   ||     
   ||  
___||____________
            """,
            """
   ==============
   ||       |
   ||       |       
   ||      ( )
   ||    
   ||   
   ||      
   ||     
   ||     
   ||  
___||____________
            """,
            """
   ==============
   ||       |
   ||       |       
   ||      ( )
   ||     |   |
   ||     |   | 
   ||      ---
   ||     
   ||     
   ||  
___||____________
            """,
            """
   ==============
   ||       |
   ||       |       
   ||      ( )
   ||    /|   |
   ||   / |   | 
   ||      ---
   ||     
   ||     
   ||  
___||____________    
            """,
            """
   ==============
   ||       |
   ||       |       
   ||      ( )
   ||    /|   |\\
   ||   / |   | \\
   ||      ---
   ||      
   ||     
   ||  
___||____________
            """,
            """
   ==============
   ||       |
   ||       |       
   ||      ( )
   ||    /|   |\\
   ||   / |   | \\
   ||      ---
   ||      / 
   ||     /  
   ||  
___||____________
            """,
            """
   ==============
   ||       |
   ||       |       
   ||      ( )
   ||    /|   |\\
   ||   / |   | \\
   ||      ---
   ||      / \\
   ||     /   \\
   ||  
___||____________
            """
        ]


    def get_random_word(self):
        words_file = open("words.txt", "r")
        words_list = []
        for w in words_file.readlines():
            if w != '\n':
                words_list.append(w.strip().lower())
        words_file.close()
        return random.choice(words_list)


    def define_hidden_output(self):
        output = []
        for i in range(len(self.word)):
            output.append('_')
        return output


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

        for elem in self.hidden_output:
            print(elem, end=' ')


    def check_win(self):
        print('\n', ''.join(self.hidden_output))
        print('\n', self.word)
        if ''.join(self.hidden_output) == self.word:
            return  True
        else:
            return False




round = Round()
print(round.output_list[0])
while round.counter < round.fail_count and not round.check_win():
    letter = input('Введите букву:')
    round.change_output(letter)

if round.check_win():
    print('win')
else:
    print('fail')


