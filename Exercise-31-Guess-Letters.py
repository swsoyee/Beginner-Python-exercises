'''
Exercise 31: Guess Letters
This exercise is Part 2 of 3 of the Hangman exercise series. 
The other exercises are: Part 1 and Part 3.

Let’s continue building Hangman. In the game of Hangman, a 
clue word is given by the program that the player has to 
guess, letter by letter. The player guesses one letter at a 
time until the entire word has been guessed. (In the actual 
game, the player can only guess 6 letters incorrectly before 
losing).

Let’s say the word the player has to guess is “EVAPORATE”.
For this exercise, write the logic that asks a player to guess
a letter and displays letters in the clue word that were 
guessed correctly. For now, let the player guess an infinite
number of times until they get the entire word. As a bonus,
keep track of the letters the player guessed and display a 
different message if the player tries to guess that letter
again. Remember to stop the game when all the letters have 
been guessed correctly! Don’t worry about choosing a word
randomly or keeping track of the number of guesses the player
has remaining - we will deal with those in a future exercise.

An example interaction can look like this:

>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
>>> Guess your letter: S
Incorrect!
>>> Guess your letter: E
E _ _ _ _ _ _ _ E
...
And so on, until the player gets the word.
'''
import re

# Solution
def modify_list(result, guess, answer):
    """
    Print all the key in dict.
    
    Arguments:
    result -- a list of the show pattern word.
    guess -- the letter of user's guess.
    answer -- the answer of word
    
    Returns:
    result -- the list of word after modified.
    
    """
    guess = guess.lower()
    answer = answer.lower()
    if guess in answer:
        index_list = [x.start() for x in re.finditer(guess, answer)]
        for i in index_list:
            result[i] = guess.upper()
    else:
        print("Letter '{}' is not in the word".format(guess.upper()))
    print(' '.join(result))
    return result
        
def win(word_list):
    """
    Check the user has guessed the right word or not.
    
    Arguments:
    word_list -- the word list.
    
    Returns:
    True/False -- return True if the word has been guessed right alse return false.
    """
    if '_' not in word_list:
        return True
    else:
        return False

def main():
    right_answer = 'EVAPORATE'
    print('Welcome to Hangman!')
    guess_list = ['_' for i in range(len(right_answer))]
    print(' '.join(guess_list))
    while True:
        guess = input('Guess your letter: ')
        guess_list = modify_list(guess_list, guess, right_answer)
        if win(guess_list) == True:
            print('You win!')
            break
    
if __name__ == "__main__":
    main()

# >>> %Run test.py
# Welcome to Hangman!
# _ _ _ _ _ _ _ _ _
# Guess your letter: e
# E _ _ _ _ _ _ _ E
# Guess your letter: a
# E _ A _ _ _ A _ E
# Guess your letter: w
# Letter 'W' is not in the word
# E _ A _ _ _ A _ E
# Guess your letter: a
# E _ A _ _ _ A _ E
# Guess your letter: v
# E V A _ _ _ A _ E
# Guess your letter: q
# Letter 'Q' is not in the word
# E V A _ _ _ A _ E
# Guess your letter: w
# Letter 'W' is not in the word
# E V A _ _ _ A _ E
# Guess your letter: p
# E V A P _ _ A _ E
# Guess your letter: o
# E V A P O _ A _ E
# Guess your letter: r
# E V A P O R A _ E
# Guess your letter: t
# E V A P O R A T E
# You win!
