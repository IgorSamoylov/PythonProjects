
with open('input_6_3_1.csv', 'r', encoding='utf-8') as file:
    record_list = file.readlines()

comp = {}
for r in record_list:
    r_tup = r.split(';')
    name = r_tup[0]
    pay = int(r_tup[1]) # Перобразуем второй кусок строки в int - значение зарплаты

    if not name in comp: # Если ещё нет первого значения по имени компании в словаре, то создаем его
        comp[name] = (pay, 1)
    else:
        comp[name] = (comp[name][0] + pay, comp[name][1] + 1)  # Дополняем словарь для каждого имени компании кортежем суммарная зарплата - +1 работник

comp_med_pay = {name :  p[0] / p[1] for name, p in comp.items()} # Создаём словарь имя компании - средняя зарплата
comp_med_pay = [(name, payment) for name, payment in comp_med_pay.items()] # Преобразуем словарь в список кортежей для сортировки

def sorter(t):
    return t[1]

comp_med_pay.sort(key=sorter) # Сортируем список по второму элементу каждого кортежа

comp_names = [n[0] for n in comp_med_pay] # Генерируем итоговый упорядоченный списко строк-названий компаний

with open('result.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(comp_names)) # Печатаем в файл результата построчно с переносом строки


