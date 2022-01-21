import threading

class TaskClass(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        threadLock.acquire()
        print("Поток ", self.getName(), " стартовал!")
        threadLock.release()


# Создаём объект блокировки посредством метода threading.Lock() в глобальной области
threadLock = threading.Lock()

taskPool = []
for i in range(4):
    taskPool.append(TaskClass())

for task in taskPool:
    task.start()

for task in taskPool:
    task.join()

# Новые вспомогательные функции Python
help(threading.Thread)
breakpoint()
