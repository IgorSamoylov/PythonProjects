import threading
from queue import Queue
 
 
def creator(data, queue):
    """
    Creates data to be consumed and waits for the consumer
    to finish processing
    """
    print('Creating data and putting it on the queue')
    for item in data:
        evt = threading.Event()
        queue.put((item, evt))
        print('Waiting for data to be doubled')
        evt.wait()
 
 
def my_consumer(queue):
    """
    Consumes some data and works on it
    In this case, all it does is double the input
    """
    while True:
        data, evt = queue.get()
        print(f'data found to be processed: {data}')
        processed = data * 2
 
        print(f'Processed: {processed}')
 
        evt.set()  # Используется event.set(), вместо notify
        queue.task_done() # Уведомление queue о завершении
 
 
if __name__ == '__main__':
    q = Queue()
    data = [5, 10, 13, -1]
    thread_one = threading.Thread(target=creator, args=(data, q))
    thread_two = threading.Thread(target=my_consumer, args=(q,))
    
    thread_one.start()
    thread_two.start()
    
    q.join()

    print("All works completed!")
