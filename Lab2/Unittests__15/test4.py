import unittest
from N_dim_vector__4 import N_vector
from math import sqrt


class TestVectorMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass\n=======")

    @classmethod
    def tearDownClass(cls) -> None:
        print("=======\ntearDownClass")

    def setUp(self) -> None:
        self.a = N_vector(5, 0, 1)
        self.b = N_vector(1, 2, 8)
        self.c = N_vector(3, 4, 0)

    def tearDown(self) -> None:
        del self.a, self.b, self.c

    #def testInsufficientArgs(self):
        #args = 0
        #self.failUnlessRaises(ValueError, N_vector, args)

    def test_init(self):
        self.assertEqual(self.a.components, (5, 0, 1))
        self.assertEqual(self.b.components, (1, 2, 8))
        self.assertEqual(self.c.components, (3, 4, 0))

    def testArgs(self):
        with self.assertRaises(TypeError):
            N_vector([1, 'dva', 3])
        with self.assertRaises(TypeError):
            N_vector(1, 2, 3.14, True)
        with self.assertRaises(IndexError):
            N_vector()

    def testAssertTrue(self):
        self.assertTrue(True)

    def test_str(self):
        self.assertTrue(str(self.a) == "(5, 0, 1)", "Неправильный вывод")

    def test_addition(self):
        self.assertEqual(self.a.addition(self.b), N_vector(6, 2, 9), "Неправильное сложение!")
        self.assertEqual(self.a.addition(self.c), N_vector(8, 4, 1), "Неправильное сложение!")
        self.assertEqual(self.b.addition(self.c), N_vector(4, 6, 8), "Неправильное сложение!")

    def test_subtraction(self):
        self.assertEqual(self.b.subtraction(self.c).components, N_vector(-2, -2, 8).components, "Неправильное вычитание!")
        self.assertEqual(self.a.subtraction(self.c).components, N_vector(2, -4, 1).components, "Неправильное вычитание!")

    def test_multiplication(self):
        self.assertEqual(self.a.multiplication(3), N_vector(15, 0, 3), "Неправильное умножение!")
        self.assertEqual(self.b.multiplication(5), N_vector(5, 10, 40), "Неправильное умножение!")
        self.assertEqual(self.c.multiplication(10), N_vector(30, 40, 0), "Неправильное умножение!")

    def test_scalar(self):
        self.assertTrue(self.a.scalar(self.b) == 13, "Неправильное скалярное произведение!")
        self.assertTrue(self.a.scalar(self.c) == 15, "Неправильное скалярное произведение!")
        self.assertTrue(self.b.scalar(self.c) == 11, "Неправильное скалярное произведение!")

    def test_length(self):
        self.assertEqual(self.c.length(), 5, "Неправильное вычисление длины!")
        self.assertEqual(self.a.length(), sqrt(25+1), "Неправильное вычисление длины!")
        self.assertEqual(self.b.length(), sqrt(5+64), "Неправильное вычисление длины!")

    def test_equality(self):
        self.assertFalse(self.a.equality(self.b), "Неправильное сравнение на равенство!")
        self.assertTrue(self.a.equality(N_vector(5, 0, 1)), "Неправильное сравнение на равенство!")
        self.assertEqual(self.b.equality(self.c), False, "Неправильное сравнение на равенство!")

    def test_getitem(self):
        self.assertEqual(self.a.get_item(0), 5, "Неправильное получение элемента по индексу")
        self.assertEqual(self.b.get_item(2), 8, "Неправильное получение элемента по индексу")
        self.assertIs(self.c.get_item(1), self.c.components[1], "Неправильное получение элемента по индексу")

    def test_tostring(self):
        self.assertTrue(self.b.tostring() == "<1 2 8>", "Неправильное строковое представление")
        self.assertEqual(self.c.tostring(), "<3 4 0>", "Неправильное строковое представление")


if __name__ == "__main__":
    unittest.main()
