#------------------------------------------------------------------#
# Author: Tracy Ficor       Final for BIFS 617     Date: 4/28/2019 #
#------------------------------------------------------------------#

import os, re

print('############################ QUESTION 1 ############################')
# CCCCATAGAGATAGAGATAGAGAACCCCGCGCGCTCGCATGGGG
# CCCCATAGAGATAGAGAtagAGAAcccCGCGCGCTCGCATGGGG
dna = (input("Please input your sequence: ")).upper()
# Function to search for ATG 
def upstream(seq):
    #in case RNA was inputted substitute U for T in the evaluated seq. 
    m =re.sub("U", "T", dna)
    # Search for the start codon
    m = re.search(r'ATG', dna)
    # obtain the start position and count upstream 20 positions.
    if m:
        pos_start = int(str(m.start()))
        upstream = (pos_start) - 20
        up = 1
        # If the start codon was identified let user know and display the 20
        # bases prior to start codon
        while up > 0:
            print("The start codon was identified,")
            print("20 bases prior to start codon is: ", dna[upstream:pos_start])
            up = 0
    # If start codon was not found then inform the user there was no start codon
    # identified in the given sequence.
    else:
        print("Start codon was not identified in the given sequence.")
    return

def main():
    # call function and print result
    upstream(dna)
    print('\n')
main()

print('############################ QUESTION 2 ##################################')

def main():
    #open the file that the user inputs
    file = open(input("Please input your txt file: "))
    #call the dictate function to read the file
    fn = dictate(file)
    #print the output of the dictate function
    print(fn)

def dictate(file):
    file_info = file.read().splitlines()

    keys = []
    values = []
    index = 0
    for elem in file_info:
        if index % 2 == 0:
            keys.append(elem)
        else:
            values.append(elem)
        index += 1
        
    diction = dict(zip(keys, values))
    return diction
    
main()
print('\n')

print('############################## QUESTION 3 ##################################')
import re

blast_x = open(input("Please input your .txt file: "))

blastinfo = blast_x.read().rstrip()
# Print Table headers with spacing. 
print("Query",'\t'*2, "BestHit",'\t'*10, "E-Value",'\t', "Identities")
print("--"*70)

# Create lists to parse out all of the required information for the table. 
query = []
for line in re.findall(r"Contig_\d\d\d", blastinfo):
    query.append(line)


best = []
for line in re.findall(r">.*", blastinfo):
    best.append(line)


evalue = []
for line in re.findall(r"[123]e-\d\d\d", blastinfo):
    evalue.append(line)
    evalue = list(dict.fromkeys(evalue))

identity = []
for line in re.findall(r"(?<= Identities = ).*?(?=,)", blastinfo):
    identity.append(line)

# create a function to formulate a table
def data_table():
    
    for best_val, q_val, id_val, e_val in zip(best, query, identity, evalue):
        print(q_val,'\t', best_val,'\n','\t'*13, e_val, '\t', id_val, '\n')
     
    return

# Call table in main
def main():
    table = data_table()
    print('\n')
main()

print('#################### QUESTION 4 ################################', '\n')
import re
comment = open(input("Please input your .fna formated file: "))

readcomments = comment.read().rstrip()

def fna_parse():
    # Obtain values for mid2 using regex and store in list
    mid2 = []
    for line in re.findall(r"MID2", readcomments):
        mid2.append(line)

    # Obtain values for contigs using regex and store in list
    contig = []
    for line in re.findall(r"contig\d*", readcomments):
        contig.append(line)

    # Obtain values for length of contig using regex and store in list
    LenSeq = []
    for line in re.findall(r"(?<= length=)\d*", readcomments):
        LenSeq.append(line)

    # Obtain values for # of reads using regex and store in list
    numread = []
    for line in re.findall(r"(?<= numreads=)\d*", readcomments):
        numread.append(line)
    
    return mid2, contig, LenSeq, numread

def main():
    #Call function fna_parse
    mid2, contig, LenSeq, numread = fna_parse()
    #Parse out the result of fna_parse
    for Mid, Con, LS, NR in zip(mid2, contig, LenSeq, numread):
        print(Mid, Con, LS,'\t', NR)
    print('\n')
