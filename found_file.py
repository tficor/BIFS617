import os

def valid_file():

    i = 0
    
    while i < 6:
        file = input("Please enter a filename: ")
        if os.path.exists(file) == False:
            i = i + 1
            print("Not a valid filename.\n")
            if i >= 5:
                print("You did not enter a valid file name.")
                print("Please try again. \n")
                i = 0
        if os.path.exists(file) == True:
            print("File found, Thanks!")
            i = 6

def main():
    valid_file()

main()
        
