#Collect red, green and blue integer values, each on range 0-255 inclusively. 
# This range is often described as “byte” or 8-bit. These 3 bytes (R, G and B) 
# can be used to describe one color using hex notation “#rrggbb”, where the “rr” 
# represents the amount of color red. The hex notation is created using the byte 
# information.

#28 = 162 = 255

#Above notation:

    #28 - 0-1 * 8 - 8-bits (base2)
    #162 - 0-f * 2 - Hexadecimals (base16)
    #255 - 0-9 0-255 - Integer representation (base10)

#So for example value 127(base-10) converts to 01111111(base-2) in 8-bit format or 
# 7F(base-16) in hexadecimal format.

#While prompting values, ensure that:

    #Values are numeric
    #Values are actually integers
    #Value is inclusively within the 0-255 range

#If any of these conditions aren’t met, then print the error message 
# "Couldn't perform the designed task due to the invalid input values.". 
# Continue the program execution to the end normally skipping the RGB displaying part. 
# One way to achieve this is to use “try-except” for the whole process and then any 
# incorrect value being collected raises exception. See Python Doc: Raising Exceptions

#If the RGB was ok, then show the details like in the example program run. 
# String format specified {:02x} converts integer into 2-digit hex format. 
# More details in the Python Documentation page Format Specification Mini-Language.

#Hex conversion example in Python REPL:

#>>> "#{:02x}{:02x}{:02x}".format(255, 127, 0)
#'#ff7f00'

# Kysytään vastaus merkkijonona
def askIntByte(PPrompt: str) -> int:
    Feed = input(PPrompt)

    try:
        value_float = float(Feed)
    except ValueError:
        print(f"\"{Feed}\" is non-numeric value.")
        raise Exception("Invalid input")

    #Kokonaisluku ilman desimaaleja
    if not value_float.is_integer():
        print(f"\"{Feed}\" is non-numeric value.")
        raise Exception("Invalid input")

    #Muutetaan arvo kokonaisluvuksi
    value_int = int(value_float)

    #arvo on välillä 0–255
    if value_int < 0 or value_int > 255:
        print(f"Value \"{Feed}\" is out of the range 0-255.")
        raise Exception("Invalid input")

    return value_int

#heksaväri muodossa "#rrggbb"
def createHex(PRed: int, PGreen: int, PBlue: int) -> str:
    return "#{:02x}{:02x}{:02x}".format(PRed, PGreen, PBlue)


def main():
    print("Program starting.")

    try:
        red = askIntByte("Insert red: ")
        green = askIntByte("Insert green: ")
        blue = askIntByte("Insert blue: ")

        #Heksakoodi
        hex_value = createHex(red, green, blue)

        #RGB tiedot
        print("RGB Details:")
        print(f"- Red {red}")
        print(f"- Green {green}")
        print(f"- Blue {blue}")
        print(f"- Hex {hex_value}")

        print(f"- Red byte {red:08b}")
        print(f"- Green byte {green:08b}")
        print(f"- Blue byte {blue:08b}")

    except Exception:
        print("Couldn't perform the designed task due to the invalid input values.")

    print("Program ending.")


if __name__ == "__main__":
    main()