#Create a menu-driven Python program with following options:

    #1 Insert a word
        #1. Which stores user inserted word into memory.
    #2 Show current word
        #1. Prints the word from the memory
    #3 Show current word in reverse
        #1. Prints the word from the memory in reverse.
    #4 Exit
        #1. Stops the program gracefully
    #5 Unknown option

#Initialize the Word with an empty string.

def main() -> None:
    print("Program starting.")

    Word = "" #Tähän tallennetaan käyttäjän antama sana.

    while True:
        print("Options:")
        print("1 - Insert word")
        print("2 - Show current word")
        print("3 - Show current word in reverse")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            Word = input("Insert word: ")
            print()

        elif choice == "2":
            print(f'Current word - "{Word}"')
            print()

        elif choice == "3":
            reversed_word = Word[::-1] #Slicing-syntaksi: alkaa lopusta, askellus -1
            print(f'Word reversed - "{reversed_word}"')

        elif choice == "0":
            print("Exiting program.\n")
            break

        else:
            print("Unknown option.\n")

    print("Program ending.")
    return None

if __name__ == "__main__":
        main()        