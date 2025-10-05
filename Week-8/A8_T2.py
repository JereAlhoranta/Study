#Create a menu-driven program which can perform basic arithmetic operations. 
# All the math operations should be performed with floating datatype and without 
# rounding. Separate the functionality into the appropriate files.

#Recommended subprogram names for the main file:

    #def main() -> None:
    #def showOptions() -> None:
    #def askChoice() -> int:
    #def askValue(PPrompt: str) -> float:

#Recommended subprogram names for the library file:

    #def add(PAddend1: float, PAddend2: float) -> float:
    #def subtract(PMinuend: float, PSubtrahend: float) -> float:
    #def multiply(PMultiplicant: float, PMultiplier: float) -> float:
    #def divide(PDividend: float, PDivisor: float) -> float:

import calc_lib  #Laskenta tiedosto

def showOptions() -> None:
    #VALIKKO
    print("Options:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")

def askChoice() -> int:
    choice = int(input("Your choice: "))
    return choice

def askValue(PPrompt: str) -> float:
    #NUMERO
    value = float(input(PPrompt))
    return value

def main() -> None:
    print("Program starting.")

    while True:
        showOptions()      
        choice = askChoice()

        if choice == 0:
            print("Exiting program.")
            break  

        elif choice == 1:  # ADD
            v1 = askValue("Insert first addend value: ")
            v2 = askValue("Insert second addend value: ")
            result = calc_lib.add(v1, v2)
            print(f"{v1} + {v2} = {result}\n")

        elif choice == 2:  # SUBTRACT
            v1 = askValue("Insert minuend value: ")
            v2 = askValue("Insert subtrahend value: ")
            result = calc_lib.subtract(v1, v2)
            print(f"{v1} - {v2} = {result}\n")

        elif choice == 3:  # MULTIPLY
            v1 = askValue("Insert multiplicant value: ")
            v2 = askValue("Insert multiplier value: ")
            result = calc_lib.multiply(v1, v2)
            print(f"{v1} * {v2} = {result}\n")

        elif choice == 4:  # DIVIDE
            v1 = askValue("Insert dividend value: ")
            v2 = askValue("Insert divisor value: ")
            result = calc_lib.divide(v1, v2)
            print(f"{v1} / {v2} = {result}\n")

        else:
            print("Unknown option.\n")

    print("\nProgram ending.")
    return None


if __name__ == "__main__":
    main()