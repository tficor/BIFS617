###############################################
# Objective: Open and read files into python. #
# Author: Tracy Ficor                         #
###############################################

# Open the created seq1.txt file from computer
seq_1 = open("seq1.txt")
# Read contents of the file into python
seq_1_content = seq_1.read()
# Remove the newline from the end of file contents
seq_1_strip = seq_1_content.rstrip("\n")
# Calculate the length of bp in sequence 1. 
seq_1_len = len(seq_1_strip)
# Open the created seq2.txt file from computer
seq_2 = open("seq2.txt")
# Read contents of the file into python
seq_2_content = seq_2.read()
# Remove the newline from the end of file contents
seq_2_strip = seq_2_content.rstrip("\n")
# Calculate the length of bp in sequence 1. 
seq_2_len = len(seq_2_strip)
# Display Sequence 1 and 2 and their bp lengths. 
print("Sequence 1 is:" , seq_1_strip, "with length, " , str(seq_1_len))
print("Sequence 2 is:" , seq_2_strip, "with length, " , str(seq_2_len))

seq_1.close()
seq_2.close()
