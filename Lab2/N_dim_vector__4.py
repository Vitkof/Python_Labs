from math import sqrt


class N_vector:
    def __init__(self, *args):
        if type(args[0]) == list or type(args[0]) == tuple:
            for el in args[0]:
                if type(el) != int and type(el) != float:
                    raise TypeError("List/Tuple не может содержать argument типа {}".format(type(el)))
            self.components = args[0]
        else:
            for el in args:
                if type(el) != int and type(el) != float:
                    raise TypeError("Argument не межет быть {}".format(type(el)))
            self.components = args

    def __repr__(self):
        return "({})".format(str(self.components)[1:-1])

    def __str__(self):
        return '({0})'.format(str(self.components)[1:-1])

    def __eq__(self, other):
        return True if (self.components == other.components) else False

    def __ne__(self, other):
        return True if (self.components != other.components) else False

    #def __str__(self):
     #   return str(self.components)

    def addition(self, vector):
        res = []
        for i in range(len(self.components)):
            res.append(self.components[i]+vector.components[i])
        return N_vector(tuple(res))

    def subtraction(self, vector):
        res = []
        for i in range(len(self.components)):
            res.append(self.components[i]-vector.components[i])
        return N_vector(tuple(res))

    def multiplication(self, const):
        res = []
        for i in range(len(self.components)):
            res.append(self.components[i] * const)
        return N_vector(tuple(res))

    def scalar(self, vector):
        res = 0
        for i in range(len(self.components)):
            res += self.components[i] * vector.components[i]
        return res

    def length(self):
        res = 0
        for i in range(len(self.components)):
            res += self.components[i] ** 2
        return sqrt(res)

    def get_item(self, index):
        return self.components[index]

    def equality(self, vector):
        res = True
        for i in range(len(self.components)):
            if self.components[i] != vector.components[i]:
                res = False
                break
        return res

    def tostring(self):
        res = '<'
        for i in range(len(self.components)):
            res += str(self.components[i])+" "
        res = res[:-1] + '>'
        return res

