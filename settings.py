"""Settings for the hangman game."""


# Modify these settings at your will in order to test your game

# WORD is the word in question we'll be using for our game of hangman
WORD = 'tetrachlorodibenzoparadioxin'
# Feel free to have a friend enter a new word without showing you, so that you
# can play the game yourself without knowing the word in advance.

# If the user makes more than MAX_NUM_ERRORS number of incorrect guesses, they
# lose the game.
MAX_NUM_ERRORS = 5

# Don't touch these assertions!
assert WORD.isalpha()  # Make sure WORD is alphabetic-only and lower case
assert WORD.islower()
assert MAX_NUM_ERRORS >= 1  # Make sure MAX_NUM_ERRORS is positive