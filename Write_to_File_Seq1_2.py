seqfile = open("out.txt" , "w")
# Open the created seq1.txt file from computer
seq_1 = open("seq1.txt")
# Read contents of the file into python
seq_1_content = seq_1.read()
# Remove the newline from the end of file contents
# seq_1_strip = seq_1_content.rstrip("\n")
seqfile.write(seq_1_content + '\n')
# Open the created seq2.txt file from computer
seq_2 = open("seq2.txt")
# Read contents of the file into python
seq_2_content = seq_2.read()
# Remove the newline from the end of file contents
# seq_2_strip = seq_2_content.rstrip("\n")
seqfile.write(seq_2_content)

seqfile.close()
seq_1.close()
seq_2.close()
