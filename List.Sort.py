
def sorter(n):
    return 11 - len(n)

list1 = ['hfh', 'hfghfgd', 'gfg', 'gdfgdfgdfg', 'f', 'ddddd', 'ddddd']

list1.sort(key=sorter)

print(list1)
