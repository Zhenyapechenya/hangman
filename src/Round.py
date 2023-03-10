import random
import sys


class Round:

    def __init__(self):
        self.counter = 0
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
        self.fail_count = len(self.output_list) - 1


    def get_random_word(self):
        try:
            with open("words.txt", "r") as words_file:
                words_list = []
                for w in words_file.readlines():
                    if w != '\n':
                        words_list.append(w.strip().lower())
                return random.choice(words_list)
        except FileNotFoundError:
            sys.exit('?????????????? ???? ????????????.')


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
        try:
            print("\033[H\033[J")
            if letter in self.word:
                for index in self.check_position(letter):
                    self.hidden_output[index] = self.word[index]
            elif letter == 'r':
                pass
            else:
                self.counter += 1

            print(f'\n????????????: {self.counter} ???? {self.fail_count}')
            print(self.output_list[self.counter])

            for elem in self.hidden_output:
                print(elem, end=' ')

        except IndexError:
            sys.exit('???????????? ????????????????????????????.')
        

    def check_win(self):
        if ''.join(self.hidden_output) == self.word:
            return  True
        else:
            return False
        
