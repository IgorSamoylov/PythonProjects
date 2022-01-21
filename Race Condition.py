
x = 0
stop = False

class RC:    
    
    @staticmethod
    def incrementer():
        global x
        while not stop:
            x += 1
    @staticmethod
    def check_odd():
        while not stop:
            if x % 2 == 0:
                print(x)

import threading
import time

threading.Thread(target=RC.incrementer).start()
threading.Thread(target=RC.check_odd).start()

time.sleep(1)
RC.stop = True


