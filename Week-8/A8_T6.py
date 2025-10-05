#Use svgwrite==1.4.3 library or build your own custom library to draw 
# SVGs(Scalable Vector Graphics).

#Links to get started with svgwrite

    #Latest svgwrite documentation: https://svgwrite.readthedocs.io/en/latest/
    #Package in Pypi: https://pypi.org/project/svgwrite/

#Create menu-driven program with following options:

    #1. Draw square (rectangle with both sides same length)
    #2. Draw circle
    #3. Save svg
    #4. Exit

#Start the program creation by initialising Drawing and then define functions to 
# fill in the details. Remember, passing object in Python works as reference 
# to the memory.

from svgwrite import Drawing
from drawLib import drawCircle, drawSquare, saveSvg


def main() -> None:
    print("Program starting.")
    Dwg = Drawing()  #oletuskokoinen piirros. Luodaan Drwaeing-olio

    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            print("Insert square")
            left = askValue1("Left edge position")
            top = askValue1("Top edge position")
            side = askValue1("Side length")
            fill = askValue1("Fill color")
            stroke = askValue1("Stroke color")

            drawSquare(Dwg, left, top, side, fill, stroke)

        elif choice == 2:
            print("Insert circle")
            centerX = askValue1("Center X position")
            centerY = askValue1("Center Y position")
            radius = askValue1("Radius")
            fill = askValue1("Fill color")
            stroke = askValue1("Stroke color")

            drawCircle(Dwg, centerX, centerY, radius, fill, stroke)

        elif choice == 3:
            filename = askValue2("Insert filename")
            print(f'Saving file to "{filename}"')
            confirm = input("Proceed (y/n)?: ")
            if confirm.lower() == "y":
                saveSvg(Dwg, filename)
                print("Vector saved successfully!")

        elif choice == 0:
            print("Exiting program.")
            break

        else:
            print("Unknown option.")

        print()

    print("Program ending.")


def showOptions() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Save svg")
    print("0 - Exit")


def askChoice() -> int:
    return int(input("Your choice: "))


def askValue1(PPrompt: str) -> str:
    return input(f"- {PPrompt}: ")


def askValue2(PPrompt: str) -> str:
    return input(f"{PPrompt}: ")


if __name__ == "__main__":
    main()