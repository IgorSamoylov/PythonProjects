
#path = "test.txt"
path = "input_6_2_2.txt"
with open(path, "r") as file:
    big_str = file.read()

res_strings = len(big_str.split("\n")) - 1

res_words = 0
res_letters = 0
write_word = True
for letter in big_str:
    if letter.isalpha():
        res_letters += 1
        if write_word:
            res_words += 1
            write_word = False
    else:
        write_word = True
        
        

print(f"Input file contains:\n{res_letters} letters\n{res_words} words\n{res_strings} lines") 
    
