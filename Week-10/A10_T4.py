########################################################
# Task A10_E1 
# Developer Jere Alhoranta
# Date 2025-12-11
########################################################

import sys
from A10_TLib import readValues, displayValues  # käytetään samoja kuin T3:ssa

#Sulauttaa kaksi valmiiksi lajiteltua listaa (PLeft ja PRight)
#yhdeksi lajitelluksi listaksi PMerge.
#PMerge on tyhjä alussa, ja funktio täyttää sen.
#PAsc = True  -> nouseva
#PAsc = False -> laskeva
def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
    i = 0  # indeksi vasempaan listaan
    j = 0  # indeksi oikeaan listaan

    # niin kauan kuin molemmissa listoissa on jäljellä alkioita
    while i < len(PLeft) and j < len(PRight):
        left_val = PLeft[i]
        right_val = PRight[j]

        if PAsc:
            # Nouseva järjestys: pienempi ensin
            if left_val <= right_val:
                PMerge.append(left_val)
                i += 1
            else:
                PMerge.append(right_val)
                j += 1
        else:
            # Laskeva järjestys: suurempi ensin
            if left_val >= right_val:
                PMerge.append(left_val)
                i += 1
            else:
                PMerge.append(right_val)
                j += 1

    while i < len(PLeft):
        PMerge.append(PLeft[i])
        i += 1

    while j < len(PRight):
        PMerge.append(PRight[j])
        j += 1

    return None

#Lajittelee listan PValues merge sort -algoritmilla.
#PAsc = True  -> nouseva
#PAsc = False -> laskeva
#Lajittelu tapahtuu "paikan päällä" eli PValues muuttuu.
def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
    # Jos listassa on 0 tai 1 alkiota, se on jo lajiteltu
    if len(PValues) <= 1:
        return

    mid = len(PValues) // 2

    # jaetaan lista kahteen osaan
    left = PValues[:mid]
    right = PValues[mid:]

    # lajitellaan vasen ja oikea puoli rekursiivisesti
    mergeSort(left, PAsc)
    mergeSort(right, PAsc)

    # sulautetaan kaksi lajiteltua listaa yhdeksi
    merged: list[int] = []
    merge(left, right, merged, PAsc)

    # kopioidaan tulos takaisin alkuperäiseen listaan
    PValues[:] = merged
    return None


def main() -> None:
    Values: list[int] = []

    print("Program starting.")

    #Tiedostonimi: joko komentoriviltä tai kysytään käyttäjältä
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = input("Insert filename: ")

    # 2. Luetaan arvot
    readValues(filename, Values)

    # 3. Raw
    displayValues("Raw", filename, Values)

    # 4. Nouseva järjestys
    asc_values = Values.copy()
    mergeSort(asc_values, PAsc=True)
    displayValues("Ascending", filename, asc_values)

    # 5. Laskeva järjestys
    desc_values = Values.copy()
    mergeSort(desc_values, PAsc=False)
    displayValues("Descending", filename, desc_values)

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()