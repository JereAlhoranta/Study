#Create a Python program which is able to analyse names listed in a text file 
# (See dataset files):

#Analyse and specify following aspects from the file:

    #1. The amount of names
    #2. Shortest name
    #3. Longest name
    #4. Average name length.

#Let the user specify the filename for the analysis. 
# Program reads the file and prints the results from the analysis. 
# Values must be presented like shown in the example program runs. 
# Average name length must be presented in 2 decimal precision. 
# Use Format Specification Mini-Language to achieving the required precision for the 
# data presentation.

#Note! Given text files may contain empty rows and the program must be able to 
# skip them if present.

#Other tips:

    #Read text file line-by-line.
    #Pay attention to the reading process (newline characters).
    #Names can be stored into a single string variable.
        #Consider separating names with a semicolon ;
            #John;Doe;Jane
    #Report can be stored into one string variable.
    #Format Specification Mini-Language.
        #E.g., "Value in 2 decimal precision {:.2f}".format(3.555)

from pathlib import Path

def main() -> None:
    print("Program starting.")
    print("This program analyses a list of names from a file.")

    filename = input("Insert filename to read: ")

    print(f'Reading names from "{filename}".')

    base = Path(__file__).parent
    file_path = base / filename

    # Luetaan nimet listaan
    names = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            name = line.strip() #strip() poistaa rivinvaihdon \n ja välilyönnit
            if name != "":          # ohitetaan tyhjät rivit
                names.append(name)

    print("Analysing names...")

    # Jos ei ole nimiä, asetetaan nollat
    if not names:
        count = 0
        shortest = 0
        longest = 0
        average = 0.0
    else: #pituudet
        lengths = [len(n) for n in names]
        count = len(names)
        shortest = min(lengths)
        longest = max(lengths)
        average = sum(lengths) / count

    print("Analysis complete!")

    #tulostus
    print("#### REPORT BEGIN ####")
    print(f"Name count - {count}") #kuinka paljon
    print(f"Shortest name - {shortest} chars") #Lyhyin nimi
    print(f"Longest name - {longest} chars") #Pisin nimi
    print(f"Average name - {average:.2f} chars") #2 desimaalia
    print("#### REPORT END ####")

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()