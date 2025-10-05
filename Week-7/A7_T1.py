#Create a program that collects positive integers from the user until user enters 
# a negative integer. After this, the program should then display the collected 
# integers along with their indices and ordinals. If no integers are entered, 
# the program should gracefully handle the situation by displaying an appropriate 
# message.

    #Input: The program repeatedly prompt the user to enter positive integers. 
    # If the user enters a negative integer, the input process stops.

    #Validation: Only positive integers should be collected. 
    # A negative integer stops the input collection.

    #Output:
        #After input is stopped, the program will display the collected integers.
        #For each integer, show the following:
            #Index (starting from 0).
            #Ordinal (index + 1).
        #If there are no integers, inform the user that there are no integers to display.

    #Program Flow:
        #The program starts with the message: “Program starting.”
        #Collect positive integers from the user.
        #Stop collecting on a negative number.
        #After stopping input, display the results.
        #The program ends with the message: “Program ending.”

#Preferred datastructures:

    #list[int]


def main() -> None:
    print("Program starting.")
    print("Collect positive integers.")

    numbers: list[int] = [] #Listaan kerätään kaikki hyväksytyt positiiviset luvut.

    # Input loop
    while True: #Silmukka jatkuu, kunnes negatiivinen luku annetaan.
        value_str = input("Insert positive integer(negative stops): ")

        try:
            value = int(value_str) #Jos syöte ei ole luku → exception → pyydetään uudestaan.
        except ValueError:
            print("Invalid input, please enter an integer.")
            continue

        if value < 0: #Negatiivinen lopettaa
            break
        numbers.append(value) #Positiivinen tallennetaan

    print("Stopped collecting positive integers.")

    # Display results
    if len(numbers) == 0:
        print("No integers to display.")
    else:
        count = len(numbers)
        print(f"Displaying {count} integers:")
        for index, num in enumerate(numbers): #enumerate antaa sekä indeksin että itse arvon.
            ordinal = index + 1
            print(f"- Index {index} => Ordinal {ordinal} => Integer {num}")

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()