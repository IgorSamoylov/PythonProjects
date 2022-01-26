import re
import os

DIVIDER_LENGTH = 110
pattern = re.compile(r'\n+=+\n+')
pattern1 = re.compile(r'\n*={3,}\n+')
pattern2 = re.compile(r'\n{5,}')
repl = r'\n\n\n\n' + '=' * DIVIDER_LENGTH + r'\n\n\n'


def format_notepad(path, file_name):
    file_path = path + file_name
    try:
        with open(file_path, 'r', encoding='utf8') as f:
            file_str = f.read()
    except:
        with open(file_path, 'r', encoding='cp1251') as f:
            file_str = f.read()

    file_str = re.sub(pattern1, repl, file_str)
    file_str = re.sub(pattern2, repl, file_str)
    file_str = file_str.replace('­\n', '')

    try:
        #with open(path + 'FORMATED/' + file_name[:-4] + '1' + '.txt', "w") as f:
        with open(path + file_name, 'w', encoding='utf8') as f:
            f.write(file_str)
    except:
        pass
    


path = "C:/Users/A12/Desktop/БЛОКНОТЫ ПРОГРАММИРОВАНИЕ/"

files = os.walk(path)

file_tup = next(files)
for file_name in file_tup[2]:
    if file_name.endswith('.txt'):
        print(file_tup[0] + file_name)
        format_notepad(file_tup[0], file_name)

        
#format_notepad("C:/Users/A12/Desktop/БЛОКНОТЫ ПРОГРАММИРОВАНИЕ/JAVA.txt")
