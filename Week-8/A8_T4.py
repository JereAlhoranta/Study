from datetime import datetime
from pathlib import Path

# KUUKAUDET
MONTHS = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
)

# VIIKONPÄIVÄT
WEEKDAYS = (
    "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"
)

#LUKEE TIESTAMPIT YHDESTÄ TIEDOSTOSTA
def readTimestamps(PFilename: str, PTimestamps: list[datetime]) -> None:
    PTimestamps.clear()

    path = Path(__file__).parent / PFilename

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            row = line.strip()
            if row == "":
                continue
            # Muoto: 2000-04-11T05:01 -> %Y-%m-%dT%H:%M
            ts = datetime.strptime(row, "%Y-%m-%dT%H:%M")
            PTimestamps.append(ts)

#LASKEE MONTA TIMESTAMPIA ON TIETYLTÄ VUODELTA
def calculateYears(PYear: int, PTimestamps: list[datetime]) -> int:
    count = 0
    for ts in PTimestamps:
        if ts.year == PYear:
            count += 1
    return count

#LASKEE MONTA TIMESTAMPIA ON TIETYLTÄ KUUKAUDELTA
def calculateMonths(PMonth: str, PTimestamps: list[datetime]) -> int:
    if PMonth not in MONTHS:
        return 0

    month_number = MONTHS.index(PMonth) + 1  # January = 1, ..., December = 12

    count = 0
    for ts in PTimestamps:
        if ts.month == month_number:
            count += 1
    return count

#LASKEE MONTAKO TIMESTAMPIA ON TIETYLTÄ VIIKONPÄIVÄLTÄ
def calculateWeekdays(PWeekday: str, PTimestamps: list[datetime]) -> int:
    if PWeekday not in WEEKDAYS:
        return 0

    weekday_index = WEEKDAYS.index(PWeekday)  # Monday = 0, ..., Sunday = 6

    count = 0
    for ts in PTimestamps:
        if ts.weekday() == weekday_index:
            count += 1
    return count


def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ").strip()

    timestamps: list[datetime] = []
    readTimestamps(filename, timestamps)

    while True:
        print("Options:")
        print("1 - Calculate amount of timestamps during year")
        print("2 - Calculate amount of timestamps during month")
        print("3 - Calculate amount of timestamps during weekday")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "0":
            print("Exiting program.")
            break

        elif choice == "1":
            year_str = input("Insert year: ")
            year = int(year_str)
            amount = calculateYears(year, timestamps)
            print(f"Amount of timestamps during year '{year}' is {amount}\n")

        elif choice == "2":
            month = input("Insert month: ")
            amount = calculateMonths(month, timestamps)
            print(f"Amount of timestamps during month '{month}' is {amount}\n")

        elif choice == "3":
            weekday = input("Insert weekday: ")
            amount = calculateWeekdays(weekday, timestamps)
            print(f"Amount of timestamps during weekday '{weekday}' is {amount}\n")

        else:
            print("Unknown option.\n")

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()