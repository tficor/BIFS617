######################################################################
# Author: Tracy Ficor   Course: BIFS617     Week#5 Discussion Board  #
# Purpose: To create a single guessing test for a user in order to   #
# guess my name.                                                     #
######################################################################

# Store my name in a variable
my_name = "tracy"

# Ask the user to take a single guessing my name
user_guess = input("Take a stab at guessing my name: ")

# Convert the string to make sure it lower case so the name would match
# my name string held in variable my_name. 
guess_lower = user_guess.lower()

# Tell user if they correctly guessed my name or not. 
if guess_lower == "tracy":
    print("Well done, good guess work!")
else:
    print("Try again next time!")
