#Make a menu-driven Python program which mimics Tally Counter.

#This menu-driven program must contain a maintainable program structure with the following requirements:

    #main function which represents the main program logic including menu cycle.
    #showOptions function which takes no arguments, shows the available options in the standard output and returns None.
    #askChoice function which takes no arguments, prompts user to insert choice and returns an integer regardless of the user feed.

#In case user incorrectly inserts text as a choice, the program must output "Unknown option!". 
# For this, see the string method isnumeric() behaviour described in W3S or via Python documentation.
#See other requirements in the example program runs below.

def showOptions():
    print("Options:")
    print("1 - Show count")      #Näyttää nykyisen luvun
    print("2 - Increase count")  #Kasvattaa laskuria ja tulostaa “Count increased!”
    print("3 - Reset count")     #Nollaa laskurin ja tulostaa “Cleared count!”
    print("0 - Exit")
    

def askChoice():
    s = input("Your choice: ")  # käyttäjä kirjoittaa jotain
    if s.isnumeric():           # tarkistetaan onko numero
        return int(s)           # jos on, muutetaan numeroksi ja palautetaan
    else:
        return -1               # jos ei ole numero, palautetaan -1
    

def main():
    print("Program starting.")
    count = 0                   # laskuri alkaa nollasta


    while True:                 # ohjelma pyörii, kunnes käyttäjä haluaa poistua
        print()
        showOptions()
        choice = askChoice()


        if choice == 1:
            print(f"Current count - {count}")
        elif choice == 2:
            count += 1
            print("Count increased!")
        elif choice == 3:
            count = 0
            print("Cleared count!")
        elif choice == 0:
            print("Exiting program.")
            break
        else:
            print("Unknown option!")

    print("\nProgram ending.")

if __name__ == "__main__" or "unittest" in __import__("sys").modules:
    main()                    