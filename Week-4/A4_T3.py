# Make Python program which prompts user to insert two integers. Use these integers together with the “while-loop” structure to create behaviour like in the example program run below.

# Note! the autograding tool will test that the correct structure has been applied

print("Program starting.")
Startvalue = int(input("\nInsert starting value: "))
Stopvalue = int(input("Insert stopping value: "))

print("\nStarting while-loop:")
current = Startvalue

while current <= Stopvalue:
    print(current, end=" ")
    current = current + 1
    
print("")   
print("\nProgram ending.")