#Create a program, which collects reasonable Celsius. Range listed below:

#TEMP_MIN = -273.15
#TEMP_MAX = 10000

#For this exercise, define collectCelsius function which returns collected celsius 
# or raises following error:

    #ValueError: "could not convert string to float: '{Feed}'"
    #Exception: "{Celsius} temperature out of range."

#FUNTKIOT
TEMP_MIN = -273.15
TEMP_MAX = 10000


def collectCelsius() -> float:
    feed = input("Insert Celsius: ")

    try: ## 1. Muunnetaan syöte floatiksi
        value = float(feed)
    except ValueError: #Jos kirjoittaa esim "ABC"
        raise ValueError(f"could not convert string to float: '{feed}'")

    if value < TEMP_MIN or value > TEMP_MAX: #Tarkista arvoalue
        raise Exception(f"{value} temperature out of range.")

    return value

#OHJELMA
def main() -> None:
    print("Program starting.")

try:
    celsius = collectCelsius()
    print(f"You inserted {celsius} °C")
except Exception as e:
    # Tulostamme virheen, mutta ohjelma ei kaadu
    print(e)

print("Program ending.")

if __name__ == "__main__":
    main()