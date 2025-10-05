# Create a program with a plain menu.

#     Prompt username first
#     Make program menu with following options:
#         Print welcome message
#             Welcome {Name}!
#         Exit
#             Exiting...
#     Prompt user to choose option “Your choice:”
#     Perform actions based on the user input

# Creating menus like this is a really handy way to make tiny text-based programs and there will be more exercises like this in the future.

# The expectation at this point is that the user is able to choose option by inserting corresponding number. No error handling is required, it will be introduced later.

# Other possible output variats:

#     Unknown option.

# Example program runs

# Program starting.
print("Program starting.")
# This is a program with simple menu, where you can choose which operation the program performs.
print("This is a program with simple menu, where you can choose which operation the program performs.")
# Before the menu, please insert your name: John
name = input("Before the menu, please insert your name: ")

# Options:
print("\nOptions:") #\n = rivinvaihto alespäin
# 1 - Print welcome message
print("1 - Print welcome message")
# 0 - Exit
print("0 - Exit")
# Your choice: 1
choice = input("Your choice: ")
# Welcome John!
if choice == "1":
    print(f"Welcome {name}!")
elif choice == "0":
    print("Exiting...")
else:
    print("Unknown option.")        

# Program ending.
print("\nProgram ending.")


