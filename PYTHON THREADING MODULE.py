import threading

resultList = []

class TaskClass(threading.Thread):
    def __init__(self, n):
        threading.Thread.__init__(self)
        self.n = n
        print("Объект потока ", self.getName(), " создан!")
        
    def run(self):
        print("Поток ", self.getName(), " стартовал!")
        result = 1
        for i in range(1, self.n + 1):
            result *= i
        resultList.append(result)
        
        
# Создаём треды
taskClass1 = TaskClass(500)
taskClass2 = TaskClass(1500)

# Запускаем треды
taskClass1.start()
taskClass2.start()

#Присоединяем основной поток к тредам, ожидая их завершения
taskClass1.join()
taskClass2.join()

for result in resultList:
    print("RESULT: ", result, sep="\n")

print("Программа завершена!")
