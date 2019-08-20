import re

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
