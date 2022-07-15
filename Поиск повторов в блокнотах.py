import os

WINDOW_SIZE = 200
PATH = "C:/Users/A12/Desktop/БЛОКНОТЫ ПРОГРАММИРОВАНИЕ"

def find_repeated(file_path):
    print(f"Reading {file_path}... \n")
    with open(file_path, "r", encoding="UTF-8") as f:
        file_str = f.read()

    x = 0
    n = 1
    while x < len(file_str) - WINDOW_SIZE:
        end_view = x + WINDOW_SIZE
        view_window = file_str[x : end_view]
        find_index = file_str.find(view_window, end_view, len(file_str))

        # Find the length of fragment that bigger than window_size
        if find_index != -1:
            end_tail = 0
            #breakpoint()
            while file_str[end_view + end_tail] == file_str[find_index + WINDOW_SIZE + end_tail]:
                end_tail += 1

            repeat_fragment = file_str[x : end_view + end_tail]
            repeat_len = len(repeat_fragment)
            print(f"""{n}) Found repeated {repeat_len} chars
                  at {x} and at {find_index}:\n{repeat_fragment}\n\n""")
            x += repeat_len
            n += 1

            #Deleting upper fragment
            file_str=file_str.replace(repeat_fragment, "", 1)
            
        x += 1

    return file_str
    

def save_new_notepad(file_path, file_str):
    with open(file_path, 'w+', encoding='UTF-8') as f:
        f.write(file_str)


def main():
    cur_path, subdir_list, file_list = os.walk(PATH)
    print(file_list)
    for file_name in file_list:
        if file_name.endswith('.txt'):
            file_str = find_repeated(os.path.join(cur_path, file_name))
            new_file_name = os.path.join('Cleared', file_name)
            save_new_notepad(os.path.join(cur_path, new_file_name), file_str)

if __name__ == '__main__':
    main()
                
#find_repeated("C:/Users/A12/Desktop/БЛОКНОТЫ ПРОГРАММИРОВАНИЕ/C++.txt")
