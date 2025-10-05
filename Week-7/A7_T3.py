#In this task, create a program that reads timestamps from a textfile. 
# The file content is in “.csv” format and contains information related to electricity 
# usage.

#CSV format:

    #Has header row
    #Columns
        #Weekday
        #Hour
        #Consumption(kWh)
        #Price(€/kWh)
    #Separator ;

#Download the datasets to your computer and set up the following steps in your program:

    #1. Prompt user to insert the filename
    #2. Read the specified file
        #1. Skip header row
        #2. Read line and remove newline character
       #3. If line is empty (contains only newline character), skip line
   #3. Analyse timestamps per weekday
       #1. Count each row that starts with weekday (Row.startswith(…))
   #4. Display results

##When analysing and creating results, the recommendation is to pass the data rows and 
# the results list to the analyse function. This analyse function then reads the 
# datarows, does the calculations and fills the results list when needed.

#Displaying the results could be a function that simply iterates through the results 
# and displays them. Below is a code example that can help structure the code for the 
# task.

#Preferred datastructures:

    #WEEKDAYS: tuple[str]
    #Rows: list[str]
    #Results: list[str]

#You may run the program with single bash command:

#echo -e "A7_T3_D1.csv\n" | python A7_T3.py


#(huomaa "Saturnday"-kirjoitusasu!)
WEEKDAYS: tuple[str, ...] = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturnday",
    "Sunday",
)


def readFile(PFilename: str, PRows: list[str]) -> None:
    print('Reading file "{}".'.format(PFilename))
    # Varmuuden vuoksi tyhjennetään PRows-lista ennen käyttöä
    PRows.clear()

    #Avataan tiedosto luettavaksi
    with open(PFilename, "r", encoding="utf-8") as f:
        first_line = True #Käytetään header rivin ohittamiseen
        #Luetaan teidosto rivi kerrallaan
        for line in f:
            # Ohitetaan ensimmäinen rivi, joka on header
            if first_line:
                first_line = False
                continue

            # Ohitetaan tyhjät rivit
            if line == "\n":
                continue

            #Poistetaan rivinvaihto lopusta ja lisätään listaan
            line = line.rstrip("\n")
            if line != "":
                PRows.append(line)
    #with-sulkee tiedoston automaattisesti
    return None


def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    #Tyhjennetään mahdollinen vanha sisältö
    PResults.clear()

    #Apulista laskemaan kuinka monta riviä kuuluu millekin viikonpäivälle
    WeekdayTimestampAmount: list[int] = [0, 0, 0, 0, 0, 0, 0]

    #Käydään kaikki rivit läpi
    for row in PRows:
        #Tarkistetaan mikä WEEKDAYS-alku löytyy rivin alusta
        for j, weekday in enumerate(WEEKDAYS):
            if row.startswith(weekday):
                #Lisätään laskuriin 1 oikealle viikonpäivälle
                WeekdayTimestampAmount[j] += 1
                break  #kun löydettiin oikea päivä, voidaan hypätä seuraavaan riviin

    #Muodostetaan tulosrivit weekday-laskureiden perusteella
    for i, weekday in enumerate(WEEKDAYS):
        count = WeekdayTimestampAmount[i]
        PResults.append(f" - {weekday} {count} stamps")

    #Tyhjennetään apulista
    WeekdayTimestampAmount.clear()
    return None


def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Timestamp analysis ###")
    #Tulostetaan jokainen analyysin tulosrivi
    for line in PResults:
        print(line)
    print("### Timestamp analysis ###")
    return None

from pathlib import Path

def main() -> None:
    print("Program starting.")
    #Alustetaan listat datariveille ja tuloksille
    Rows: list[str] = []
    Results: list[str] = []

    #Pyydetään käyttäjältä tiedoston nimi
    filename_input = input("Insert filename: ").strip()

    filename = Path(__file__).parent / filename_input

    readFile(filename, Rows)
    analyseTimestamps(Rows, Results)
    displayResults(Results)

    Rows.clear()
    Results.clear()

    print("Program ending.")
    return None

if __name__ == "__main__":
    main()