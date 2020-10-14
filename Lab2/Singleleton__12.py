def singleton(myClass):
    instances = {}
    def getInstance(*args, **kwargs):
        if myClass not in instances:
            instances[myClass] = myClass(*args, **kwargs)
        return instances[myClass]
    return getInstance()


class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):  # обработку КВАРГ мб запилить??
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:  # если у класса экземпляра еще нет, то создать
            super().__call__(*args, **kwargs)
        return cls._instance  # возвращаем Одиночку(1экземпляр)


class Logger(metaclass=Singleton):
    pass
