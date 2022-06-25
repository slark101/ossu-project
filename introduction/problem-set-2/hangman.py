# Problem Set 2, hangman.py
# Name: rusdi
# Collaborators:
# Time spent:
# Solution for Problem Set 2
# https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/ps2/

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
from collections import Counter
import random
import re
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    inFile.close()
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word:str, letters_guessed:list[str]):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    secret_word_count = Counter(letters_guessed)
    for i in secret_word:
      if not secret_word_count.get(i):
        return False
    return True



def get_guessed_word(secret_word:str, letters_guessed:list[str]):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    current_guess = ''
    letters_guessed_count = Counter(letters_guessed)
    for i in secret_word:
      if letters_guessed_count.get(i):
        current_guess = current_guess+i
      else:
        current_guess = current_guess+'_ '
    return current_guess



def get_available_letters(letters_guessed:list[str]):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letter_source = string.ascii_lowercase
    letters_guessed_count = Counter(letters_guessed)
    result:list[str] = []
    for i in letter_source:
      if not letters_guessed_count.get(i):
        result.append(i)
    return ''.join(result)
    


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word = secret_word
    vowel = 'aiueo'
    guessed_letter = []
    guessed_word = get_guessed_word(word,guessed_letter)
    guess_left =6
    warning = 3
    print('Welcome to the game Hangman!')
    print(f"I am thinking of a word that is {len(word)} letters long.")
    print(f"You have {warning} warnings left.")
    print(guessed_word)
    while word != guessed_word:
      if guess_left<=0:
        print(f"Sorry, you ran out of guesses. The word was {word}.")
        break
      print(f"You have {guess_left} guesses left.")
      print("Available letters:",get_available_letters(guessed_letter))
      print("Please guess a letter:",end="")
      letter = input()
      if not letter.isalpha() or letter in guessed_letter:
        if warning==0:
          guess_left-=1
        else:
          warning-=1
        if not letter.isalpha():
          print(f"Oops! That is not a valid letter. You have {warning} warnings left: {guessed_word}")
        else:
          print(f"Oops! You've already guessed that letter. You have {warning} warnings left: {guessed_word}")
        continue
        
      new_guessed_word = get_guessed_word(word,[*guessed_letter,letter])
      if new_guessed_word == guessed_word:
        print("Oops! That letter is not in my word:",guessed_word)
        guessed_letter.append(letter)
        if letter in vowel:
          guess_left-=2
        else:
          guess_left-=1
        continue
      else:
        print("Good guess:",new_guessed_word)
        guessed_word = new_guessed_word
        guessed_letter.append(letter)
      if guessed_word == word:
        print('Congratulations, you won!')
        print(f"Your total score for this game is: {guess_left*len(set(word))}")
        break


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word:str, other_word:str):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    return bool(re.match(my_word,other_word))



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    regex:str = '^'
    no_space_word = my_word.replace(' ','')
    unique_word = ''.join(set(no_space_word))
    for i in no_space_word.lower():
      if i == '_':
        regex = regex+"(?!["+unique_word+"])[a-z]{1}"
      else:
        regex = regex+i
    regex = regex+'$'
    matched_words_limit = 20
    matched_words:list[str] = []
    index = 0
    while matched_words_limit>0 and index+1<len(wordlist):
      word = wordlist[index]
      if match_with_gaps(regex,word):
        matched_words_limit-=1
        matched_words.append(word)
      index+=1
    if not len(matched_words):
      print("No matches found")
    else:
      print(*matched_words)


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    word = secret_word
    vowel = 'aiueo'
    guessed_letter = []
    guessed_word = get_guessed_word(word,guessed_letter)
    guess_left =6
    warning = 3
    print('Welcome to the game Hangman!')
    print(f"I am thinking of a word that is {len(word)} letters long.")
    print(f"You have {warning} warnings left.")
    print(guessed_word)
    while word != guessed_word:
      if guess_left<=0:
        print(f"Sorry, you ran out of guesses. The word was {word}.")
        break
      print(f"You have {guess_left} guesses left.")
      print("Available letters:",get_available_letters(guessed_letter))
      print("Please guess a letter:",end="")
      letter = input()
      if letter == '*':
        show_possible_matches(guessed_word)
        continue
      if not letter.isalpha() or letter in guessed_letter:
        if warning==0:
          guess_left-=1
        else:
          warning-=1
        if not letter.isalpha():
          print(f"Oops! That is not a valid letter. You have {warning} warnings left: {guessed_word}")
        else:
          print(f"Oops! You've already guessed that letter. You have {warning} warnings left: {guessed_word}")
        continue
        
      new_guessed_word = get_guessed_word(word,[*guessed_letter,letter])
      if new_guessed_word == guessed_word:
        print("Oops! That letter is not in my word:",guessed_word)
        guessed_letter.append(letter)
        if letter in vowel:
          guess_left-=2
        else:
          guess_left-=1
        continue
      else:
        print("Good guess:",new_guessed_word)
        guessed_word = new_guessed_word
        guessed_letter.append(letter)
      if guessed_word == word:
        print('Congratulations, you won!')
        print(f"Your total score for this game is: {guess_left*len(set(word))}")
        break



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
