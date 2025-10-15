print("Program starting.")

num = int(input("Insert a positive integer: "))
while num <= 0:
    num = int(input())

steps = 0 #alustaa laskurin, joka laskee kuinka monta kertaa silmukka suoritetaan, ennen kuin Collatz-jono päätyy arvoon 1.
sequence = str(num) #muuttaa annetun luvun merkkijonoksi. 

#Silmukka
while num != 1:
    if num % 2 == 0: #tarkistaa, onko luku parillinen (jakojäännös 0)
        num = num // 2 #jakaa luvun kahdella kokonaislukuna (ei desimaaleja)
    else:
        num = 3 * num + 1 #uorittaa parittoman luvun laskutoimituksen.
    sequence += " -> " + str(num)
    steps += 1

print(sequence)
print(f"Sequence had {steps} total steps.")                

print("\nProgram ending.")