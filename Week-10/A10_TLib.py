########################################################
# Task A10_E1 
# Developer Jere Alhoranta
# Date 2025-12-11
########################################################


import os
import sys


def readValues(PFilename: str, PValues: list[int]) -> None:
    """
    Reads integers from a file into PValues.
    File is searched from the same directory as the script.
    """
    PValues.clear()

    folder = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(folder, PFilename)

    try:
        with open(full_path, "r", encoding="UTF-8") as f:
            for line in f:
                row = line.strip()
                if row == "":
                    continue
                PValues.append(int(row))
    except Exception:
        print(f"Couldn't read file '{PFilename}'.")
        sys.exit(1)

    return None


def displayValues(PLabel: str, PFilename: str, PValues: list[int]) -> None:
    text = ", ".join(str(v) for v in PValues)
    print(f"{PLabel} '{PFilename}' -> {text}")


def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
    n = len(PValues)

    for iteration in range(n - 1):
        for index in range(n - iteration - 1):
            a = PValues[index]
            b = PValues[index + 1]

            if PAsc:
                # ascending
                if a > b:
                    PValues[index], PValues[index + 1] = b, a
            else:
                # descending
                if a < b:
                    PValues[index], PValues[index + 1] = b, a

    return None