#Create a Python program that processes a list of comma-separated integers entered 
# by the user.

#The program will perform the following operations:

    #1. Parse the input, validate that all entries are valid integers.
    #2. If an invalid value is detected, output an error message indicating the 
    # invalid value, but still process the valid integers.
    #3. Calculate the sum of the valid integers and determine if the sum is even or odd.
    #4. Display the total count of valid integers, the sum of the integers, 
    # and whether the sum is even or odd.
    #5. If no valid integers are provided, display an appropriate message.

#Requirements:

    #Input:
        #The user inputs a comma-separated list of values.
        #The program parses these the entered values and checks if they are valid.
   # Output:
        #If all values are valid, display the number of integers, their sum, 
        # and whether the sum is even or odd.
        #If invalid values have been entered, display an error message for the 
        # invalid value.
        #If no valid integers remain after parsing, inform the user that there are no 
        # values to analyze.

#Preferred datastructures: list[int]

def main() -> None:
    print("Program starting.")

    raw = input("Insert comma separated integers: ")

    # Pilkotaan käyttäjän syöte listaksi merkkijonoja
    parts = raw.split(",") #jos syöte on "2,2,1,3" → parts = ["2", "2", "1", "3"]
                            #1. Pilkkominen

    numbers: list[int] = []

    for p in parts:
        p = p.strip()
        if p == "":
            continue  # ohitetaan tyhjät arvot kuten ", ,"
        try: #Validointi try/except-lohkolla
            num = int(p)
            numbers.append(num)
        except ValueError: #Jos int() ei pysty muuntamaan (esim "hello"), 
            #se ei kaada ohjelmaa, vaan tulostaa virheen.
            print(f"Invalid value: {p}")

    # Jos ei validoituja numeroita ole
    if len(numbers) == 0:
        print("No valid integers to analyze.")
        print("Program ending.")
        return None

    # Lasketaan summa
    total = sum(numbers)

    # Tarkistetaan parillisuus
    if total % 2 == 0: 
        parity = "even"
    else:
        parity = "odd"

    # Tulostetaan raportti
    count = len(numbers) #4. Ei yhtään validia arvoa
    print(f"There are {count} integers in the list.")
    print(f"Sum of the integers is {total} and it's {parity}")

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()