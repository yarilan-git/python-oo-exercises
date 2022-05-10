"""Word Finder: finds random words from a dictionary.
   requires the random module
"""
import random


class WordFinder:
    def __init__(self, file_name):
        """
        Loads the input file into an array or words.
        Prints the number of words read from the file.
        """
        self.words = []
        self.read_file(file_name)
        print(f"{len(self.words)} words read")

    def read_file(self, file_name):
        """
        Strips the NL char from each record read and appends the word into the global words array.
        """
        try:
            word_file = open(file_name, "r")
            for word in word_file:
                self.words.append(word.rstrip())
            word_file.close()
        except:
            print("The file name provided was not found.")

    def __repr__(self):
        return "<SerialGenerator start=100 next=101>"

    
    def random(self):
        """
        Generates a random index between 0 and the numbe of words. Then, prints a word with that index.
        """
        if len(self.words) > 0:
            i = random.randint(0, len(self.words)-1)
            print(self.words[i])

class SpecialWordFinder(WordFinder):
    def __init__(self, file_name):
        super().__init__(file_name) 


    def random(self):
        """
        Generates a random index between 0 and the numbe of words. Then, prints a word with that index, if the word is not empty and if it does not contain the char '#'
        """
        if len(self.words) > 0:
            i = random.randint(0, len(self.words)-1)            
            if len(self.words[i].strip()) > 0 and "#" not in self.words[i]:
                print(self.words[i])


