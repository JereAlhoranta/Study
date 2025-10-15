print("Program starting.")
print("\nCheck multiplicative persistence.")

while True:
    try:
        num = input("Insert an integer: ")
        int(num) # tarkistetaan, että syöte voidaan muuttaa kokonaisluvuksi
        break # jos onnistui, poistutaan silmukasta
    except ValueError:
        continue # jos ei onnistu, kysytään uudelleen

steps = 0
while len(num) > 1:
    numerot = [int(d) for d in num]
    lause = " * ".join(num)
    tulo = 1
    for d in numerot:
        tulo *= d
    print(f"{lause} = {tulo}")
    num = str(tulo)
    steps += 1  

print("No more steps.")
print(f"\nThis program took {steps} step(s)")
print("\nProgram ending.")