import hashlib

CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"

# Muutetaan salasana tavuiksi ja lasketaan md5
def hash_password(password: str) -> str:
    return hashlib.md5(password.encode("utf-8")).hexdigest()

# 1. Luetaan olemassa olevat rivit, jotta tiedetään seuraava id
def register(PUsername: str, PPassword: str) -> None:
    try:
        with open(CREDENTIALS_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    new_id = len(lines)  # id = rivien määrä

    # 2. Hashataan salasana
    password_hash = hash_password(PPassword)

    # 3. Kirjoitetaan uusi käyttäjä tiedoston loppuun
    with open(CREDENTIALS_FILE, "a", encoding="utf-8") as f:
        row = f"{new_id}{DELIMITER}{PUsername}{DELIMITER}{password_hash}\n"
        f.write(row)

    print("User registration completed!\n")


def login(PUsername: str, PPassword: str) -> bool:
    # 1. Hashataan annettu salasana
    password_hash = hash_password(PPassword)

    # 2. Luetaan tiedosto ja verrataan
    try:
        with open(CREDENTIALS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue

                parts = line.split(DELIMITER)
                if len(parts) != 3:
                    continue

                user_id, username, stored_hash = parts

                if username == PUsername and stored_hash == password_hash:
                    # Löytyi osuma
                    return True
    except FileNotFoundError:
        # Ei vielä käyttäjiä rekisteröitynä
        return False

    # Ei löytynyt
    return False


def viewProfile(PUsername: str) -> list[str]:
    try:
        with open(CREDENTIALS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue

                parts = line.split(DELIMITER)
                if len(parts) != 3:
                    continue

                user_id, username, _ = parts

                if username == PUsername:
                    # Profiili löytyi
                    return [user_id, username]
    except FileNotFoundError:
        return []

    # Ei löytynyt
    return []


def change_password(PUsername: str, PNewPassword: str) -> None:
    print("Change password is not implemented.\n")