

with open("./Input/Names/invited_names.txt", "r") as file:
   names = file.readlines()


with open("./Input/Letters/starting_letter.txt", "r") as file:
    letter_template = file.read()


for name in names:
    modified_name = name.strip()
    with open(f"./Output/ReadyToSend/letter_for_{modified_name.lower().replace(" ","_")}.txt","w") as file:
        modified_template = letter_template.replace("[name]",modified_name)
        file.write(modified_template)