#Analyse provided CSV data and create a summary of daily power usage and cost. 
# Use the data from the A7_T3 task. Rename files accordingly e.g., 
# “A7_T3_D1.csv” => “A7_T5_D1.csv”.

#For the summary, calculate the daily power usage and the cost.

    #Daily usage: Sum the consumption for each timestamp at the daily level. Use gatherer variable.
    #Daily cost: Multiply the consumption by the daily timestamp’s corresponding price. Then sum the results into an gatherer-type variable.

#Preferred datastructures:

    #Timestamps: list[TIMESTAMP]
    #Analysis helper: list[DAY_USAGE]
    #Results: list[str]


from dataclasses import dataclass
from pathlib import Path

DELIMITER = ";"

WEEKDAYS = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturnday",
    "Sunday",
)


@dataclass
class TIMESTAMP:
    weekday: str
    hour: str
    consumption: float
    price: float


def readTimestamps(filename: str) -> list[TIMESTAMP]:
    just_name = Path(filename).name
    print(f'Reading file "{just_name}".')
    timestamps: list[TIMESTAMP] = []

    with open(filename, "r", encoding="utf-8") as f:
        first = True
        for line in f:
            # Ohitetaan header
            if first:
                first = False
                continue

            # Siivotaan rivinvaihto
            row = line.strip()
            if row == "":
                continue  

            parts = row.split(DELIMITER)
            # parts[0] = weekday, [1] = hour, [2] = consumption, [3] = price
            ts = TIMESTAMP(
                weekday=parts[0],
                hour=parts[1],
                consumption=float(parts[2]),
                price=float(parts[3]),
            )
            timestamps.append(ts)

    return timestamps


def main() -> None:
    print("Program starting.")
    filename_input = input("Insert filename: ").strip()
    filename = Path(__file__).parent / filename_input

    timestamps = readTimestamps(str(filename))

    daily_usage = [0.0] * len(WEEKDAYS)
    daily_cost = [0.0] * len(WEEKDAYS)

    print("Analysing timestamps.")

    for ts in timestamps:
        if ts.weekday in WEEKDAYS:
            idx = WEEKDAYS.index(ts.weekday)
            daily_usage[idx] += ts.consumption
            daily_cost[idx] += ts.consumption * ts.price

    print("Displaying results.")
    print("### Electricity consumption summary ###")

    for i, weekday in enumerate(WEEKDAYS):
        usage = daily_usage[i]
        cost = daily_cost[i]
        print(f" - {weekday} usage {usage:.2f} kWh, cost {cost:.2f} €")

    print("### Electricity consumption summary ###")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()