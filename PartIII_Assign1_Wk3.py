################################################################################
# Author: Tracy Ficor       Date: 2/24/2019                                    #
# Regarding: Part III of Assignment 1                                          #
# Purpose: To read in Reflectin Gene from Cuttlefish Species from a text file  #
# and calculate the AT and GC content within that sequence and print out the   #
# results to DNA_Statistics.txt file.                                          #
################################################################################

# Open and read in the Reflectin Cuttlefish gene saved in text file from genebank
cuttle_gene = open("HE866979.1.txt")
cuttle_dna = cuttle_gene.read()

# Calculate the length of the cuttlefish gene
length_seq = len(cuttle_dna)

# Calculate the AT and GC content but calculating the number of A and T in the
# sequence, adding the individual count for A and T together, divid the sum of
# As and Ts by the length of the gene sequence and then multiply by 100 to obtain
# a floating percentage. Repeat steps to calculate the GC content. 

at_content = ((cuttle_dna.count('A') + cuttle_dna.count('T')) / length_seq) * 100
gc_content = ((cuttle_dna.count('G') + cuttle_dna.count('C')) / length_seq) * 100

# Answer for AT and GC content contains too many numbers past the decimal point and is
# not properly formated to be written out into statistics file. Convert the AT and GC
# content answers to only having 1 decimal point and convert to a string. 
rounded_at = str(round(at_content, 1))
rounded_gc = str(round(gc_content, 1))

# Open a new file named DNA_Statistics.txt and write AT and GC content following
# part III homework guidelines.  
cuttle_stats = open("DNA_Statistics.txt", "w")
cuttle_stats.write("The AT content of the DNA sequence given is: " + rounded_at + "%" + "\n")
cuttle_stats.write("The GC content of the DNA sequence given is: " + rounded_gc + "%")


# Close stats file. 
cuttle_stats.close()

