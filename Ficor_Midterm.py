###############################################################################
# Author: Tracy Ficor       Course: BIFS617     Date: 3/17/2019               #
# Purpose: Midterm for BIFS617.                                               #
###############################################################################

# Question 1. Write out portions of the gene to files that indicate non-coding
# portions and coding portions.

# Print out details of question 1 so its indicating that something is happening
print("\n")
print("Question 1: Write out portions of the genomic DNA to their own file,")
print("introns and exons are written out into their own files. \n")
# Open genomic_dna file on computer, read and strip of newline characters
gene_file = open("C:/Users/Tray-CSSD/Desktop/BIFS 617/Week 6/genomic_dna.txt")
gene_dna = gene_file.read().rstrip("\n")

# based on information provided regarding the known intron and exon positions
# in the sequence data separate the sequence into introns and exons. 
gene_len = len(gene_dna)
exon1 = gene_dna[0:63]
intron1 = gene_dna[63:90]
exon2 = gene_dna[90:]

# Open a new non-coding file and write introns into the non-coding file
# Open a new coding file and write exons into the coding file
intron = open("non-coding.txt", "w")
intron.write("Intron: " + intron1)
exon = open("coding.txt", "w")
exon.write("Exon 1: " + exon1 + "\n")
exon.write("Exon 2: " + exon2 + "\n")
# Close the files
intron.close()
exon.close()
print("-"*100, "\n")

print("Question 2. Calcuating the percent of sequence that is coding and non-coding")
# find the length of exons and intron from previous question and determine percentages
len_exon1 = len(exon1)
len_exon2 = len(exon2)
len_intron = len(intron1)
# print out the results showing percent coding and non-coding
print("Percent of sequence that is coding: ", round(((len_exon1 + len_exon2)/gene_len)*100), "%", sep = "")
print("Percent of Sequence that is non-coding: ", round((len_intron/gene_len)*100),"%", "\n", sep = "")
      
gene_file.close()
print("-"*100, "\n")

# Question 3
print("Question 3. Read in provided files to manipulate sequences into 3 separate fasta files.")
print("Remove special characters and put the sequence in all caps. \n")

# Opent the accession numbers file and sequences file, read in and strip
acc_file = open("C:/Users/Tray-CSSD/Desktop/BIFS 617/Week 6/AccessionNumbers.txt")
acc_name = acc_file.read().rstrip("\n").split()
seq_file = open("C:/Users/Tray-CSSD/Desktop/BIFS 617/Week 6/sequences.txt")
seqs = seq_file.read().upper().replace("-", "").rstrip("\n").split()

# Combine the accessions with sequences
acc1 = ">" + acc_name[0] + "\n" + seqs[0]
acc2 = ">" + acc_name[1] + "\n" + seqs[1]
acc3 = ">" + acc_name[2] + "\n" + seqs[2]

# Write out info for each accession into their own fasta file
acc1_seq = open("ABCD1234.fasta", "w")
acc1_seq.write(acc1)
acc2_seq = open("GFRT7890.fasta", "w")
acc2_seq.write(acc2)
acc3_seq = open("HJIS5630.fasta", "w")
acc3_seq.write(acc3)

# Close the files. 
acc1_seq.close()
acc2_seq.close()
acc3_seq.close()
print("-"*100, "\n")


# Question 4 Reverse Complement DNA
print("Question 4. Write a program the check if two provided sequences are")
print("reverse complement of one another.")
# Have user input the sequences
seq1 = input("Please input your first sequence: ")
seq2 = input("Please input your second sequence: ")
# put them all in the same upper case format
upper_seq1 = list(seq1.upper())
upper_seq2 = list(seq2.upper())
# create a dictionary to change to complement
complement = {"A":"C", "C":"A", "T":"G", "G":"T"}
upper_seq1 = list("".join(complement[base]for base in upper_seq1))

# print out the sequences
print("".join(upper_seq1))
print("".join(upper_seq2))

# Check to see if the second sequence is the reverse complement of first sequence
if upper_seq2 == upper_seq1:
    print("Yes, Sequence 2 is the reverse complement of Sequence 1! \n")
else:
    print("The sequences provided are not the reverse complement of each other. \n")
print("-"*100, "\n")

# Question 5
print("Question 5. Write a program to read a file, and then print its lines ")
print("in reverse order, the last line first. You can use the sequence.txt file")
print("(attached) to test your program with. \n")

#Read sequences.txt file into python and print lines in reverse order. 
# open and read in sequences
seq_file = open("C:/Users/Tray-CSSD/Desktop/BIFS 617/Week 6/sequences.txt")
seq_dna = seq_file.read()

# split seq_dna at newline character
seq_lines = seq_dna.split('\n')

# Print lines in reverse order with last line first and so on. 
print(seq_lines[-1], "\n")
print(seq_lines[-2], "\n")
print(seq_lines[-3], "\n")
print("-"*100, "\n")

# Question 6.
print("Question 6. Size population prediction program.\n")
# Ask user for # of orgs, avg population increase per day, and how many days
# the organisms are allowed to divide for.

