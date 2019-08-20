#############################################################################
# Author: Tracy Ficor   Date: 3/14/2019 - BIFS617                           #
# Purpose: Using a for loop, request 5 numbers from user to be summed and   #
# and averaged. Display their sum and average to the user.                  #
#############################################################################

# Define range and sum
sum_range = 5
sum1 = 0
print("You will be asked to input 5 numbers to be summed and averaged.\n")
# Have user input 5 numbers indicated in the range and then use to calculate
# the sum of all of the numbers.
for x in range(sum_range):
    user_num = float(input("Select your number: "))
    sum1 = sum1 + user_num
# Divide the sum of the numbers by 5 to obtain the average of the 5 numbers.
# Print the sum of the five numbers and their average. Convert average to str.
average = sum1/sum_range
print("The sum is: ", str(round(sum1, 1)),"And Average: ", str(round(average, 1)))
print("Sum and Average are rounded to the nearest tenth.")
