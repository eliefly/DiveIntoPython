class Fib:
    '''生成菲波拉稀数列的迭代器'''
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a+self.b
        return fib


>>> fib = Fib(1000)
>>> next(fib)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    next(fib)
  File "<pyshell#64>", line 12, in __next__
    fib = self.a
AttributeError: 'Fib' object has no attribute 'a'
>>> iter(fib)
<__main__.Fib object at 0x02A17770>
>>> next(fib)
0
>>> next(fib)
1
>>> next(fib)
1
>>> iter(fib)
<__main__.Fib object at 0x02A17770>
>>> next(fib)
0
>>> next(fib)
1
>>> 