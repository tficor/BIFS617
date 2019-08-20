#############################################################################
# Author: Tracy Ficor   Course: BIFS617     Date: 2/28/2019                 #
# Purpose: To ask the user for 5 individual numbers and have them stored    #
# into their own variable. These numbers will be summed and then averaged.  #
# The sum of the users numbers and its average will be printed out to user. #
#############################################################################

# Ask and obtain the users 5 numbers that will be stored in their own variable. 
num_1 = int(input("Please enter your first number: "))
num_2 = int(input("Please enter your second number: "))
num_3 = int(input("Please enter your third number: "))
num_4 = int(input("Please enter your fourth number: "))
num_5 = int(input("Please enter your fifth number: "))

# Add up the 5 numbers provided to obtain the sum of the 5 numbers. 
num_sum = num_1 + num_2 + num_3 + num_4 + num_5

# To average divide the total sum of the added numbers by 5. 
avg_sum = num_sum / 5

# Print out the sum and the average for the user to see. 
print("The sum of your inputed numbers is ", num_sum, "and their average is ", avg_sum)


