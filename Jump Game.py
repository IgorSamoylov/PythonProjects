

data = [1,1,3,2,5,3,1,1,5,1,1,1,1,3]
length = len(data)

step_dict = {x: 2000 for x in range(len(data))}
step_dict[0] = data[0]

for i, st in enumerate(data):
    for j in range(1, st):
        if i + j < length:
            step_dict[i + j] = min(step_dict[i + j], step_dict[i] + 1)

    
   
print(step_dict)
