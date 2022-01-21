

def nod(p, q):
    if q == 0:
        return p
    r = p % q
    print(q, " ", r)
    return nod(q, r)


#print("Наибольший общий делитель: ", nod(1024, 225486688888))



def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

print(gcd(1000, 120))
