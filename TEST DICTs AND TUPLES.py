
dictionary1 = {1:111, 2:222, 3:333, 4:444}
dictionary2 = {1:111, 2:222, 7:777, 8:888}

dictionary1.update(dictionary2)
print("Обновление элементов методом update() из другого словаря", dictionary1)
    

tuple1 = (dictionary1, dictionary2) #Кортеж может хранить словари

print(tuple1)

list1 = [dictionary1, dictionary2] #Список может хранить словари

print(list1)

#Множество не может хранить словари, потому они не имеют постоянного хэша
#set1 = {dictionary1, dictionary2} 

#print(set1)

dictionary1[5] = 555
#dictionary1.delete[5]

print(dictionary1)

Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}  
print(type(Employee))  
print("printing Employee data .... ")

name = Employee["Name"]
print(f"Name : {name}")

print("Age : ", Employee.get("Age"))

Employee.update({"salary" : 27500})

print("Salary : ", Employee["salary"])

del Employee["Company"] #Удаление элемента отдельной функцией del !

print(Employee)

for keys in Employee:
    print("Обычный iterable", keys, Employee[keys])

for keys, values in Employee.items(): #Метод dict.items() даёт кортежи содержимого ключ-значение
    print("С методом dict.items() ", keys, values)

print(Employee.pop("salary")) # Возврат элемента по ключу с удалением его из словаря pop()

print(Employee)
     
if "Age" in Employee.keys():  #Проверка вхождения переменной во все ключи
    print("Возраст указан ", Employee["Age"])

if 29 in Employee.values(): #Проверка вхождения переменной во все значения
    print("Значение Age составляет 29")

Iterator = iter(Employee)
while True:
    print(next(Iterator))

    
