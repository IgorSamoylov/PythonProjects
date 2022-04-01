import numpy as np

vertex_n = 5
adjacence_list = np.array([1,0,2,3,1,3,1,2,4,3])
offset_list = np.array([0,1,4,6,9,10])

for i in range(vertex_n):
    print(i, adjacence_list[offset_list[i] : offset_list[i+1]])
