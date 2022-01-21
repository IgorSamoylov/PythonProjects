

def test_TrueTest():
    assert True

def test_FalseTest():
    assert False

test_TrueTest()
#test_FalseTest()

a = 0
for i in range(100):
    a = i

assert a == 99
assert a == 100
assert a == 98 #Программа выполняется только до первого несработавшего assert'a

