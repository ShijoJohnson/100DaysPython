#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./input/Letters/starting_letter.txt") as letter:
    letter_str = letter.read()
    # print(letter_str)

with open("./input/Names/invited_names.txt") as names:
    names_str = names.read()
    # print(names_str)
    names_lst = names_str.split("\n")
    print(names_lst)

for name in names_lst:
    ltr = letter_str.replace("[name]", name)
    with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as file:
        file.write(ltr)