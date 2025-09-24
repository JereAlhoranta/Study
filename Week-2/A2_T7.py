#Create a Python program to convert Fahrenheit to Celcius. Round the Celsius to 1 decimal precision.

#Formula to calculate Celcius from Fahrenheit is (Fahrenheit - 32) / 1.8

#Example program run:

#Program starting.
print("Program starting.")

#Insert fahrenheits: 50
Fahrenheits = float(input(f"Insert fahrenheits: "))

#50.0°F is 10.0°C
Celsius = round((Fahrenheits - 32) / 1.8, 1)

print(f"{Fahrenheits}°F is {Celsius}°C")

#Program ending.
print("Program ending.")