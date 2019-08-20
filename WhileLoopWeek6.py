######################################################################
# Author: Tracy Ficor   Course: BIFS617     Week#5 Discussion Board  #
# Purpose: To use a while loop to develop a simple name guessing game#
# asking user to input what their guess is and returning a response  #
# on whether they are right and giving them additional chances if not#
######################################################################

def guessname():
# Store my name in a variable
# set guess_lower to zero to loop
    my_name = "tracy"
    guess_lower = 0
# Ask the user to take a guess. 
    while my_name != guess_lower:
        user_guess = input("Take a stab at guessing my name: ")
        # put guess in lower case
        guess_lower = user_guess.lower()
        # report whether they are right or not. 
        if guess_lower == "tracy":
            print("Well done, good guess work!")
        else:
            print("How about another try? ")

