
########################################################
# Task A10_E1 
# Developer Jere Alhoranta
# Date 2025-12-11
########################################################

import sys
import os  # tarvitaan, että löydetään tiedosto samasta kansiosta
from A10_TLib import readValues, displayValues, bubbleSort


def main() -> None:
    Values: list[int] = []
    Filename = ""

    print("Program starting.")

    if len(sys.argv) == 2:
        Filename = sys.argv[1] 
    else:
        Filename = input("Insert filename: ")

    # tiedosto haetaan samasta kansiosta, missä main.py sijaitsee.
    script_folder = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_folder, Filename)

    # Luetaan arvot tiedostosta Values-listaan
    readValues(full_path, Values)

    # Näytetään "Raw" arvot (alkuperäinen järjestys)
    #  Oletus: displayValues(Label, Filename, Values)
    displayValues("Raw", Filename, Values)

    # Lajitellaan nouseva järjestys
    asc_values = Values.copy()          # tehdään kopio, ettei alkuperäinen katoa
    bubbleSort(asc_values, PAsc=True)   # nouseva järjestys
    displayValues("Ascending", Filename, asc_values)

    # Lajitellaan laskeva järjestys
    desc_values = Values.copy()
    bubbleSort(desc_values, PAsc=False)  # laskeva järjestys
    displayValues("Descending", Filename, desc_values)

    # 7. Tyhjennetään listat
    Values.clear()
    asc_values.clear()
    desc_values.clear()

    print("Program ending.")


if __name__ == "__main__":
    main()