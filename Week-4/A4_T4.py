# Make a program, which prompts user to insert words. 
# Program must stop prompting words if user inserts empty word. 
# After stopping the repetitive prompt, print the amount of words and characters that the user inserted.

print("Program starting.")
print("")

Sanat = 0
Kirjain = 0

Word = input("Insert word (empty stops): ")
while Word != '':
    Sanat += 1
    Kirjain += len(Word)
    Word = input("Insert word (empty stops): ")

print("\nYou inserted:")
print(f"- {Sanat} words")
print(f"- {Kirjain} characters")

print("\nProgram ending.")