
# A3_T4 More menu options

# Extend the previous menu program by adding three more options to the menu.

# Options:

#     Print the name backwards
#         Your name backwards is "{NameBackwards}"
#     Print the first character
#         The first character in name "{Name}" is "{FirstChar}"
#     Show the amount of characters in the name
#         There are {NameLength} characters in the name "{Name}"

# Program starting.
print("Program starting.")
# This is a program with simple menu, where you can choose which operation the program performs.
print("This is a program with simple menu, where you can choose which operation the program performs.")
# Before the menu, please insert your name: John
name = input("Before the menu, please insert your name: ")

# Options:
print("\nOptions:")
# 1 - Print welcome message
print("1 - Print welcome message")
# 2 - Print the name backwards
print("2 - Print the name backwards")
# 3 - Print the first character
print("3 - Print the first character")
first_char = name[0]
# 4 - Show the amount of characters in the name
print("4 - Show the amount of characters in the name")
name_length = len(name)
# 0 - Exit
print("0 - Exits")
# Your choice: 1
choice = input("Your choice: ")
# Welcome John!
if choice == "1":
    print(f"Welcome {name}!")
elif choice == "2":
    print(f"Your name backwards is", f"\"{name[::-1]}\"")    
elif choice == "3":
    print(f"The first character in name \"{name}\" is f\"{first_char}\"")
elif choice == "4":
    print(f"There are {name_length}, characters in the name \"{name}\"")
elif choice == "0":
    print("Exiting...")
else:
    print("Unknown option.")

# Program ending.
print("\nProgram ending.")


