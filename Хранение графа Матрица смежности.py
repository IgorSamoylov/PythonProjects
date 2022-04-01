
# M - number of Vertexes, N - number of Edges
M, N = [int(x) for x in input().split()]
A = [[0] * M for i in range(M)]
index = {}
Vertexes = []

for i in range(N):
    # input an Edges as a vertexes pairs, for example A B, A C 
    v1, v2 = input().split()
    for v in v1, v2:
        if v not in index:
            Vertexes.append(v)
            index[v] = len(Vertexes) - 1
    v1_i = index[v1]
    v2_i = index[v2]
    A[v1_i][v2_i] = 1
    A[v2_i][v1_i] = 1

for row in A:
    print(row)
        
    
