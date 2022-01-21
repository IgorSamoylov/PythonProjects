
path = "test.txt"
#path = "input_6_2_2.txt"
with open(path, "r") as file:
    str_list = file.readlines()

res_strings = len(str_list)

big_string = ""
for string in str_list:
    big_string += string

res_letters = 0
for letter in big_string:
    if letter.isalpha():
        res_letters += 1

res_words = len(big_string.split())


print(f"Input file contains:\n{res_letters} letters\n{res_words} words\n{res_strings} lines") 
    
