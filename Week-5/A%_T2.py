#Create Python program which is able to print user input with a decorative frame.

#Program must consist of two functions:

    #main-function
       # Print starting and ending statements.
       # Print any empty row (see example program run)
     #  # #Prompt user to insert a word.
       # Pass the inserted word into the frameWord-function.
       # Returns None
   # frameWord
        #Takes PWord as a parameter.
        #Prints the framing and the PWord
        #    Hint: Multiply the asterisk '*'-character.
       # Returns None

#Note! Tests for this task relies on properly defined functions and may fail if the program is not written according to the instructions.



def frameWord(PWord: str) -> None: 
    # """
    #Tulostaa annetun sanan PWord ympärille kehykset.
    # """

    # Lasketaan kehyksen leveys: sana + 2 väliä + 2 tähteä
    frame_width = len(PWord) + 4 
    border = "*" * frame_width 
    #PWord: str = Parametri joka on merkkijono

    #Def = Määritellään funktio 
    # #frameWord = funktion nimi (testit etsivät tätä nimeä)

    #len(PWord) = Laskee merkkijonon pituuden

    #border = "*" * frame_width. esim. jos frame_width == 13, tästä tulee "*************"  

    #print(f"* {PWord} *"). 
        # f-string (muotoiltu merkkijono). 
        # {PWord} korvataan arvolla, esim. "Beautiful"
                  
    #Yläreuna
    print(border)
    #Keskirivi muodossa: * SANA *
    print(f"* {PWord} *") 
    #Alareuna
    print(border)

    return None 

def main() -> None:
    # """
    #Pääfunktio: tulostaa alku- ja lopputekstit,
    #kysyy sanan ja tulostaa sen kehyksessä.
    #"""

    print("Program starting.")
    word = input("Insert word: ")

    print()

    frameWord(word)

    print("\nProgram ending.")

    return None

if __name__ == "__main__":
    main()