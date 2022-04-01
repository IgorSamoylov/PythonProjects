

# M - number of Vertexes, N - number of Edges
M, N = [int(x) for x in input().split()]
Graph = {}
for i in range(N):
    # input an Edges as a vertexes pairs, for example A B, A C
    v1, v2 = input().split()
    for v, u in (v1, v2), (v2, v1):
        if v not in Graph:
            Graph[v] = {u}
        else:
            Graph[v].add(u)

for vertex, adjacence_list in Graph.items():
    print(vertex, adjacence_list)
