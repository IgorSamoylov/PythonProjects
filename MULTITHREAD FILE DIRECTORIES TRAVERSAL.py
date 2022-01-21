import threading
import os
import time

list_of_files = []
locker = threading.Lock() # lock для правильного вывода сообщений потоков в консоли

class TreeTraversal(threading.Thread):
    def __init__(self, path):
        threading.Thread.__init__(self)
        
        locker.acquire()
        print("Стартовал поток ", threading.get_ident())
        locker.release()
        
        self.path = path
        
    def run(self):
        with os.scandir(self.path) as dir_itr:
            for file in dir_itr:
                if file.is_dir():
                    new_thread = TreeTraversal(file)
                    new_thread.start()
                else:
                    #print(file.name)
                    list_of_files.append(file.name)


path = input("Введите директорию")
traversal = TreeTraversal(path)
traversal.start()

while threading.active_count() > 2:
    locker.acquire()
    print("Активно потоков ", threading.active_count())
    locker.release()
    time.sleep(0.1)
    
for n, file_name in enumerate(list_of_files):
    print(n + 1, " ", file_name)

            
