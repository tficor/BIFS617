#############################################################################
# Author: Tracy Ficor   Course: BIFS617     Date: 2/28/2019                 #
# Purpose: To create a program that stores the following list: peroxidase,  #
# gene, protein, oxidase, and hemoglobin as provided into list variable.    #
# It will then need to print the 3rd element in the array followed by 2     #
# blank empty lines before printing the 5th element in the array.           #
#############################################################################

# Store the provided list in an array
gene_array = ('peroxidase', 'gene', 'protein', 'oxidase', 'hemoglobin')

# Print the 3rd element in the array index 2
# Print out 2 blank/empty lines before printing the next requested element
# Print the 5th element in the array index 4
print(gene_array[2], "\n"*3, gene_array[4], "\n", sep = "")


print("The length of the arrays is: ", len(gene_array))
print("The array contains the following words: ", gene_array)
