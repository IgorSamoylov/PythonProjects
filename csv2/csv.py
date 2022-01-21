
result_str = ""

with open('input_6_3_2.csv', 'r', encoding='utf-8') as file:
    str_file = file.read()
    string_list = str_file.split('\n')
    for record in string_list:
        tup = tuple(record.split(';'))
        #breakpoint()
        if len(tup) < 2:
            break
        result_str += tup[1] + ';' + tup[0] + '\n'

with open('result_input_6_3_2.csv', 'w', encoding='utf-8') as file:
    file.write(result_str)
    
