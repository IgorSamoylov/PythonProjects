import time

class QuickUnionUF:
    def __init__(self, N: int):
        self._id = [i for i in range(N)] # id[i] = parent of i
        self._count = N # number of components
        self.N = N

    def count(self):
        return self._count

    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

    # Wrong variant of a union function
    def union_wrong(self, p: int, q: int):
        if self.connected(p, q):
            return
        for i in range(self.N):
            if self._id[i] == self._id[p]:
                self._id[i] == self._id[q]
       
        self._count -= 1

    # 1 Variant, without find function calls
    def union_fast_search(self, p: int, q: int):
        p_id = self._id[p]
        q_id = self._id[q]

        if p_id == q_id:
            return

        for i in range(self.N):
            if self._id[i] == p_id:
                self._id[i] = q_id
                
        self._count -=1
        
    def find(self, p: int) -> int:
        k = p
        while p != self._id[p]:
            p = self._id[p]
        # Сжатие пути
        while k != self._id[k]:
            i = k
            k = self._id[k]
            self._id[i] = p
        return p
    
    # 2 Variant
    def union_fast_union(self, p: int, q: int):
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root == q_root:
            return

        self._id[p_root] = q_root
                    
        self._count -=1

    def print_array(self):
        print(self._id)


with open("UnionData/largestUF.txt", "r", encoding="UTF-8") as file:
    N = int(file.readline())
    quuf = QuickUnionUF(N)
    start = time.time()
    for line in file:
        p, q = map(int, line.split(" "))
        #print(f"p {p}, q {q}")
        quuf.union_fast_search(p, q)
        #quuf.print_array()
    stop = time.time()

print(f"Find components: {quuf.count()}. Time: {stop-start}")
