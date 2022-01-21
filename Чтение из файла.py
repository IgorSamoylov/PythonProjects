
with open("input_6_2_1.txt", "r") as file:
    str_list = file.readlines()

str_list.reverse()

with open("result.txt", "w") as res_file:
    res_file.writelines(str_list)
