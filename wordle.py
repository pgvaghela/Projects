import sys
import random

sys.path.append('./files')

from wordle_words import word_list, valid_guesses

def get_user_guess(valid_guesses):
    '''
    Function that gets the guess from the user.
    Code checks that the word is in the list of `valid_guesses`
    If not in list, ask user for new word.
    Returns the word in lowercase.
    '''

    # get user input. Convert to lowercase
    guess = input('Enter your guess: ')
    guess = guess.lower()

    # loop to check that guess is valid
    while guess not in valid_guesses:
        print('Please enter a valid 5-letter word')
        guess = input('Enter your guess: ')
        guess = guess.lower()

    return guess

def update_progress(guess, word_to_guess):
    '''
    Function that updates the progress of the Wordle game.
    For each letter in the word do the following:
    -- If letter is in the correct spot, fill with that letter.
    -- If letter is correct but not in the right spot, fill with a "?"
    -- If letter is not part of the word, fill with a "_"

    e.g.
    word to guess: "table"
    user guess:    "facet"
    output:        "_a_??"
    '''

    progress = ''
    word_length = len(guess)

    for i in range(word_length):
        if guess[i] == word_to_guess[i]:
            progress += guess[i]
        elif guess[i] in word_to_guess and guess.count(guess[i]) <= word_to_guess.count(guess[i]):
            progress += '?'
        else:
            progress += '_'

    return progress

def play_wordle(word_list, valid_guesses):
    attempts = 0
    guessed_correctly = False
    # Choose a random word from the word_list
    word_to_guess = random.choice(word_list)
    ## FOR DEBUGGING PURPOSES ONLY ##
    #print(f'The chosen word is {word_to_guess}')
    # Play game!
    while attempts < 6 and not guessed_correctly:
        # get guess from user
        guess = get_user_guess(valid_guesses)
        # check if guess matches the word_to_guess
        if guess == word_to_guess:
            guessed_correctly = True
        # else, game progress gets updated
        else:
            print(update_progress(guess, word_to_guess))
            attempts += 1

    if guessed_correctly == True:
        print("Congratulations!")
    else:
        print(f'The correct word was {word_to_guess}. Try again!')

play_wordle(word_list, valid_guesses)