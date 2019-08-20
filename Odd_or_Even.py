######################################################################
# Author: Tracy Ficor   Course: BIFS617     Week#5 Discussion Board  #
# Purpose: To create a program that prompts user for a number to     #
# test to see if their number is odd or even.                        #
######################################################################

# Ask the user to input a number, convert round number to nearest
# integer. 
user_num = float(input("Please input your number: "))
conv_num = int(round(user_num))

# Verify with the user the number that they inputted and inform them
# that you converted the number to make sure it is an integer. 
print("You inputted ", user_num,"\n")
print("To be sure it's a whole number we've rounded your input to the nearest integer which is", conv_num,"\n")

# Determine if the converted integer is even or odd. 
if conv_num % 2 == 0:
    print("Your converted number is", conv_num, "which is even.")
else:
    print("Your converted number is", conv_num, "which is odd.")
