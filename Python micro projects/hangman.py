from __future__ import division, absolute_import, print_function, unicode_literals
from random import choice
try:
  from future_builtins import *
except ImportError:
  pass

try:
  input = raw_input
  range = xrange
except NameError:
  pass
HANGMAN_PICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def get_random_word():
    # gets a random word from wordlist.txt.
    # words in the wordlist must be a single word
    # seperated by a newline (no phrases)
    with open('wordlist.txt', 'r') as filedata:
      choosen_word = choice(filedata.readlines())
      return choosen_word.strip() #remove the carriage return with strip()

def display_board(HANGMAN_PICS, missed_letters, correct_letters, secrect_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secrect_word)

    for i in range(len(secrect_word)): # replace blanks with correctly guessed letters
        if secrect_word[i] in correct_letters:
            blanks = blanks[:i] + secrect_word[i] + blanks[i+1:]

    for letter in blanks: # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

def get_guess(already_guessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def play_again():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


print('Goodluck!')
missed_letters = ''
correct_letters = ''
secrect_word = get_random_word().lower()
gameIsDone = False

while True:
    display_board(HANGMAN_PICS, missed_letters, correct_letters, secrect_word)

    # Let the player type in a letter.
    guess = get_guess(missed_letters + correct_letters)

    if guess in secrect_word:
        correct_letters = correct_letters + guess

        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secrect_word)):
            if secrect_word[i] not in correct_letters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secrect_word + '"! You have won!')
            gameIsDone = True
    else:
        missed_letters = missed_letters + guess

        # Check if player has guessed too many times and lost
        if len(missed_letters) == len(HANGMAN_PICS) - 1:
            display_board(HANGMAN_PICS, missed_letters, correct_letters, secrect_word)
            print('You have run out of guesses!\nAfter ' + str(len(missed_letters)) + ' missed guesses and ' + str(len(correct_letters)) + ' correct guesses, the word was "' + secrect_word + '"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if play_again():
            missed_letters = ''
            correct_letters = ''
            gameIsDone = False
            secrect_word = get_random_word()
        else:
            break