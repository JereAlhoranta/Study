# Create a Python program which prompts user to insert two integers. Use these integers together with the “for-loop” structure to create behaviour like in the example program example run below.

# Note! the autograding tool will test that the correct structure has been applied.

# Example program runs

print("Program starting.")
Startvalue = int(input("\nInsert starting value: "))
Stopvalue = int(input("Insert stopping value: "))

print("\nStarting for-loop:")

for i in range(Startvalue, Stopvalue + 1):
    print(i)
    

print("\nProgram ending.")
