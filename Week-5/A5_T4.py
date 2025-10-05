#The following code should calculate the area of a rectangle based on the user inputs.
#Fix the example code below without altering defined function names or 
# function parameters. 
# Fixed code must produce similar results as is in the expected program runs. 
# The code must also be fixed to match the requirements in the provided style guide.

def askDimension(PPrompt: str) -> float:
   value = float(input(f"Insert {PPrompt}: "))
   return value


def calcRectangleArea(PWidth: float, PHeight: float) -> float:
   area = PWidth * PHeight
   return area

def main() -> None:
    print ("Program starting.")

    width = askDimension("width")
    height = askDimension("height")
    print()

    area = calcRectangleArea(width, height)
    print(f"Area is {area}²")

    print("Program ending.")
    return None

if __name__ == "__main__":
   main()