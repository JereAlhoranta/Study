#Create a program that copies a text file by reading from a source file 
#and writing the content to a destination file. 
#Allow the user to specify the source and destination file names.

from pathlib import Path

def main() -> None:
    print("Program starting.")
    print("This program can copy a file.")

    source = input("Insert source filename: ")
    dest = input("Insert destination filename: ")

    base = Path(__file__).parent
    source_path = base / source
    dest_path = base / dest

    print(f"Reading file '{source}' content.")

    # Luo tiedosto
    try:
        with open(source_path, "r", encoding="utf-8") as src: #avaa tiedoston lukutilassa. 
            content = src.read() #src.read() lukee koko tiedoston sisällön merkkijonoksi
    except FileNotFoundError:
        print(f"ERROR: source file '{source}' not found.")
        print("Program ending.")
        return None

    print("File content ready in memory.")
    print(f"Writing content into file '{dest}'.")

    # Kirjoita kohdetiedostoon
    with open(dest_path, "w", encoding="utf-8") as dst: #avaa kohdetiedoston kirjoitustilassa
        dst.write(content) #dst.write(content) kirjoittaa sisällön sellaisenaan

    print("Copying operation complete.")
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()