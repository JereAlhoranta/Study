#Structure timestamp data in program.

#This task is continuation to the A7_T3 task. You may start this task by copying 
# the previous datasets. Rename datasets to match this task 
# e.g., “A7_T3_D1.csv” => “A7_T4_D1.csv”.

#The dataset had four different values separated by a semicolon ;:

    #1. Weekday
    #2. Hour
    #3. Consumption(kWh)
    #4. Price(€/kWh)

#The goal is to print each timestamp from a file and also calculate the total of 
# consumption and price. Below is the output format for a single record.

#To keep the code maintainable, define a named datastructure for the different values. 
# Once defined, specify a way to read the timestamps into a list. 
# This can be done by reading a file line by line, skipping empty lines, trimming line 
# endings, and then splitting each line by the delimiter.

#To keep the code maintainable, define a named datastructure for the different values. 
# Once defined, specify a way to read the timestamps into a list. 
# This can be done by reading a file line by line, skipping empty lines, 
# trimming line endings, and then splitting each line by the delimiter.


from dataclasses import dataclass

DELIMITER = ";"

@dataclass #Luo automaattisesti luokan, jossa on kentät weekday, hour, consumption, price
class TIMESTAMP:
    weekday: str
    hour: str
    consumption: float
    price: float
    

def readTimestamps(Pfilename: str, Ptimestamps: list[TIMESTAMP]) -> None:
    print(f'Reading file "{Pfilename}".')
    Ptimestamps.clear()

    with open(Pfilename, "r", encoding="utf-8") as f:
        first_line = True
        for line in f:
            # Ohitetaan header-rivi
            if first_line:
                first_line = False
                continue

            # Poistaa rivinvaihdot ja mahdolliset ylimääräiset välit
            row = line.rstrip()
            if row == "":
                continue

            columns = row.split(DELIMITER) #Pilkkoo merkkijonon listaksi:
            #"Monday;00:00;154;0.09" → ["Monday", "00:00", "154", "0.09"]
            if len(columns) < 4:
                continue

            ts = TIMESTAMP(
                weekday=columns[0],
                hour=columns[1],
                consumption=float(columns[2]),
                price=float(columns[3]),
                #Muuttaa kulutuksen ja hinnan oikeaan numeeriseen muotoon laskemista varten.
            )
            Ptimestamps.append(ts)

    return None


def displayTimestamps(Ptimestamps: list[TIMESTAMP]) -> None:
    print("Electricity usage:")
    for ts in Ptimestamps:
        total = ts.price * ts.consumption
        print(
            f" - {ts.weekday} {ts.hour}, "
            f"price {ts.price:.2f}, "
            f"consumption {ts.consumption:.2f} kWh, "
            f"total {total:.2f} €"
            #Tulostaa desimaaliluvut kahden desimaalin tarkkuudella.
        )
    return None

from pathlib import Path

def main() -> None:
    print("Program starting.")
    filename_input = input("Insert filename: ").strip()
    filename = Path(__file__).parent / filename_input

    timestamps: list[TIMESTAMP] = []

    readTimestamps(str(filename), timestamps)
    displayTimestamps(timestamps)

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()