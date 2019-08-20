aminos = ["Trp", "Arg", "Liu", "Ilu", "Asp"]
sum_index = 0
while aminos !=0:
    user_aa = input("Input Amino Acid you are looking for: ")
    lower_aa = user_aa.lower().capitalize()
    print("If you were looking for amino acid", lower_aa)
    if lower_aa in aminos:
        print("Amino Acid Found at position", (aminos.index(lower_aa)) + 1)
        aminos = 0
    else:
        print("Amino Acid NOT Found")
        aminos = 0
            
