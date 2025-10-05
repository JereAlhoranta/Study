#Create a program that can write a text file. 
# Prompt the user to insert first name and last name. 
# Then prompt the file name for the write operation. 
# Finally write a text file with first name on the first row and last name 
# on the second row. 
# Ensure that the text file ends in a empty row. Finally exit the program cleanly.

def main() -> None:
    print("Program starting.")

    first = input("Insert First name: ")
    last = input("Insert last name: ")
    filename = input("Insert filename: ")

    # Kirjoitetaan tiedostoon
    with open(filename, "w", encoding="utf-8") as f: #Avaa tiedoston kirjoitustilassa ("w")
        f.write(first + "\n")
        f.write(last + "\n")
        f.write("\n")  # tyhjä rivi loppuun

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()