import pandas

nato_dataframe = pandas.read_csv("./Day26/NATO-alphabet-start/nato_phonetic_alphabet.csv")
# print(nato_dataframe.to_dict())

nato_phonetics_dict = {row.letter:row.code for (index,row) in nato_dataframe.iterrows()}
# print(nato_phonetics_dict)

input_name = input("Enter a Name: ").upper()
nato_encoded_list = []
# for char in input_name: #no error when name contains a space " "
#     for (letter,code) in nato_phonetics_dict.items():
#         if char == letter:
#             nato_encoded_list.append(code)
nato_encoded_list = [nato_phonetics_dict[letter] for letter in input_name]  #with a name with " " comes error will unfold
print(nato_encoded_list)



