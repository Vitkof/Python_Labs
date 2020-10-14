
class MyException(TypeError):
    def __init__(self, x):
        self.type = type(x)

    def __str__(self):
        return "Unknown_type: {}".format(self.type)


def to_json(obj, raise_unknown=False):
    if type(obj) is str:
        return "\"%s\"" % obj
    elif obj is None:
        return 'null'
    elif type(obj) is int or type(obj) is float:
        return obj
    elif type(obj) is bool:
        if obj == 1:
            return 'true'
        else:
            return 'false'
    elif type(obj) is list:
        out = ''
        id = 0
        for el in obj:
            obj[id] = to_json(el)
            out += '{}, '.format(obj[id])
            id += 1
        out = '[{}]'.format(out[:-2])
        return out
    elif type(obj) is dict:
        out = ''
        for k, v in obj.items():
            out += '\n\xa0"{}": {},'.format(k, to_json(v))  # Вложенные значения в парах k,v
            # не будут выбрасывать MyException
        out = '{%s\n}' % out[:-1]
        return out

    else:        # экз.пользовательских типов
        try:
            out = ''
            for k, v in obj.__dict__.items():  # если Error, то unknown_type
                out += "\n \"{}\": {},".format(str(k), to_json(v))
            out = '{%s\n}' % out[:-1]
            return out
        except AttributeError:
            if raise_unknown:
                try:
                    raise MyException(obj)
                except MyException as e:
                    return f"myJSON don't support {obj}! {e}"
            else:
                return ''
