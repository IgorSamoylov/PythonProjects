# создание файла
myfile = open("hello.txt", "w")

# запись в файл
res = myfile.write("Hello friends, how are you?")
print(res, "bytes written to the file.")
# закрытие файла
myfile.close()

# чтение содержимого из файла
myfile = open("hello.txt", "r")
print("file content...")
print(myfile.read())

# устанавливает текущее местоположение файла на позицию 6 
print("file content from 6th position...")
myfile.seek(6)
print(myfile.read())

# устанавливает текущее местоположение файла на позицию 0
print("file content from 0th position...")
myfile.seek(0)
print(myfile.read())

# устанавливает текущее местоположение файла на позицию 12
print("file content from 12th position...")
myfile.seek(12)
print(myfile.read())
