import collections

a = [1,2,3,2,0]
b = [5,1,2,7,3,2]

c = set(a).intersection(set(b))


for item in c:
    occurs = min(a.count(item), b.count(item))
    
output =[]
for i in a:
    for k in b:
        if i == k:
            output.append(i)
            
print(output)



def common_elements(a, b):
  b_dict = collections.defaultdict(int)  # defaultdict
  
  for el in b:
      b_dict[el] += 1  # я считаю все элементы из b, т.е. типа collections.Counter

  result = []

  for el in a:
      count = b_dict[el]
      if count > 0:  # если какой-то элемент из a встречается в b
          result.append(el)  # то это успех
          b_dict[el] -= 1  # и я "вынимаю" его из b, т.е. уменьшаю его количество на 1

  return result

print(common_elements(a, b))



string = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'

def RLE(string) -> str:
    if not string:
        raise "Input string is null!"
    
    output = []
    current_letter = ''
    counter = 1 
    for letter in string:
        
        if letter == current_letter:
            counter += 1
        elif counter > 1:
            output.append(str(counter))
            counter = 1  
        if counter == 1:
                current_letter = letter

        output.append(letter)
       
    if counter > 1:
            output.append(str(counter))
                          
    outputStr = ''.join(output)
    return outputStr

print(RLE(string))


#test = [0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1]
test = [1, 1 , 0, 1, 0 , 1, 0, 1, 1, 1]

def max_ones_length(inputList):
    if not  isinstance(inputList, list):
        raise 'Wrong input data!'
    #if len(inputList) == 1:
     #   return inputList[0]

    ones_groups = []
    counter = 0
    first_elem = 1
    for i, item in enumerate(inputList):
           
        if item == 1:
            counter += 1
            first_elem = i if first_elem == 1 else first_elem
        elif counter > 0:
            ones_groups.append((first_elem, i - 1))
            counter = 0
            first_elem = 1
        
    if counter > 0:
        ones_groups.append((first_elem, len(inputList) - 1))

    print(ones_groups)
    
    max_merge = 0
    for i in range(len(ones_groups) - 1):
        if ones_groups[i + 1][0] - ones_groups[i][1] == 2:
            length_merge_ones = ones_groups[i + 1][1] - ones_groups[i][0]
            max_merge = max(max_merge, length_merge_ones)

    max_single = 0
    for group in ones_groups:
        length_group = group[1] - group[0]
        max_single = max(max_single, length_group)
    print(max_merge, "  ", max_single)
    return max(max_merge, max_single, 0)
        


print(max_ones_length(test))

