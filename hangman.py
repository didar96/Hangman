"""Some functions useful for the hangman game.
Starter code by David Szeto. Implementation by the CSCA20 student.
"""


# Add any necessary imports up here


def obfuscated_word(word, past_guesses):
    """ Returns a str with the correct guesses shown

    Given the string word and list past_guesses, return a string where the
    guesses are shown and the non-guessed characters are replaced with an
    underscore. For example, obfuscated_word('hello', ['e', 'o'])
    should return the str '_e__o'

    Args:
        word: a string
        past_guesses: a list of strings

    Returns:
        a new string with guesses and non-guesses
    """

    new_string = ''
    for element in word:
        if element in past_guesses:
            new_string += element
        else:
            new_string += '_'
    return new_string


def get_guess(past_guesses):
    """Returns the guess made by user

   Ask the user to make a guess and if the guess is not one alphabetic
   character or was already in past_guesses, then a warning will be
   displayed and another opportunity to guess will be given. This step will be
   repeated until a correct guess is made. The correct guess will then be
   appended to past_guesses.

   Args:
      past_guesses: a list of strings

   Returns:
       A string: the correct guess made
    """
    result = True
    while result:
        new_guess = input("Guess a Letter: ")
        new_guess = new_guess.lower()
        if (len(new_guess) == 1 and new_guess not in past_guesses and
                new_guess.isalpha()):
            result = False
        else:
            print('You need to enter one alphabetic character which you' +
                  ' haven\'t already guessed. Try again')
    past_guesses.append(new_guess)
    return new_guess


def format_guesses(past_guesses):
    """Returns a string of the past_guesses.

    For example, format_guesses(['x', 'y', 'z']) should return the str 'x y z'

    Args:
      past_guesses: a list of strings

    Returns:
       A string: of past_guesses
    """
    return " ".join(past_guesses)


def is_guess_good(word, guess):
    """Returns whether guess is in the word

    For example, is_guess_good('hello', 'e') should return True while
    is_guess_good('hello', 'p') should return False.

    Args:
      word: a string
      guess: a string

    Returns:
       bool: True if guess is in word, else returns False
    """
    return guess in word


def is_word_guessed(word, past_guesses):
    """Returns whether the word is guessed or not

    The function will return True if the word is fully guessed, otherwise, will
    return false. For example, is_word_guessed('hello',['h', 'e', 'a', 'o',
    'l']) should return True while is_word_guessed('hello', ['e', 't', 'a'])
    should return False.

    Args:
        word: a string
        past_guesses: a list of strings

    Returns:
        bool: True if word was guessed else false
    """
    result = True
    for element in word:
        if element not in past_guesses:
            result = False
    return result


if __name__ == '__main__':
    # If you'd like to write testing code for this assignment, you may do so
    # here. You may also include doctests if you feel they will give you better
    # testing.
    pass
