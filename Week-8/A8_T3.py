#Create a menu-driven program for analysing number files.

#Menu options:

    #1. Read values
    #2. Amount of values
    #3. Calculate sum of values
    #4. Calculate average of values

#The recommendation during the “readValues” operation is to skip the empty rows “\n” 
# and convert the rows into floating point values. Values can be stored into a list
# [float] data structure.

#The amount of values can be calculated directly by using the “len”- function for the 
# values list. For analysing (options 3 and 4), pass the list of values as an argument 
# to some specific function. After calculating the sum or the average, round the 
# results to one decimal precision. E.g. “1.234” => “1.2”



def showOptions() -> None: 
    #VALIKKO
    print("Options:")
    print("1 - Read values")
    print("2 - Amount of values")
    print("3 - Calculate sum of values")
    print("4 - Calculate average of values")
    print("0 - Exit")


def readValues(filename: str) -> list[float]:
    values: list[float] = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()  #Poistaa rivinvaihdot ja välilyönnit
            if stripped == "":
                continue
            number = float(stripped)  #muutetaan teksti luvuksi (float)
            values.append(number)

    return values


def sumValues(values: list[float]) -> float: 
    #LASKEE LISTAN
    total = sum(values)
    return round(total, 1)


def averageValues(values: list[float]) -> float: 
    #Laskee listan keskiarvon ja palauttaa sen 1 desimaalilla
    if len(values) == 0:
        return 0.0
    avg = sum(values) / len(values)
    return round(avg, 1)

from pathlib import Path

def main() -> None:
    print("Program starting.")

    values: list[float] = []

    while True:
        showOptions()
        choice = input("Your choice: ")

        if choice == "0":
            print("Exiting program.")
            break

        elif choice == "1":
            filename_input = input("Insert filename: ").strip()
            filename = Path(__file__).parent / filename_input
            values = readValues(filename)

        elif choice == "2":
            amount = len(values)
            print(f"Amount of values {amount}")

        elif choice == "3":
            if len(values) == 0:
                print("No values loaded.")
            else:
                total = sumValues(values)
                print(f"Sum of values {total}")

        elif choice == "4":
            if len(values) == 0:
                print("No values loaded.")
            else:
                avg = averageValues(values)
                print(f"Average of values {avg}")

        else:
            print("Unknown option.")

        print()

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()