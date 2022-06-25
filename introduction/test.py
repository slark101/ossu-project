"""
Code for testing problem set code
"""
import re
import unittest

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open('./problem-set-3/words.txt', 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    inFile.close()
    return wordlist


def is_valid_word(word:str, hand:dict[str,int], word_list:list[str]):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    is_word_element_valid = True
    lowered_word = word.lower()
    copy_hand = hand.copy()
    for i in lowered_word:
        letter_value = copy_hand.get(i,0)
        if not letter_value:
            is_word_element_valid = False
            break
        copy_hand[i] = letter_value-1
    reg_pattern = '^'
    for i in lowered_word:
        if i=='*':
            reg_pattern+='[aiueo]+'
        else:
            reg_pattern+=i
    reg_pattern+='$'
    word_found = False
    for i in word_list:
        if bool(re.match(reg_pattern,i)):
            word_found = True
            break

    return is_word_element_valid and word_found

class TestCode(unittest.TestCase):
    def test_code(self):
        word_list = load_words()
        initial_value = {'a': 2, 'g': 1, 'l': 1, 'h': 1, '*':1}
        word = 'la*gh'
        self.assertTrue(is_valid_word(word,initial_value,word_list))

if __name__ == "__main__":
    unittest.main()