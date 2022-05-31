

class WeightedQuickUnionUF:
    def __init__(self, N: int):
        self._id = [i for i in range(N)] # id[i] = parent of i
        self._sz = [i for i in range(N)] # sz[i] = number of objects in subtree rooted at i
        self._count = N # number of components

    def count(self):
        return self._count

    def find(self, p: int) -> int:
        while p != self._id[p]:
            p = self._id[p]
        return p

    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

    def union(self, p: int, q: int):
        i = self.find(p)
        j = self.find(q)
        if  i == j:
            return
        
        if self._sz[i] < self._sz[j]:
            self._id[i] = j
            self._sz[j] += self._sz[i]
        else:
            self._id[j] = i
            self._sz[i] += self._sz[j]
            
        self._count -= 1


with open("UnionData/mediumUF.txt", "r", encoding="UTF-8") as file:
    N = int(file.readline())
    wquuf = WeightedQuickUnionUF(N)
    for line in file:
        p, q = map(int, line.split(" "))
        #print(p, q)
        wquuf.union(p, q)

print(f"Find components: {wquuf.count()}")

    

    
