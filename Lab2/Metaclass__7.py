import re


class Creator(type):
    def __new__(mcs, name, bases, dct, **extra_kwargs):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        uppercase_attr.update(mcs.readattrs(extra_kwargs['path']))
        print(uppercase_attr)

        return type.__new__(mcs, name, bases, uppercase_attr)

    @staticmethod
    def readattrs(path):
        with open(path, 'r') as f:
            dic = {}
            while True:
                row = f.readline()
                if len(row) == 0:
                    break
                row = list(filter(None, re.split("[=:]", row)))
                try:
                    name = row[0].strip()
                    value = row[1].strip()
                except IndexError:
                    dic[name] = None
                    continue
                try:
                    value = int(value)
                except ValueError:
                    continue
                finally:
                    dic[name] = value
            return dic


class Vehicle(metaclass=Creator, path='metaclass_attrs.txt'):
    pass


class Star(metaclass=Creator, path='star_attrs.txt'):
    pass
