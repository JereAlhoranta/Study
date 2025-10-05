from pathlib import Path

SEPARATOR = ";" #puolipiste erottaa arvot ja CSV-sarakkeet

def readValues(filename: str) -> str: #Lukee annetun tiedoston rivit ja palauttaa ne yhtenä merkkijonona, jossa arvot erotetaan SEPARATOR merkillä
    base_folder = Path(__file__).parent
    path = base_folder / filename
    with open(path, "r") as f:
        #poistetaan rivinvaihdot ja mahdolliset väli tai loppu spacet
        numbers = [line.strip() for line in f.read().splitlines() if line.strip() != ""]
        #yhdistetään yhdeksi merkkijonoksi esim. "13;45;20"
    return SEPARATOR.join(numbers)

def analyseValues(values_str: str): #ottaa vastaan puolipiste-erotellun numerosarjan merkkijonona ja laskee count, sum, greatest, average.
    if not values_str:
        count = 0
        total = 0
        greatest = 0
        average = 0.0
    else:
        parts = [int(p) for p in values_str.split(SEPARATOR)]
        count = len(parts)
        total = sum(parts)
        greatest = max (parts)
        average = total / count if count else 0.0

    header = "Count;Sum;Greatest;Average"
    data = f"{count};{total};{greatest};{average:.2f}"
    return f"{header}\n{data}\n"

def format_results(count: int, total: int, greatest: int, average: float) -> str: #muotoilee tuloksen CSV-tyylisesti puolipiste-erottimella. Keskiarvo kahden desimaalin tarkkuudella
    header = "Count;Sum;Greatest;Average"
    data = f"{count};{total};{greatest};{average:.2f}"
    return f"{header}\n{data}"

def main():
    print("Program starting.")
    filename = input("Insert filename: ").strip()

    print("#### Number analysis - START ####")
    try:
        values = readValues(filename)
        result_csv = analyseValues(values)
        
        print(f'File "{filename}" results:')
        print(result_csv, end="")
    except FileNotFoundError:
        print(f'Error: file "{filename}" not found.')
    except ValueError:
        print("Error: file must contain only positive integers (one per line).")
    finally:
        print("\n#### Number analysis - END ####")
        print("Program ending.")

if __name__ == "__main__":
    main()
