#Prompt the user to insert exit code. Exit the program with using sys.exit and the 
# user defined exit code. Remember to convert the value into an integer. sys.exit 
# expects value between 0-255.

#sys.exit usage:

#import sys

#sys.exit(0) # Success exit code
#sys.exit(1) # Error exit code

########################################################
# Task A9_T2
# Developer Jere Alhoranta
# Date 2025-12-08
########################################################

import sys

def main() -> None:
    print("Program starting.")

value_str = input("Insert exit code(0-255): ")

try:
    code = int(value_str)
except ValueError:
    print("Invalid exit code! Must be an integer.")
    sys.exit(1)   # virheellinen lopetus

if code < 0 or code > 255:
    print("Invalid exit code! Must be between 0-255.")
    sys.exit(1)   # virheellinen lopetus

print("Clean exit")
sys.exit(code)

if __name__ == "__main__":
    main()