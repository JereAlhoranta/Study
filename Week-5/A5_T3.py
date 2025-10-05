#Create a Python program with two functions:

    #main-function
        #Does the routines ("Program starting." and "Program ending.")
        #Utilizes askName-function.
        #Utilizes greetUser-function.
       # Returns None
   # askName-function
       # Prompts the user to insert name
       # Returns name
    #greetUser-function
       # Which takes PName as an argument
       # Greets the user "Hello {PName}!"
       # Returns None

#Note! Tests for this task relies on properly defined functions and may fail if the program is not written according to the instructions.

#Kysyy käyttäjältä nimen ja palauttaa sen.
def askName() -> str:
    name = input("Insert name: ")
    return name

#Tulostaa tervehdyksen käyttäjälle.
def greetUser (PName: str) -> None:
    print(f"Hello {PName}!")
    return None

#Ohjelman pääfunktio:
    #- tulostaa alku- ja lopputekstit
    #- kysyy nimen askName-funktiolla
    #- tervehtii käyttäjää greetUser-funktiolla
def main() -> None:
    print("Program starting.")

    name = askName()
    greetUser(name)

    print("Program ending.")

    return None

if __name__ == "__main__":
    main()