#Write a small Python program which read a text file. If the file doesn’t exist, 
# the program must print error message to the user and the program must exit with 
# code 1. Otherwise print the file content and continue program run normally.

import sys
import os

def main():
    print("Program starting.")

filename = input("Insert filename: ")

#Tiedostopolku
path_cwd = os.path.join(os.getcwd(), filename)

# Jos ei löydy, kokeillaan: sama kansio, jossa tämä .py-tiedosto on
path_script = os.path.join(os.path.dirname(__file__), filename)

if os.path.exists(path_cwd):
    full_path = path_cwd
elif os.path.exists(path_script):
    full_path = path_script
else:
    print("Error! File '{}' does not exist.".format(filename))
    sys.exit(1)

with open(full_path, "r", encoding="utf-8") as f:
    print("## {} ##".format(filename))
    for line in f:
        print(line.rstrip("\n"))
    print("## {} ##".format(filename))

print("Program ending.")

if __name__ == "__main__":
    main()