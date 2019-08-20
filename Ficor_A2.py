##########################################################################################
# Author: Tracy Ficor       Course: BIFS617                                              #
# Assignment 2 - Complete the homework assignment in one python program. Comments        #
# indicate what is required to answer each question from the assignment.                 #
##########################################################################################


# PART 1A) Define array that contains the amino acids in three letter 
# notation and print in one line.
polypep = ["Phe", "Val", "Asn", "Gln", "His", "Leu", "Cys", "Gly", "Ser"]
print("PART 1A) The stored polypeptide sequence is: \n", polypep, "\n")

# PART 1B) Calculate the # of amino acides in the polypeptide and print
polypep_len = len(polypep)
print("PART 1B) The Length of the Stored Polypeptide is:", polypep_len, "\n")

# PART 1C) Add "His" to end of the polypeptide and print result of add
polypep.append("His")
print("PART 1C) The amino acid 'His' was added to the stored polypeptide and is now: \n", polypep, "\n")

# PART 1D) User input number corresponds to amino acid position in polypeptide
# chain and print the amino acid. 
user_num = int(input("PART 1D) Enter a number between 1 and 10: "))
user_num = user_num - 1
print("The polypeptide at this position is", polypep[user_num],"\n")

# PART 1E) Create an inversion
user_num1 = int(input("PART 1E) Enter first number between 1 and 10: "))
user_num2 = int(input("PART 1E) Enter second number between 1 and 10: "))
user_num1 = user_num1 - 1
print("The polypeptide without inversion is: \n", polypep, "\n")
polypep[user_num1 : user_num2] = reversed(polypep[user_num1 : user_num2])
print("The inverted polypeptide chain given the numbers provided is: \n", polypep, "\n")

# Question 2) store a given amino acid sequence into an array hidden from the 
# user, have the program prompt user to provide a number which will correspond to 
# a potential position of an amino acid in the array. 

# Store the amino acid
amino_array = ["Trp", "Arg", "Liu", "Ilu", "Asp"]

# Prompt user to select a potential index within the array
user_index = int(input("QUESTION 2) Please select a number between and including 1 to 5: "))
user_index = user_index - 1

# Set boundary for user input so that program errors if number user inputs
# is out of range for the array.
if user_index >= 0 and user_index < 5:
    print("The selected amino acid at the position provided is ", amino_array[user_index],"\n")
else:
    print("I'm sorry that is not a valid index for this array. \n")

# Question 3) Write a program to store a given DNA sequence as an array
# and not as a string. Perform various manipulations to the array.

# Store the DNA sequence into an array.
my_seq = ["C", "C", "G", "T", "A", "A", "C", "G", "C"]

# Q3 PART A: Add a T to the End of the array, then print the array.
my_seq.append("T")
print("PART 3A) The stored sequence is \n", my_seq)
# Q3 PART B: Remove the 1st element of the array and print it.
my_seq.remove("C")
print("PART 3B) If we revmove the first base the new sequence is \n", my_seq)
# Q3 PART C: Add T to the beginning of the array and print it.
my_seq.insert(0, "T")
print("PART 3C) Adding the base 'T' to the sequence changes the sequence to \n", my_seq)
# Q3 PART D: Make your output neat and readable. 







