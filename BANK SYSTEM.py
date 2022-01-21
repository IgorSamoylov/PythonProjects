clients = {}

def deposit(name, money):
    if not name in clients:
        clients[name] = 0
    clients[name] += money
    
def withdraw(name, money):
    if not name in clients:
        clients[name] = 0
    money = int(money)
    clients[name] -= money

def balance(name):
    if not name in clients:
        print("ERROR")
    else:
        print(clients[name])

def transfer(name1, name2, money):
    if not name1 in clients:
        clients[name1] = 0
    if not name2 in clients:
        clients[name2] = 0
    money = int(money)
    clients[name1] -= money
    clients[name2] += money

def income(procent):
    for client, summ in clients.items():
        if summ > 0:
            summ += int(summ * procent / 100) 

#functions = {"DEPOSIT" : deposit, "WITHDRAW" : withdraw,
#             "BALANCE" : balance}


n = int(input())
for i in range(n):
    q = input().split()
    if len(q) < 2 or len(q) > 4:
        print("ERROR")
    comm = q[0]
    if comm == "DEPOSIT":
        deposit(q[1], int(q[2]))
    elif comm == "WITHDRAW":
        withdraw(q[1], int(q[2]))
    elif comm == "BALANCE":
        balance(q[1])
    elif comm == "TRANSFER":
        transfer(q[1], q[2], int(q[3]))
    elif comm == "INCOME":
        income(int(q[1]))
    else:
        print("ERROR")
    
    
