################################################################
# Author: Tracy Ficor   Date: 2/24/2019                        #
# Purpose: is to write a program that converts a given DNA     #
# Sequence to RNA and to display both Sequences for comparison.#
################################################################

# Ask the user for their DNA sequence for conversion. User
# dna to be stored in variable.
user_dna = input("Please input your DNA sequence: ")

print("The DNA sequence you provided was: ", user_dna)
print("The converted DNA sequence to RNA is: ", user_dna.replace("T", "U"))


