

# Write a Python program which asks user to insert hex color. 
# In this case hex color is expected to be the 7 character representation starting with # and followed by 6 0-F characters to represent RGB colors. 
# More about hex colors at https://en.wikipedia.org/wiki/Web_colors

#Slice the amount of red, green and blue from that inserted color and display each color as shown below.

#Example program run:

#Program starting.

print("Program starting.")

#Insert a hex color: #FFA500

Color = input(f"\nInsert a hex color: ")

#Colors
#- Red FF
Red = Color[1:3]
#- Green A5
Green = Color[3:5]
#- Blue 00
Blue = Color[5:7]

print(f"\nColors")
print(f"- Red {Red}")
print(f"- Green {Green}")
print(f"- Blue {Blue}")

#Program ending.

print("\nProgram ending.")