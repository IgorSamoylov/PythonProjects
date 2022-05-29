
G = { 1 : [2], 2 : [3], 3 : [5, 6], 4 : [6], 5 : [4], 6 : [] }

n = len(G)
visited = [False] * (n + 1)
ans = []

def dfs(start, G, visited, ans):
    visited[start] = True
    for vertex in G[start]:
        if not visited[vertex]:
            dfs(vertex, G, visited, ans)
    ans.append(start)



for i in range(1, n + 1):
    if not visited[i]:
        dfs(i, G, visited, ans)

ans = ans[::-1]

print(ans)
