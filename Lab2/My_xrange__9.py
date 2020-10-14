class xrange:
    def __init__(self, *args):
        if len(args) == 1:
            if args[0] > 0:  # >0 потому что range(0) - error
                self.__last = args[0]
                self.__first = 0
                self.__step = 1
            else:
                raise ValueError

        elif len(args) == 2:
            if args[0] < args[1]:  # range(10, 1), range(10, 10) - error
                self.__first, self.__last = args[0], args[1]
                self.__step = 1
            else:
                raise ValueError

        elif len(args) == 3:
            bool_normal = args[0] < args[1] and args[2] > 0  # обычный range(1, 10, 2) first < last, step > 0
            bool_back = args[0] > args[1] and args[2] < 0  # обратный range(10, -1, 2) first > last, step < 0
            if bool_normal or bool_back:
                self.__first, self.__last, self.__step = args[0], args[1], args[2]
            else:
                raise ValueError
        self.__elem = []
        i = self.first
        while i < self.last:
            self.__elem.append(i)
            i += self.step

    @property
    def first(self):
        return self.__first

    @property
    def last(self):
        return self.__last

    @property
    def step(self):
        return self.__step

    @property
    def elem(self):
        return self.__elem

    def __iter__(self):
        self.curr_index = -1  # ставим указатель перед 1-м элементом
        return self

    def __next__(self):
        self.curr_index += 1
        if self.curr_index == len(self.elem):
            raise StopIteration
        return self.elem[self.curr_index]

    def __repr__(self):
        return "xrange(%s, %s, %s)" % (self.first, self.last, self.step)

    def __getitem__(self, ind):
        return self.elem[ind]

    def __len__(self):
        return len(self.elem)

    def __reversed__(self):
        return self.elem[::-1]

    def count(self, val):
        for el in self.elem:
            if el == val:
                return 1
        return 0

    def index(self, val):
        i = 0
        for el in self.elem:
            if el == val:
                return i
            i += 1
        raise ValueError("{} is not in xrange".format(val))

