with open("Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
    names_final = []
    for name in names:
        stripped_name = name.strip("\n")
        names_final.append(stripped_name)

with open("Input/Letters/starting_letter.txt") as starting_letter:
    letter_contents = starting_letter.read()
    for name in names_final:
        new_letter = letter_contents.replace("[name]", name)
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letter:
            letter.write(new_letter)