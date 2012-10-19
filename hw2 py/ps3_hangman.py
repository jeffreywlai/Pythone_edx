# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    if secretWord == '':
        return True
    else:
        if lettersGuessed.count(secretWord[0]) > 0:
            return isWordGuessed(secretWord[1:], lettersGuessed)
        else:
            return False


def getGuessedWord(secretWord, lettersGuessed):
    if len(secretWord) == 0:
        return ''
    else:
        if lettersGuessed.count(secretWord[0]) > 0:
            return secretWord[0] + ' ' + getGuessedWord(secretWord[1:], lettersGuessed)
        else:
            return '_ ' + getGuessedWord(secretWord[1:], lettersGuessed)


def getAvailableLetters(lettersGuessed):
    lettersLeft = 'abcdefghijklmnopqrstuvwxyz'
    x = lettersGuessed[:]
    while len(x) > 0:
        g = x.pop(0)
        if lettersLeft.find(g) != -1:
            lettersLeft = lettersLeft[0:lettersLeft.find(g)] + lettersLeft[lettersLeft.find(g)+1:]
    return lettersLeft
    

def hangman(secretWord):
    L = len(secretWord)
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is "+(str(L))+" letters long.")
    print ("-------------")
    tries = 8
    lettersGuessed = []
    guessedLetters = []
    string1 = ''
    while tries > 0:
        print ("You have "+str(tries)+" guesses left")
        print ("Available letters: "+getAvailableLetters(lettersGuessed))
        a = raw_input("Please guess a letter: ").lower()
        if a in getAvailableLetters(lettersGuessed):
            lettersGuessed.append(a)
        else:
            while (not a.isalpha()) or a in (lettersGuessed):
                print ("Oops! You've already guessed that letter: "+ getGuessedWord(secretWord, lettersGuessed))
                print ("-------------")
                print ("You have "+str(tries)+" guesses left")
                print ("Available letters: "+getAvailableLetters(lettersGuessed))
                a = raw_input("Please guess a letter: ").lower()
            lettersGuessed.append(a)
        if a in secretWord:
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            print ("-------------")
        else:
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            print ("-------------")
            tries -= 1
        if isWordGuessed(secretWord,lettersGuessed):
            print ("Congratulations, you won!")
            break
    if tries <= 0:
         print ("Sorry, you ran out of guesses. The word was "+str(secretWord)+".")





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
secretWord = "cunt"