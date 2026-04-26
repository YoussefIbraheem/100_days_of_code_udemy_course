import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_alphapets = {row.letter:row.code for _,row in data.iterrows()}

print("Initiating Operator...")

user_input = ""

while user_input == "":
    user_input = input("Hello! Enter the desired word\n ")

interpreted_word = [phonetic_alphapets[letter] for letter in user_input.upper() if letter.isalpha() ]

print(interpreted_word)

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

