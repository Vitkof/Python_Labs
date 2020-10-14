import unittest
from JSON__3_11 import to_json, MyException


class Foo(object):
    def __init__(self, name, age, isAdmin, powers='none'):
        self.name = name
        self.age = age
        self.isAdmin = isAdmin
        self.powers = powers


class ToJSON(unittest.TestCase):

    def setUp(self) -> None:
        self.foo = Foo('Spartak', 30, True, ['Radioaktive', 'Turning tiny', 'Bandzai'])
        self.num = 151515
        self.float = 1/8
        self.str = 'stroka'
        self.bool = False
        self.lst = ['London', 'Paris', 3, True, 'Berlin']
        self.dct = {"president": {"name": "Arnold Swartznegger", "place": "LA"},
                    "vice-president": {"name": "Donald Trump", "place": "NY"}}
        self.compl = complex(2, 3)
        self.listDuplication = {13, 13, 13}
        self.set = set()

    def tearDown(self) -> None:
        del self.foo

    def test_simpleType(self):
        self.assertEqual(to_json(self.num), 151515, "Неправильное JSON-преобразование")
        self.assertEqual(to_json(self.float), 0.125, "Неправильное JSON-преобразование")
        self.assertEqual(to_json(self.str), '"stroka"', "Неправильное JSON-преобразование")
        self.assertEqual(to_json(self.bool), 'false', "Неправильное JSON-преобразование")

    def test_listType(self):
        self.assertEqual(to_json(self.lst), '["London", "Paris", 3, true, "Berlin"]', "Неправильное преобразование")
        self.assertEqual(to_json(self.dct), '{\n\xa0"president": {\n "name": "Arnold Swartznegger",\n "place": "LA"\n},'
                                            '\n\xa0"vice-president": {\n "name": "Donald Trump",\n "place": "NY"\n}\n}',
                                            "Где-то неправильно!")

    def test_customType(self):
        self.assertEqual(to_json(self.foo), '{\n "name": "Spartak",\n "age": 30,\n "isAdmin": true,\n "powers": ['
                                            '"Radioaktive", "Turning tiny", "Bandzai"]\n}', "NE SOVPALO!")

    def test_MyException(self):
        self.assertNotEqual(to_json(self.compl, raise_unknown=True), '', "Почему-то не выбросило MyException!")
        self.assertRaises(TypeError, to_json(self.set, raise_unknown=True), "Don't TypeError")
        self.assertTrue(to_json(self.compl) == '', "Фун-я не вернула ''!")
        self.assertEqual(to_json(self.listDuplication, raise_unknown=True), 'myJSON don\'t support {13}! '
                                                                            'Unknown_type: <class \'set\'>', "No")


if __name__ == "__main__":
    unittest.main()