Start_num_orgs = int(input("Please enter the number of starting organisms: "))
# define days, find the decimal average, and set start_num_orgs equal to population
while Start_num_orgs < 2:
    Start_num_orgs = int(input("That is insufficient - a positive number greater than or equal to 2 is required for starting number of organisms: " ))

avg_pop_inc_perday = float(input("Please input the percent of average population growth for organisms: "))
while avg_pop_inc_perday < 0:
    print("I'm sorry, a positive percentage is required for calculation.")
    avg_pop_inc_perday = float(input("Please input a positive percentage: "))
        
days_dividing = int(input("Please input the number of days the organisms are allowed to multiply: "))
while days_dividing < 1: 
    days_dividing = int(input("Please input a number 1 or greater for number of days: "))

print("\n")
day = 0
decimal_avg = avg_pop_inc_perday/100
population = Start_num_orgs
# print out information into a table form
print("Day", "\t"*1, "Organisms")
print("-"*18)
# show number of organisms after each day allowed to divide
for day in range(1, days_dividing + 1):
    print(day, "\t"*1, float(population))
    population = population + (population*decimal_avg)
print("\n")
print("-"*100, "\n")

    
# Question 7.
print("Question 7. User input lines to store in array until user quits.")
print("program prints out sorted lines.")

# declare an empty list and set stop = "quit"
storage = []
stop = "quit"
print("Please begin typing in your data.")
print("When done wanting to store input type the word quit when prompted.\n")

# Obtain user input and store in the storage array, sort that array after storing
# Ask user if they want to quit or press no to continue. 
while True:
    to_be_stored = input("Please type your input you would like stored: ")
    storage.append(to_be_stored)
    storage.sort()
    To_stop = input("Type QUIT to stop or NO to continue: ")
    loweredstop = To_stop.lower()
    print("\n")
    if loweredstop == "quit":
        break
# After user quits display all of the inputs that were sorted and stored.    
print("The following inputs were sorted and stored: ", storage, "\n")

print("-"*100, "\n")

# Question 8.
print("Question 8. Modify question 7 to tell user how many lines have been entered")
print("and then print only lines 2, 3, and 4.")

# declare an empty list and set stop = "quit"
storage = []
stop = "quit"

# Obtain user input and store in the storage array, sort that array after storing
# Ask user if they want to quit or press no to continue. 
print("To stop storing numbers type quit when prompted.\n")
while True:
    to_be_stored = input("Please type your input: ")
    storage.append(to_be_stored)
    storage.sort()
    len_storage = len(storage)
    To_stop = input("Type quit to stop or no to continue: ")
    loweredstop = To_stop.lower()
    print("\n")
    if loweredstop == "quit":
        break
# determine if the length of the storage is sufficient and display what is available. 
if len_storage == 1:
    print("I'm sorry there are no lines stored at 2, 3, or 4. \n")
while len_storage != 1:
    if len_storage >= 4:
        print(len_storage, "lines were sorted and stored.")
        print("The lines at 2, 3, and 4 are: ", storage[1], ", ",storage[2],", and ", storage[3], "\n", sep = "")
        len_storage = 1
    elif len_storage is 3:
        print("There is no line at 4 however, lines at 2 and 3 are: ", storage[1], "and ",storage[2], "\n")
        len_storage = 1
    else: 
        print("There are no lines at 3 or 4 however, line at 2 is: ", storage[1], "\n")
        len_storage = 1

print("-"*100, "\n")

#Question 9.
print("Question 9. Ask the user for a list of sequence lengths, separated by whitespace ")
print("Store the sequence lengths as one string in a variable, then Split that string and ")
print("create an array from it use a for loop to get the sum of all sequence lengths, and ")
print("print the average. \n")

# Ask user for sequence lengths with space
print("Example of Various Sequence lengths with space: 100 123 45")
string_sequence = input("Please type various sequences lengths with a space in between: ")
print("\n")
# split the string and use for loop to get sum of all sequences
split_string = string_sequence.split(" ")
total = 0
count = 0
for num in split_string:
    total += int(num)
    count = count + 1
# print the average of the summed sequence lengths. 
print("The average of the summed sequences lengths is:", round((total/count),1), "\n")
print("-"*100, "\n")

# Question 10. Percent Calories from fat.
print("Question 10. Determining Calories from fat, total calories, and percent calories from fat.")  

# create a loop to input the number of calories if number of calories is lower
# than calories from fat indicate the user to reinput a higher total calories. 

fat_cals = 1
cals = 0
while cals < fat_cals:
    cals = int(input("Please input the number of calories: "))
    grams_fat = int(input("Please input the number of grams of fat: "))
    print("\n")
    fat_cals = grams_fat*9
    percent_cals_fat = round((fat_cals/cals)*100, 1)
    if cals < fat_cals:
        print("Calories from fat cannot be greater than the total number of calories in food item.")
    else:
        print("Calories from fat: ", fat_cals, "\n")
        print("Total calories: ", cals, "\n")
        print("Percentage of calories from fat: ", percent_cals_fat, "%", sep = "")
# Display low in fat if less than 30.0
        if percent_cals_fat < 30.0:
            print("Food is low in fat. \n")
print("-"*100, "\n")

print("The end! \n")





