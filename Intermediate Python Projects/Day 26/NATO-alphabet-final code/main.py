student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    # print(key, value)
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    # print(index, row)
    #Access row.student or row.score
    # print(row.student)
    # print(row.score)
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
with open("nato_phonetic_alphabet.csv", "r") as file:
    data = pandas.read_csv(file)
    new_data = pandas.DataFrame(data)
    new_dict = {row.letter: row.code for (letter, row) in new_data.iterrows()}
    # print(new_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter a word: ").upper()
name_list = [letter for letter in name]
# print(name_list)

phonetic_list = [new_dict[letter] for letter in name_list]
print(phonetic_list)

