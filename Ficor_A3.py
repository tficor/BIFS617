############################################################################
# Author: Tracy Ficor   BIFS617   Assignment 3                             #
############################################################################
# Question 1. Write a program to look for motifs/domains in sequence both  #
# of which are provided by the user.                                       #
# Question 2. Write a program that takes the data acquired for three       #
# tissue/organ                                                             #
# types and sends the data through 4 different functions to calculate      #
# the number of elements in each list, the average of each list, the       #
# maximum, and the minimum for each lists. Return information to main      #
# function and display results when main() is called.                      #
############################################################################

# Import regular expression and operating system for question 1
import os
import re

# Write a function to open and read a user's file return to main Question 1
def open_seq(found_file):
    user_seq_file = open(found_file)
    content_user_file = user_seq_file.read().rstrip("\n")
    return content_user_file

# Question 1 Write a function to take contents of user provided file and user motif
# to search for. Search for motif/domain and Return to main. 
def domain_motif(content_user_file, user_motif):
    user_motif = user_motif
    result = re.findall(user_motif, content_user_file)
    return result
# In main function, get user input and call functions
# print whether the motif/domain selected by user is
# in the protein sequence file. Question 1

# Question 2. lists for each tissue type with indentified enzyme activity.
    
brain = [65, 69, 70, 63, 70, 68]
heart = [102, 95, 98, 110]
lung = [112, 115, 113, 109, 95, 98, 100]
    
#Q2. Func1 Count the number of measurements
def counting(organ):
    tissue = 0
    for activity in organ:
        tissue = tissue + 1
    return tissue
#Q2. Func2 Find the average enzyme activity
def averaging(organ):
    #Add the list elements together and divide by count to find average
    counting(organ)
    num = 0
    for activity in organ:
        num += activity
    average = num/counting(organ)
    print("It's average enzyme activity is", average)
    
#Q2. Func3 Find the maximum value in the data set
def maximum(organ):
    organ.sort()
    lowest = 0
    for activity in organ:
        if activity > lowest:
            lowest = activity
    print("It's maximum value in the dataset is", activity)
    
#Q2. Func4 Find the minimum value in the data set
def minimum(organ):
    organ.sort(reverse=True)
    highest = 0
    for activity in organ:
        if activity < highest:
            highest = activity
    print("It's minimum value in the dataset is", activity)
    
# Initiate main function for retrieving information and passing through to
# created functions. 
def main():
    # get user input for their seq file and motif/domain to search
    user_seq = input('Please type in file name with extension: ')
    user_motif = input("Please input the domain/motif you would like to search: ")
    # get file path, open, and read in the file. 
    dir_path = os.path.dirname(os.path.realpath(user_seq))
    found_file = dir_path + '\\' + user_seq
    content_user_file = open_seq(found_file)
    #search for domain/motif using function domain_motif(arg1,arg2)
    results = domain_motif(content_user_file, user_motif)
    print('--------------------------------------------------------------')
    # Display if the motif was found in the sequence or not.
    
    #######################QUESTION 1 Output#######################
    
    if user_motif in results:
        print("The searched domain/motif", user_motif,"has been found in",user_seq)
    else:
        print("I'm sorry the domain/motif", user_motif,"has not been found in",user_seq)

    print('\n')

    #######################QUESTION 2 Output#######################

    print("Enzyme Activity information for Brain, Lung, and Heart")
    # When main() is called in the shell print out the information
    print("For brain there were", counting(brain), "measurements.")
    averaging(brain)
    maximum(brain)
    minimum(brain)
    print('\n')
    print("For heart there were", counting(heart), "measurements.")
    averaging(heart)
    maximum(heart)
    minimum(heart)
    print('\n')
    print("For lung there were", counting(lung), "measurements.")
    averaging(lung)
    maximum(lung)
    minimum(lung)
    return 
