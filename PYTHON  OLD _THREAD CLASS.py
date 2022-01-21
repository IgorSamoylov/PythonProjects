import _thread

def test(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print("RESULT: ", result, sep="\n")
    #return result

_thread.start_new_thread(test, (200,))
_thread.start_new_thread(test, (400,))
