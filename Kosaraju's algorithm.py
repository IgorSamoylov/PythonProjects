""" Kosaraju's Algorithm for finding strongly connected components """

from collections import deque

G = {'A' : {'B', 'C'}, 'B' : {'D', 'E'}, 'C' : {'A'}, 'D' : {}, 'E' : {'F', 'C'},
     'F' : {'G'}, 'G' : {'H'}, 'H' : {'F'}}

visited = set()
visited_stack = deque()
components = {}

def dfs(vertex: str):
    visited.add(vertex)
    for neighbour in G[vertex]:
        if neighbour not in visited:
            dfs(neighbour)

    visited_stack.append(vertex)

def find_reverse_neighbours(vertex: str) -> set:
    result = set()
    for v, neighbours in G.items():
        if vertex in neighbours:
            result.add(v)
    return result

def assign(vertex: str, root: str):
    if vertex not in components:
        if root not in components:     
            components[root] = set()
        else:
            components[root].add(vertex)
        for v in find_reverse_neighbours(vertex):
            assign(v, root)


def main(root: str):
    dfs(root)               
    while len(visited_stack) > 0:
        vertex = visited_stack.pop()
        assign(vertex, vertex)
    print(components)


main('A')

        
