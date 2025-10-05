#In some scenarios, programs contain unsaved user data, and the user may accidentally 
# do something that typically causes the program to close. In CLI programs, this 
# occurs if the user sends a keyboard interrupt (CTRL + C). Handle the 
# KeyboardInterrupt in a menu-driven program, which collects user-inserted lines.

#If the user has inserted 0 lines during a program run, there is nothing to save.
# Handle the keyboard interrupt (CTRL + C) smoothly by informing the user that the 
# program is closing suddenly.

#If the user has inserted 1 or more lines and then presses CTRL + C, prompt the user 
# to confirm if they would like to save the lines to a file. If the user confirms 
# with yes, ask for the filename to write. Otherwise close the program gracefully.

#In the example program runs below, keypair ^C indicates user initiated 
# KeyboardInterrupt. Text after ^C on the same line represents program output after 
# keyboard interrupt (color glitch).


def showOptions() -> None:
    print("Options:")
    print("1 - Insert line")
    print("2 - Save lines")
    print("0 - Exit")
    # TODO: Print the menu options
    pass

def askChoice() -> int:
    try:
        choice_str = input("Your choice: ")
        choice = int(choice_str)
        return choice
    except ValueError:
        print("Invalid choice! Please insert a number.")
    # TODO: Ask user for a menu choice and return it as an integer
    # Students should use try-except to handle invalid input
    return -1

def saveLines(PLines: list[str]) -> None:
    if len(PLines) == 0:
        print("No lines to save.")
    # TODO: Ask for filename and save lines to the file
    # Students should use try-except to handle file errors
        return

    filename = input("Insert filename: ")
    
    try:
        with open(filename, "w", encoding="UTF-8") as f:
            for line in PLines:
                f.write(line + "\n")
    except OSError:
        print("Error while saving the file.")
    

def insertLine(PLines: list[str]) -> None:
    text = input("Insert text: ")
    PLines.append(text)
    # TODO: Ask user to input a line and add it to PLines

def onInterrupt(PLines: list[str]) -> None:
    if len(PLines) == 0:
        print("Keyboard interrupt. No lines to save!.")
        return

    print("Keyboard interrupt and unsaved progress!")
    answer = input("Save before quit(y/n)?: ")
    if answer.lower().startswith("y"):
        saveLines(PLines)
    # TODO: Handle KeyboardInterrupt when there are unsaved lines
    # Students should use try-except to handle input errors

def main() -> None:
    Lines: list[str] = []
    Choice = -1
    print("Program starting.")
    # Wrap the main loop in a try-except block to catch KeyboardInterrupt
    try:
        while Choice != 0:
            showOptions()
            Choice = askChoice()
            if Choice == 1:
                insertLine(Lines)
            elif Choice == 2:
                saveLines(Lines)
            elif Choice == 0:
                print("Exiting program.")
            else:
                print("Unknown option!")
        print("")

    except KeyboardInterrupt:
        onInterrupt(Lines)
       
    Lines.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()