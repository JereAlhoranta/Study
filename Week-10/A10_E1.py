########################################################
# Task A10_E1 
# Developer Jere Alhoranta
# Date 2025-12-11
########################################################

#Lajittelee listan PValues quick sort -algoritmilla.
#PAsc = True  -> nouseva järjestys (ascending)
#PAsc = False -> laskeva järjestys (descending)
#Funktio EI palauta listaa, vaan muuttaa PValues-listaa suoraan.
import sys
import os

def quickSort(PValues: list[int], PAsc: bool = True) -> None:
    def _quick_sort(arr: list[int], low: int, high: int, asc: bool) -> None:
        #jos alueella on 0 tai 1 alkiota, se on jo järjestyksessä
        if low >= high:
            return

        # Valitaan pivot = keskimmäinen alkio
        mid = (low + high) // 2
        pivot = arr[mid]

        i = low
        j = high

        while i <= j:
            if asc:
                # Nouseva: siirretään i:tä eteenpäin niin kauan kuin arr[i] < pivot
                while arr[i] < pivot:
                    i += 1
                # Siirretään j:tä taaksepäin niin kauan kuin arr[j] > pivot
                while arr[j] > pivot:
                    j -= 1
            else:
                # Laskeva: päinvastaiset vertailut
                while arr[i] > pivot:
                    i += 1
                while arr[j] < pivot:
                    j -= 1

            if i <= j:
                # Vaihdetaan alkiot keskenään
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        # Rekursiivisesti lajitellaan vasen ja oikea puoli
        if low < j:
            _quick_sort(arr, low, j, asc)
        if i < high:
            _quick_sort(arr, i, high, asc)

    # Tyhjä tai yhden alkion lista on jo järjestyksessä
    if len(PValues) <= 1:
        return

    _quick_sort(PValues, 0, len(PValues) - 1, PAsc)
    return None

#Lukee tiedostosta kokonaislukuja, yksi per rivi.
#Ohittaa tyhjät rivit.
#Palauttaa list[int].
def read_numbers_from_file(filename: str) -> list[int]:
    values: list[int] = []

    # Selvitetään kansion polku, jossa .py-tiedosto sijaitsee
    folder = os.path.dirname(os.path.abspath(__file__))
    # Liitetään tiedostonimi perään
    full_path = os.path.join(folder, filename)

    try:
        with open(full_path, "r", encoding="UTF-8") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                values.append(int(line))
    except Exception:
        print(f"Couldn't read file '{filename}'.")
        sys.exit(1)

    return values
#Muuttaa listan luvuista merkkijonoksi:
#[1000, 221, 392] -> "1000, 221, 392"
def format_numbers(values: list[int]) -> str:
    return ", ".join(str(v) for v in values)


def main() -> None:
    print("Program starting.")

    # 1. Selvitetään tiedoston nimi:
    #    - jos komentoriviparametri on annettu (len(sys.argv) == 2), käytetään sitä
    #    - muuten kysytään käyttäjältä
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = input("Insert filename: ")

    # 2. Luetaan luvut tiedostosta
    values = read_numbers_from_file(filename)

    # 3. Muodostetaan merkkijono alkuperäisistä arvoista
    raw_str = format_numbers(values)

    # 4. Tehdään kopiot nousevaa ja laskevaa lajittelua varten
    asc_values = values.copy()
    desc_values = values.copy()

    # 5. Lajitellaan quickSort-funktiolla
    quickSort(asc_values, PAsc=True)
    quickSort(desc_values, PAsc=False)

    asc_str = format_numbers(asc_values)
    desc_str = format_numbers(desc_values)

    # 6. Tulostetaan
    print(f"Raw '{filename}' -> {raw_str}")
    print(f"Ascending '{filename}' -> {asc_str}")
    print(f"Descending '{filename}' -> {desc_str}")

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()