#In this exercise, get familiar with the Caesar cipher and specificly on the 
# ROT13 implementation.

#Caesar Cipher explained (3 minutes): youtu.be/sMOZf4GN3oc

#Create a Python program which collects plain text rows from user till the user 
# inserts an empty row. Cipher all rows and then ask user to choose between showing 
# the ciphered text or saving it.

#Program must be able to cipher following lowercase and uppercase alphabets. 
# Other characters remains same during ciphering operation.


# 1) Aakkoset
LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def build_rot13_table():
    #Rakennetaan käännöstaulu (translation table) ROT13:lle.
    #str.maketrans palauttaa taulun, jota str.translate voi käyttää.
    
    # ROT13 siirtää 13 merkkiä eteenpäin, kiertäen aakkosissa
    lower_rot = LOWER_ALPHABETS[13:] + LOWER_ALPHABETS[:13]  # "nopqrstuvwxyzabcdefghijklm"
    upper_rot = UPPER_ALPHABETS[13:] + UPPER_ALPHABETS[:13]  # "NOPQRSTUVWXYZABCDEFGHIJKLM"
    # Maketrans saa kolme merkkijonoa: mistä -> mihin (yhdistetään pienet ja isot)
    table = str.maketrans(LOWER_ALPHABETS + UPPER_ALPHABETS, lower_rot + upper_rot)
    return table

# Luodaan taulu vain kerran
ROT13_TABLE = build_rot13_table()

def rot13_line(line: str) -> str:
    #Koodaa yhden tekstirivin ROT13:lla.
    #Ei-aakkoset (välit, numerot, välimerkit) pysyvät samoina.
    return line.translate(ROT13_TABLE)

def collect_lines() -> list[str]:
    #Kysyy käyttäjältä rivejä, kunnes annetaan tyhjä rivi (Enter).
    #Palauttaa listan alkuperäisistä riveistä (plaintext).
    print("\nCollecting plain text rows for ciphering.")
    rows = []
    while True:
        row = input("Insert row(empty stops): ")
        if row == "":               # tyhjä rivi lopettaa syötön
            break
        rows.append(row)
    return rows

def cipher_lines(lines: list[str]) -> list[str]:
    #Koodaa koko rivijoukon ROT13:lla ja palauttaa uudet rivit listana.
    return [rot13_line(r) for r in lines]

def show_ciphered(lines_ciphered: list[str]) -> None:
    #Tulostaa koodatut rivit ruudulle.
    print("\n#### Ciphered text ####")
    for r in lines_ciphered:
        print(r)

def save_ciphered(lines_ciphered: list[str], filename: str) -> None:
    #Tallentaa koodatut rivit tiedostoon (yksi rivi / rivi).
    with open(filename, "w", encoding="utf-8") as f:
        for r in lines_ciphered:
            f.write(r + "\n")
    print("Ciphered text saved!")

def ask_action() -> str:
    #Pyytää käyttäjää valitsemaan toiminnon: show tai save.
    #Palauttaa merkkijonon 'show' tai 'save'.
    while True:
        choice = input("\nType 'show' to display or 'save' to write into a file: ").strip().lower()
        if choice in ("show", "save"):
            return choice
        print("Please type exactly 'show' or 'save'.")

def main():
    print("Program starting.")
    # 1) Kerää rivit
    plaintext_lines = collect_lines()

    # Jos käyttäjä ei syöttänyt mitään, kerrotaan ja lopetetaan
    if not plaintext_lines:
        print("\nNo input provided. Nothing to cipher.")
        print("Program ending.")
        return

    # 2) Koodaa rivit
    ciphered = cipher_lines(plaintext_lines)

    # 3) Kysy mitä tehdään
    action = ask_action()

    if action == "show":
        show_ciphered(ciphered)
    else:  # "save"
        print("\n#### Ciphered text ####")
        filename = input("Insert filename to save: ").strip()
        if not filename:
            print("No filename provided. Aborting save.")
        else:
            save_ciphered(ciphered, filename)

    print("Program ending.")

if __name__ == "__main__":
    main()