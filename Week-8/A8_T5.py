#Create program which can handle basic user registrations and logins. 
# For this exercise, study the built-in library hashlib. 
# The passwords must be hashed with md5 and hexdigested to a string format. 
# It isn’t necessary to implement unique constraints on usernames.

#Main menu options:

    #1. Login
    #2. Register
    #3. Exit

#User menu options:

    #1. View profile
    #2. Change passsword (no need to implement)
    #3. Logout

#Use “credetials.txt” filename as place to store the credentials in CSV format. 
# The filename can be defined as constant variable on the top-level of the library file. 
# The value separator or delimiter must be a semicolon “;”.

#Example “credentials.txt”: 0;admin;58d613129c5e71de57ee3f44c5ce16bc

from LoginLib import login, register, viewProfile


def main() -> None:
    print("Program starting.")
    mainMenu()
    print("Program ending.")


def showOptions() -> None:
    print("Options:")
    print("1 - Login")
    print("2 - Register")
    print("0 - Exit")


def showUserMenu() -> None:
    print("User menu:")
    print("1 - View profile")
    print("0 - Logout")


def mainMenu() -> None:
    while True:
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting program.")
            break

        elif choice == 1:
            # Login
            username = askValue("username")
            password = askValue("password")

            success = login(username, password)
            if success:
                userMenu(username)
            else:
                print("Login failed. Invalid username or password.\n")

        elif choice == 2:
            # Register
            username = askValue("username")
            password = askValue("password")
            register(username, password)

        else:
            print("Unknown option.\n")


def userMenu(PUsername: str) -> None:
    while True:
        showUserMenu()
        choice = askChoice()

        if choice == 0:
            print("Logging out.\n")
            break

        elif choice == 1:
            # Näytä profiili
            profile = viewProfile(PUsername)
            if profile:
                user_id, username = profile
                print("### Profile ###")
                print(f"User id: {user_id}")
                print(f"Username: {username}")
                print("###############\n")
            else:
                print("Profile not found.\n")

        else:
            print("Unknown option.\n")


def askChoice() -> int:
    return int(input("Your choice: "))


def askValue(PPrompt: str) -> str:
    return input(f"Insert {PPrompt}: ")


if __name__ == "__main__":
    main()