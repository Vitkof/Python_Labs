class StringField(object):
    def __init__(self):
        self.name = None
        self.default = None

    def __set__(self, instance, value):
        if isinstance(value, str):
            setattr(instance, self.name, value)
        else:
            raise TypeError("В текст. поле нельзя вписать {}".format(type(value)))

    def __get__(self, instance, owner):
        return getattr(instance, self.name, self.default)


class ModelCreator(type):
    # mcs – объект метакласса, <__main__.ModelCreator>
    # cls – созданный класс,   <__main__.Student>
    def __new__(mcs, name, bases, attrs):
        socket = set()
        # наследование классов
        for base in bases:
            if hasattr(base, '__slots__'):
                socket.update(base.__slots__)  # __slots__, а не __dict__
        for key, val in iter(attrs.items()):
            if isinstance(val, StringField):
                val.name = "_{}".format(key)
                socket.add(val.name)

        def __new__(cls, **kwargs):
            # Рабочий __new__ метод, поддерживающий наследование
            for parent in cls.__mro__[1:]:
                if '__new__' in parent.__dict__:
                    instance = object.__new__(cls)
                    break  # последний класс в __mro__ является object, который всегда имеет '__new__'

            for names in kwargs:
                if '_{}'.format(names) in cls.__slots__:
                    setattr(instance, names, kwargs[names])
            return instance

        attrs["__slots__"] = list(socket)  # __dict__, __weakref__ для экзем. не будут созданы
        attrs["__new__"] = __new__
        return super().__new__(mcs, name, bases, attrs)


class Student(metaclass=ModelCreator):
    name = StringField()
    surname = StringField()


class Login(Student):
    nick_name = StringField()


def main():
    st = Student(name="Oleg", surname="Ivanov")
    print(st.name, st.surname)  # Oleg Ivanov

    my = Login(name="Victor", nick_name="Vitkof")
    print(my.name, my.nick_name)  # Victor Vitkof
    print(my.__slots__)  # ['_surname', '_name', '_nick_name']


if __name__ == '__main__':
    main()
