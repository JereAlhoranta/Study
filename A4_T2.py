# Copy the previous program and modify the behaviour to match the example program run below. This program must use “for-loop” structure.

# It is recommended to replace the print-command end character with space, so that all the iterations can be printed on the same row. Last iteration might require additional logic to get rid of the extra space at the end.

# Note! the autograding tool will test that the correct structure has been applied

print("Program starting.")
Startvalue = int(input("\nInsert starting value: "))
Stopvalue = int(input("Insert stopping value: "))

print("\nStarting for-loop:")

for i in range(Startvalue, Stopvalue + 1):
    print(i, end=' ')
    
print("")   
print("\nProgram ending.")