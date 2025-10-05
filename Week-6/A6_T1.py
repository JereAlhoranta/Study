#Create a program that can read a text file and then print the file content. 
# User must be able to specify the file name. 
# Decorate the beginning and the end of the file with a decorative line.

#Decorative lines

    #### START "{filename}" ####
    #### END "{filename}" ####

from pathlib import Path

def main() -> None:
    print("Program starting.")
    print("This program can read a file.")

    filename = input("Insert filename: ")

    script_folder = Path(__file__).parent
    file_path = script_folder / filename

    print(f'#### START "{filename}" ####')

    try:
        with open(file_path, "r", encoding="utf-8") as f: #avaa tiedoston lukutilassa ("r")
            content = f.read() #content = f.read()
    #read() lukee koko tiedoston sisällön yhdeksi merkkijonoksi

            print(content, end="")
    except FileNotFoundError:
        print(f'ERROR: File "{filename}" not found.')

    print(f'\n#### END "{filename}" ####')
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()          