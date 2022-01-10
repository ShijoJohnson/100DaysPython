import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TO DO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TO DO 2. Create a list of the phonetic code words from a word that the user inputs.

while True:
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Please enter only alphabets")
    else:
        print(output_list)


