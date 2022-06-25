from collections import deque
import json


def compute_chess_knight_desk():
    chess_knight_desk = {}
    
    letters = "abcdefgh"
    numbers = "12345678"
    for x in letters:
        for y in numbers:
            chess_knight_desk[x + y] = set()

    # Add direct and reversed path in set for each chess desk cell
    def add_edge(v1, v2):
        chess_knight_desk[v1].add(v2)
        chess_knight_desk[v2].add(v1)

    for x in range(8):
        for y in range(8):
            v1 = letters[x] + numbers[y] # Simple add start cell as each desk cell

            # Then computing existing chess knight pathes from it
            if 0 <= x + 2 < 8 and 0 <= y + 1 < 8:
                v2 = letters[x+2] + numbers[y+1]
                add_edge(v1, v2)
                
            if 0 <= x - 2 < 8 and 0 <= y + 1 < 8:
                v2 = letters[x-2] + numbers[y+1]
                add_edge(v1, v2)

            if 0 <= x + 1 < 8 and 0 <= y + 2 < 8:
                v2 = letters[x+1] + numbers[y+2]
                add_edge(v1, v2)

            if 0 <= x - 1 < 8 and 0 <= y + 2 < 8:
                v2 = letters[x-1] + numbers[y+2]
                add_edge(v1, v2)
                
    return chess_knight_desk
            

    
def search_knight_path_bfs(chess_knight_desk, start_cell, end_cell): 
    distances = { v: None for v in chess_knight_desk }
    parents = { v: None for v in chess_knight_desk }

    distances[start_cell] = 0
    queue = deque([start_cell])

    # Search distances to every chess cell from start cell by the knight
    # And adds shortest parent cell for each
    while queue:
        current_v = queue.popleft()
        for neigh_v in chess_knight_desk[current_v]:
            if distances[neigh_v] is None:
                distances[neigh_v] = distances[current_v] + 1
                parents[neigh_v] = current_v
                queue.append(neigh_v)
                
    # Restore path by parents list, starting with the end cell
    path = [end_cell]
    parent = parents[end_cell]
    while not parent is None:
        path.append(parent)
        parent = parents[parent]
        
    # Path is inverted, restore direct order
    return path[::-1]
   

def main():
    chess_knight_desk = None
    
    try:
        with open("RESOURCES/chess_knight_desk.json", "r", encoding="UTF=8") as f:
            input_json_dict = json.load(f)
            chess_knight_desk = { v: set(input_json_dict[v]) for v in input_json_dict }
    except Exception as ex:
        chess_knight_desk = compute_chess_knight_desk()
        with open("RESOURCES/chess_knight_desk.json", "w", encoding="UTF=8") as f:
            output_json_dict = { v: list(chess_knight_desk[v]) for v in chess_knight_desk }
            json.dump(output_json_dict, f)
        
    print(chess_knight_desk)
    print(search_knight_path_bfs(chess_knight_desk, "a1", "h8"))

if __name__ == '__main__':
    main()

"""
Заполнение графа в задаче с конем для приверженцев DRY:

for i in range(len(letters)):
    for j in range(len(numbers)):
        v1 = letters[i] + numbers[j]
        for i_modified, j_modified in (i+2, j+1), (i-2, j+1), (i+1, j+2), (i-1, j+2):
            if 0 <= i_modified < len(letters) and 0 <= j_modified < len(numbers):
                v2 = letters[i_modified] + numbers[j_modified]
                add_edge(v1, v2)

"""
"""
        if x + 2 < 8 and y + 1 < 8:
            chess_knight_desk[cols[x] + rows[y]].add(cols[x+2] + rows[y+1])
        if x + 1 < 8 and y + 2 < 8:
            chess_knight_desk[cols[x] + rows[y]].add(cols[x+1] + rows[y+2])
        if x - 2 >= 0 and y + 1 < 8:
            chess_knight_desk[cols[x] + rows[y]].add(cols[x-2] + rows[y+1])
        if x - 2 >= 0 and y - 1 >= 0:
            chess_knight_desk[cols[x] + rows[y]].add(cols[x-2] + rows[y-1])
        if x + 1 < 8 and y - 2 >= 0:
            chess_knight_desk[cols[x] + rows[y]].add(cols[x+1] + rows[y-2])
        if x - 1 >= 0 and y - 2 >= 0:
            chess_knight_desk[cols[x] + rows[y]].add(cols[x-1] + rows[y-2])
        if x - 1 >= 0 and y + 2 < 8:
            chess_knight_desk[cols[x] + rows[y]].add(cols[x-1] + rows[y+2])
        if x + 2 < 8 and y - 1 >= 0:
            chess_knight_desk[cols[x] + rows[y]].add(cols[x+1] + rows[y-2])
"""
