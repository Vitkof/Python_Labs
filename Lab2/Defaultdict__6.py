
class recur_defd(dict):
    def __init__(self, func=None):
        super().__init__()
        self.default = func
        """"
        if func is int:
            self.__defvalue = 0            
        elif func is float:
            self.__defvalue = 0.0
        elif func is str:
            self.__defvalue = ''
        elif func is bool:
            self.__defvalue = False
        elif func is dict:
            self.__defvalue = {}
        elif func is list:
            self.__defvalue = []
        elif func is tuple:
            self.__defvalue = ()
        elif func is set:
            self.__defvalue = set()
            """
        if hasattr(func, '__call__'):
            self.__defvalue = func.__call__()
        else:
            raise TypeError("type object is not subscriptable")

        self.components = {}

    @property
    def defvalue(self):
        return self.__defvalue

    def __setitem__(self, key, value):
        self.components[key] = value

    def __getitem__(self, item):
        if item not in self.components.keys():
            self.components[item] = recur_defd(self.default)
            return self.components[item]
        else:
            return self.components[item]

    def get_recursive(self, item):
        items_found = []
        for k, v in iter(self.components.items()):
            if k == item:
                items_found.append(v)
            elif isinstance(v, dict):
                pass

    @staticmethod
    def str(dic):
        if isinstance(dic, recur_defd):
            dic = {k: recur_defd.str(v) for k, v in dic.components.items()}
        return dic

    def __str__(self):
        string = ''
        for k, v in self.components.items():
            if type(k) is str:
                k = "'{}'".format(k)
            if type(v) is str:
                v = "'{}'".format(v)
            if isinstance(v, recur_defd):
                string += f"{k}: {v.__str__()}, "  # вызываем рекурсивно вложенные словари
            else:
                string += f"{k}: {v}, "  # 'a': 'One'
        string = "{%s}" % string[:-2]
        return string

    """     # не корректен из-за вложенных recur_defd и наслаивающихся кавычках
            dic = {}
            for k, v in self.components.items():
                if isinstance(v, recur_defd):
                    v = v.__str__()
                    dic[k] = v
                else:
                    dic[k] = v
            return '{}'.format(dic)
"""
