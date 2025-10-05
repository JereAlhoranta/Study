#Insert header comments into the beginning of each program file.

#Header comment example:

########################################################
# Task A9_Tx
# Developer First_name Last_name
# Date YYYY-MM-DD
########################################################

#Python documentations to study:

    #https://docs.python.org/3/tutorial/errors.html
    #https://docs.python.org/3/library/sys.html#sys.exit

#Example program run visualizations:

     #text  - program output (print)
     #text  - user input

#Create a Python program that prompts the user to insert floating-point values. 
# If the user inserts 0, stop the prompt and print the sum of the inserted values.

#If the user inserts an invalid value, such as “aaaaa” or “1.b2”, print an error 
# message indicating that the inserted value couldn’t be converted to a floating-point 
# number. Skip the incorrect feed and continue prompting.

#During the prompts, use the raw values for the presentation ("{}".format(Value)). 
# In the final sum presentation, use two decimal presentation format. 
# This can be achieved by using the float format specifier.

#"{:.2f}".format(Value)

########################################################
# Task A9_T1
# Developer Jere Alhoranta
# Date 2025-12-08
########################################################

def main() -> None:
    print("Program starting.\n")

total = 0.0  #SUMMA

while True:
    value_str = input("Insert a floating-point value (0 to stop): ")

    #Merkkijono floatiksi
    try:
        value = float(value_str)
        # Käyttäjä syöttää virheellisesti esim. "AAAA"
    except ValueError:
        print("Error! '{}' couldn't be converted to float.".format(value_str))
        continue  # palataan alkuun

    #Loopin lopetus
    if value == 0:
        break

    #Arvo -> Summaan
    total += value

print("\nFinal sum is {:.2f}".format(total))
print("Program ending.")

if __name__ == "__main__":
    main()