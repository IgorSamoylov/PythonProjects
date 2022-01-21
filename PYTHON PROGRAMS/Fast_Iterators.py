import time
#import itertools






s = []
new_iterator = iter (s)

def create_list() :
    s = [ 0 for i in range (0, 90_000_000)]

def main () :
    for i in range (0, 1000_000 - 1 ):
        s [i] = 1



def main_1 () :
    try:
        while True:           
            s[next(new_iterarator)] = 2
    except:
        pass


create_list()   

#start_time = time.time()
#main()
#print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
#main_1()
list(map(lambda x: x + 1, s))
print("--- %s seconds ---" % (time.time() - start_time))


    
