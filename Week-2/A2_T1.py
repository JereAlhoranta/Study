#Make a Python program, which prompts the user name and two floating numbers. 
# Multiply the inserted numbers to get product. 
# Round the product in two decimal precision. 
# Complete the program output as shown below.

#Example program run:

#Program starting.
print("Program starting.")
#What is your name: John
Name = input("What is your name: ")
#Enter a floating point number: 3.1
First_number = input("Enter a floating point number: ")
First_number = float(First_number)
#Enter second floating point number: 5.3
Second_number = input("Emter second floating point number: ")
Second_number = float(Second_number)
#John you gave numbers 3.1 and 5.3
print(f"{Name} you gave numbers {First_number} and {Second_number}")
#Multiplying first and second number will result in product 16.43
Multi = First_number * Second_number
print(f"Multiplying first and second number will result in product {round(Multi, 2)}")
#Program ending.
print("Program ending")
