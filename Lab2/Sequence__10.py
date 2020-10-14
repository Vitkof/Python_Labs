from itertools import zip_longest
from memory_profiler import profile
import random


class Sequence:   # class ListIterator(Iterator):
    def __init__(self, items):  # items - произвольный iterable объект.
        self._items = list(items)  # локальная копия предотвращает изменение списка
        self.id = len(self._items)
        random.shuffle(self._items)

    def __getitem__(self, c):
        return self._items[c]

    def __repr__(self):
        return "%s" % list(self._items)

    def __iter__(self):
        self.pos = -1
        return self

    def __next__(self):  # он же и CurrentItem
        x = self
        if self.pos+1 >= self.id:
            self.pos = -1
            raise StopIteration
        self.pos += 1
        return x[self.pos]

    def __add__(self, other):
        self.id += 1
        self._items.append(other)

    def pick(self):
        try:
            self.id -= 1
            return self._items.pop()
        except IndexError:
            raise LookupError('Выбор из пустой Sequence')

    def grouper(self, n, fillvalue=None):
        args = [iter(self._items)] * n
        return list(zip_longest(*args, fillvalue=fillvalue))

    @staticmethod
    def only_numbers(x):
        if type(x) == int or type(x) == float or type(x) == complex:
            return 1
        elif type(x) is type(str):
            for ch in x:
                if '0' <= ch <= '9':
                    continue
                else:
                    return 0
            return 1
        else:
            return 0

    @staticmethod
    def isPrime(n):
        try:
            if type(n) is bool or type(n) is float:
                raise TypeError
            n = int(n)
        except Exception:
            return 0
        if n % 2 == 0:  # отсекаем все четные,
            return n == 2  # кроме 2
        d = 3
        while d * d <= n and n % d != 0:  # сложность алгоритма O(sqrt(n))
            d += 2
        return d * d > n

    @profile(precision=5)
    def filtr(self, function, iterable):
        for item in iterable:
            if function(item):
                yield item
                del item

    def filtrPrime(self):
        result = Sequence([])
        for val in self.filtr(Sequence.isPrime, self):
            result.__add__(val)
        return result

    def filtrNumber(self):
        res = Sequence([])
        for val in self.filtr(Sequence.only_numbers, self):
            res.__add__(val)
        return res
