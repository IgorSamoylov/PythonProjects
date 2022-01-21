import collections

inp_file = open("TEST3.txt", "r", encoding="utf-8")
w_dict = collections.Counter(inp_file.read().split())
inp_file.close()

w_list = []
for word, freq in w_dict.items():
    w_list.append((freq, word))

def sorter_alf(tup):
    return tup[1]
    
def sorter_freq(tup):
    return tup[0]
    
w_list.sort(key=sorter_alf)
w_list.sort(key=sorter_freq, reverse=True)

out_str = ''
for tup in w_list:
    out_str += tup[1] + " "



out_file = open("RESULT.txt", "w", encoding="utf-8")
print(out_str, file=out_file)
out_file.close()


