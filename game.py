"""The script that runs the game of hangman"""


# Add any necessary imports up here
from hangman import *
from settings import *


def main():
    """The main code for this script. Runs the hangman game."""
    # Write your code as detailed in the assignment handout here
    past_guesses = []
    N = 0
    result = True
    while result:
        print('Word: ' + obfuscated_word(WORD, past_guesses))
        print('Number of bad guesses: ' + str(N) + ' out of ' +
              str(MAX_NUM_ERRORS))
        print('Guesses: ' + format_guesses(past_guesses))
        guess = get_guess(past_guesses)
        if is_guess_good(WORD, guess):
            print(guess + ' is in the word' + "\n")
        else:
            print(guess + " is not in the word" + "\n")
            N += 1
        if is_word_guessed(WORD, past_guesses) or N == 5:
            result = False

    if is_word_guessed(WORD, past_guesses):
        print('Congratulations! It took you ' + str(N) +
              ' incorrect guesses to guess the word')
    else:
        print("Sorry, you failed to guess the word after " +
              str(MAX_NUM_ERRORS) + " incorrect guesses")

    print('  The word was ' + WORD)

if __name__ == '__main__':
    main()  # Don't modify this part!
