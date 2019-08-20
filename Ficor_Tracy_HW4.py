#########################################################
# Author: Tracy Ficor       BIFS617                     #
# Homework Assign 4                                     #
#########################################################
print("-------------Question 1--------------------")
import re

# create a function to help determine if matches are in result. 
def list_enquire(result):
    if not result:
        return 1
    else:
        return 0
# open the test file
dna = open("C:/Users/Tray-CSSD/Desktop/BIFS 617/Week 11/Test.txt")
# read in the contents
dna_content = dna.read().rstrip().upper()
matches = re.finditer(r"AT[AT]+", dna_content)
result = []
for m in matches:
    result.append(m.group())
    list_enquire(result)
if list_enquire(result):
    print("This file does not contain AT repeat(s)")
else:
    print("This file contains AT repeat(s)")

print("___________________________________________")
print("\n")
#### Question 2 ########
print("-------------Question 2--------------------")
print("\n")

# create a function to parse the embl records
def embl_parse():
    EMBLfile = open("C:/Users/Tray-CSSD/Desktop/BIFS 617/Week 11/EMBL_records.txt", "r+")

    EMBL = EMBLfile.readlines()
    for line in EMBL:
        line = line.rstrip()

        if re.search(r'ID\s\s', line) or re.search(r'DE\s\s', line) or re.search(r'SQ\s\s', line) or re.search(r'^\s\s\s\s\s', line):
            print(line)

def main():
    embl_parse()
main()
