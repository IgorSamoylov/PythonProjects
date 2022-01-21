

N = [x for x in range(5)]

def shift_left(N: list):
    tmp = N[0]
    for i in range(len(N) - 1):
        N[i] = N[i + 1]
    N[-1] = tmp

#shift_left(N)
#shift_left(N)
print(N)


def shift_right(N: list):
    tmp = N[-1]
    for i in range(len(N) - 2, -1, -1):
        N[i + 1] = N[i]
    N[0] = tmp

shift_right(N)
print(N)
