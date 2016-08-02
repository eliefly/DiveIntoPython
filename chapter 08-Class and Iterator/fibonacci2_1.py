class Fib:
    '''生成菲波拉稀数列的迭代器'''
    def __init__(self, max):
        self.max = max
        self.a = 0
        self.b = 1        

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a+self.b
        return fib


>>> fib = Fib(1000)
>>> 
>>> next(fib)
0
>>> next(fib)
1
>>> next(fib)
1
>>> iter(fib)
<__main__.Fib object at 0x02A05E50>
>>> next(fib)
2
>>> next(fib)
3