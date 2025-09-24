#Make a Python program, which prompts for a compound word.

#Get following aspects from the word
    #Length
    #First character
    #Reversed version e.g. “Suitcase” is reversed “esactiuS”
    #Display the aspects using print commands.
    #Prompt the user to take substring from the existing compound word.
    #Finally print the user specified substring.

#Example program run:

#Program starting.
print("Program starting.")
#Insert a closed compound word: Moonbanana
Word = input(f"\nInsert a closed compound word: ")
#The word you inserted is 'Moonbanana' and in reverse it is 'ananabnooM'.
print(f"The word you inserted is", f"'{Word}'", "and in reverse it is " f"'{Word[::-1]}'." )
#The inserted word length is 10
print(f"The inserted word length is", len(Word))
#Last character is 'a'
print(f"Last character is", f"'{Word[-1]}'")

#Take substring from the inserted word by inserting...
print("\nTake substring from the inserted word by inserting...")
#1) Starting point: 0
start = int(input("1) Starting point: "))
#2) Ending point: 4
end = int(input("2) Ending point: "))
#3) Step size: 1
step = int(input("3) Step size: "))

#The word 'Moonbanana' sliced to the defined substring is 'Moon'.
substring = Word[start:end:step]

print(f"\nThe word '{Word}' sliced to the defined substring is '{substring}'.")

#Program ending.

print("Program ending.")