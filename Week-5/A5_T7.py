#Create a Python program which collects words in a collectWords-function and analyses the words in a analyseWords-function. 
# Use main-function to define the main logic.

#Separate words with comma ',' delimiter. Define DELIMITER at the beginning of the program on the top-level as a constant variable.

#Main logic

#Call the collectWords-function and store the words into a local variable. Next pass the collected words to the analyseWords-function.

#Word collecting:

#Prompt user to insert word. Repeat the prompt till the user enters an empty word. Collect all words into one variable where each word is separated by a DELIMITER. 
# At the end of the function, return the string variable holding all of the words.

#Analysing words:

#Takes one parameter containing words wrapped into one string. Calculates the amount of words, characters and the average word length. 
# Separating words must happen by utilizing the DELIMITER. Finally displays the results. Average word length must be presented in 2 decimal precision. This function should not return anything.

#Use print("- {:.2f} Average word length".format(Avg)) to print average word length in 2 decimal precision.

DELIMITER = ","

def collectWords(): #kysyy sanoja yksi kerrallaan. Jos painaa enter ilman sanaa, kerääminen loppuu.
    words = []
    while True:
        s = input("Insert word(empty stops): ")
        if s == "": ## jos käyttäjä ei kirjoita mitään -> lopeta
            break
        words.append(s)
    return DELIMITER.join(words)

def analyseWords(words_str):
    if words_str == "":
        words = []
    else:
        words = words_str.split(DELIMITER)

    word_count = len(words)    #montako sanaa
    char_count = sum(len(w) for w in words)   #kirjamia yhteensä
    avg_len = (char_count / word_count) if word_count > 0 else 0.0

    print(f"- {word_count} Words")
    print(f"- {char_count} Characters")
    print(f"- {avg_len:.2f} Average word length")

def main():
    print("Program starting.")
    collected = collectWords()  #1. kerää sanat
    analyseWords(collected)     #2. analysoi sanat
    print("Program ending.")

if __name__ == "__main__" or "unittest" in __import__("sys").modules:
    main()                 