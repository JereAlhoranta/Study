# Make Python program and implement if-statements in proper places.

#     Ask user to insert two integers

#     Compare the integers and then announce the greater number
#     Create sum of the two integers
#     Check the parity of the sum (see modulo-operator ‘%’)

# Other possible output variants:

#     Integer comparison
#         Integers are the same.
#         First integer is greater.
#     Parity check
#         Sum is even.


# Program starting.
print("Program starting.")
# Insert two integers.
print("Insert two integers.")
# Insert first integer: 5
Int1 = int(input("Insert first integer: "))
# Insert second integer: 5
Int2 = int(input("Insert second integer: "))
# Comparing inserted integers.
print("Comparing inserted integers.")
if(Int1 > Int2):
    print("First integer is grater.")
elif(Int2 > Int1):
    print("Second integer is greater.")
# Integers are the same
else:
    print("Integers are the same")
    print("")        
# Adding integers together
print("\nAdding integers together")
Sum = Int1 + Int2
# 5 + 5 = 10
print(f"{Int1} + {Int2} = {Sum}")
print("")
# Checking the parity of the sum...
print("\nChecking the parity of the sum...")
Remainder = Sum % 2
# Sum is even.
if(Remainder == 0):
    print("Sum is even.")
else:
    print("Sum is odd.")    
# Program ending.
print("Program ending.")





