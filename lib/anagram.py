class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, list):
        return_list = []
        for list_word in list:
            list_letters = [letter for letter in list_word]
            word_letters = [letter for letter in self.word]
            if sorted(list_letters) == sorted(word_letters):
                return_list.append(list_word)
        return return_list

# breakpoint()