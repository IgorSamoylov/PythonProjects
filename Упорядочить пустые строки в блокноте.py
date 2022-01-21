import re

path = "C:/Users/A12/Desktop/БЛОКНОТЫ ПРОГРАММИРОВАНИЕ/ПРОГРАММИРОВАНИЕ НА PYTHON.txt"
file = open(path,"rt", encoding="windows-1251")
string_data = file.read()
string_data = str(string_data)



string_data = re.sub("\n{5,}","\n\n\n\n\n", string_data)
#string_data = re.sub('\n{0,4}',"\n\n", string_data)


path = "C:/Users/A12/Desktop/БЛОКНОТЫ ПРОГРАММИРОВАНИЕ/ПРОГРАММИРОВАНИЕ НА PYTHON1.txt"
outp_file = open(path,"w", encoding="windows-1251")
outp_file.write(string_data)

file.close()
outp_file.close()



