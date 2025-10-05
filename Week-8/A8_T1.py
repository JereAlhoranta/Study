#Create a menu-driven program which has three options:

    #Set pause duration
    #Activate pause
    #Exit

#Utilize time-library’s sleep-function to implement the pause in the program.

#Create a single program file “A8_T1.py”. Use this exercise to build the “template.py” 
# mentioned earlier.

import time 

def main() -> None:
    print("Program starting.")

pause_duration = 0.0

while True:
    print("Options:")
    print("1 - Set pause duration")
    print("2 - Activate pause")
    print("0 - Exit")
    choice = input("Your choice: ")

    if choice == "0":
        print("Exiting program.")
        break 

    elif choice == "1":
        pause_duration = float(input("Insert pause duration (s): "))

    elif choice == "2":
        print(f"Pausing for {pause_duration} seconds.")
        time.sleep(pause_duration)
        print("Unpaused.")

    else:
        print("Unknown option.")

print("\nProgram ending.")

if __name__ == "__main__":
    main()