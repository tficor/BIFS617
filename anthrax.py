import re

anth = open("C:/Users/Tray-CSSD/Desktop/BIFS 617/Week 11/sequence.fasta")

header = []
seq = []
sequences = ''
for line in anth:
   if line[0] == ">":
      # converted header to upper case
      header.append(line[1:].strip().upper())
      if sequences != '':
         seq.append(sequences)

      sequences = ''
   else:
      # make sure seq is converted to upper
      line = line.upper()
      sequences += line.strip()

seq.append(sequences)

count = 0
for acc in header:
   acc_select = header[count]
   for name in acc_select:
      acc = re.findall(r"(\w+)", acc_select)
      acc = (acc[1] + "_" + acc[2])
   count = count + 1
   print("Accession: ", acc)
   print("Sequence: ", seq[count-1], "\n")

anth.close()
