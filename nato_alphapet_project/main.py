import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_alphapets = {row.letter:row.code for _,row in data.iterrows()}

print("Initiating Operator...")

def interpret_word(word: str):
    try:
        interpreted_word = [phonetic_alphapets[letter] for letter in word.upper()]
    except KeyError as error:
        print("Sorry, only letters in the alphabet please.")
        interpret_word(input("Try again: "))
    
    else:
        print(interpreted_word)
        

interpret_word(input("Enter a word: "))

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

