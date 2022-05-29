
def dfs(vertex, G, used): 
    used.add(vertex)
    for neighbour in G[vertex]:
        if neighbour not in used:
            dfs(neighbour, G, used)


G = {'A' : ['B', 'C'], 'B' : ['A', 'D'], 'C' : ['A'], 'D' : ['B'], 'E' : ['F'], 'F' : ['E']}

# Подсчет количества компонент связности в графе с использованием DFS
used = set()
N = 0
for vertex in G:
    if vertex not in used:
        dfs(vertex, G, used)
        N += 1

print('Количество компонент связности в графе:', N)    

    
