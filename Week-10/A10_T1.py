########################################################
# Task A10_E1 
# Developer Jere Alhoranta
# Date 2025-12-11
########################################################

#First download the datasets above. Then create a program which 
#prompts user to insert a filename and then displays the file 
# content in two different ways:

#Vertically - Each value on its own row.
#Horizontally - Values on the same row, separated by comma and 
# space “, ”.

#While reading the file rows, strip the newline characters and 
# ignore empty rows.

import os

def readValues(filename: str) -> list[str]:
    values: list[str] = []

    folder = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(folder, filename)

    try:
        with open(full_path, "r", encoding="utf-8") as f:
            for line in f:
                cleaned = line.strip()
                if cleaned == "":
                    continue
                values.append(cleaned)
    except Exception:
        print(f"Couldn't read file '{filename}'.")
        return []

    return values

#tulostaa arvot vertikaalisesti
def printVertical(values: list[str]) -> None:
    print("# --- Vertically --- #")
    for v in values:
        print(v)
    print("# --- Vertically --- #")


#tulostaa arvot horisontaalisesti
def printHorizontal(values: list[str]) -> None:
    print("# --- Horizontally --- #")
    print(", ".join(values))
    print("# --- Horizontally --- #")


# MAIN-FUNKTIO
def main() -> None:
    print("Program starting.")

    filename = input("Insert filename: ")

    values = readValues(filename)

    # Jos tiedostoa ei voitu lukea, lopetetaan
    if values == []:
        print("Program ending.")
        return

    printVertical(values)
    printHorizontal(values)

    print("Program ending.")


if __name__ == "__main__":
    main()