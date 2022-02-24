class Tst:

    def __init__(self):
        self._a = 1

    @property
    def a(self):
        print('hahaha')
        return self._a


if __name__ == '__main__':

    tst = Tst()
    print('{0.a}'.format(tst))