main()

print('############################### QUESTION 5 #############################################', '\n')

genome = open(input("Please input the .txt file you would like to evaluate for codon frequency: "))
# genome.txt
genseq = genome.read().rstrip()
# list of possible codons
codons = ['AAA', 'AAC', 'AAG', 'AAT', 'ACA', 'ACC', 'ACG', 'ACT', 'AGA', 'AGC', 'AGG', 'AGT',
          'ATA', 'ATC', 'ATG', 'ATT', 'CAA', 'CAC', 'CAG', 'CAT', 'CCA', 'CCC', 'CCG', 'CCT',
          'CGA', 'CGC', 'CGG', 'CGT', 'CTA', 'CTC', 'CTG', 'CTT', 'GAA', 'GAC', 'GAG', 'GAT',
          'GCA', 'GCC', 'GCG', 'GCT', 'GGA', 'GGC', 'GGG', 'GGT', 'GTA', 'GTC', 'GTG', 'GTT',
          'TAA', 'TAC', 'TAG', 'TAT', 'TCA', 'TCC', 'TCG', 'TCT', 'TCT', 'TGA', 'TGC', 'TGG',
          'TTA', 'TTC', 'TTG', 'TTT']

# Create lists in order to obtain counts for each codon and hole calculated codon frequency.

counts = []
codonFreq = []
# Obtain codon counts and append counts list
for codon in codons:
    count = genseq.count(codon)
    counts.append(count)
# Calculate the total codons to calculate codon frequency
total = sum(counts)

#Calculate codon frequence for each codon in codons. 
for count in counts:
    codonFreq.append(round(((count/total)*100), 2))

# Create a dictionary by zipping the codons and codonFreq list and output dictionary. 
codon_dict = dict(zip(codons, codonFreq))
print(codon_dict)
print('\n')
print('\n')

print("################################# QUESTION 6 ###########################################", '\n')

#parse staden_link.txt and store information in a dictionary

import re
# open and create dictionary from the staden file. 
def staden_parser():
    staden = open("Staden_link.txt").read().splitlines()
    enzym_dict = {}
    for line in staden:
        if re.search("^\s", line) or re.search("^Rich", line) or re.search("^REBASE", line):
            continue
        name = line.split("/")
        site = name.pop()
        site = name.pop()
        site = name[1:]
        # Tried to convert any non-ACTG character to ACTG and remove the cut character
        site = [s.replace(r"[^ACTG]", "[ACTG]") for s in site]
        site = [s.replace("N", "[ACTG]") for s in site]
        site = [s.replace("'", "") for s in site]
        for elem in site:
            enzym_dict[name[0]] = site
    return enzym_dict

dictionary = staden_parser()
print(dictionary)

# output the restriction enzymes and the cut sites. 

seqs = open(input("Please input your fasta file: "))

dnaseqs = seqs.read().rstrip("\n")

# Use a regex to find enzymes that match segments of the sequences
# contained in the dictionary
#all_cuts = [0] 
#for match in re.finditer("[AGCT]", seqs): 
#    all_cuts.append(match.start() + 3) 
#all_cuts.append(len(seqs)) 
#print(all_cuts)

# Use a modified version of the code below to attempt to find cut
# positions so that they can be displayed. 
#for i in range(1,len(all_cuts)): 
#    this_cut_position = all_cuts[i] 
#    previous_cut_position = all_cuts[i-1] 
#    fragment_size = this_cut_position - previous_cut_position 
#    print("one fragment size is " + str(fragment_size))

# this will all need to be modified so that it can loop through
# for each sequence contained in the fasta file provided. 

# Display enzyme names and cut positions in the form of a table
# output will appear similar to this

print("Seq 1 Results")
print("Enzyme Name", "\t", "Cut Positions")
print("-----------------------------------------")
print("EcoR1", "\t", "30, 45, 65")
print("ARGII", "\t", "12,18,89")

print("Seq 2 Results")
