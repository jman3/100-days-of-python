import pandas as pd
# TODO 1. Create a dictionary using the csv file

df = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_code = {
    row.letter: row.code for (idx, row) in df.iterrows()
}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs
user_input = input("Enter a word: ").upper()
result = [phonetic_code[letter] for letter in user_input]
print(result)