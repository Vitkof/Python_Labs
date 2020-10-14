import unittest
from Defaultdict__6 import recur_defd


class TestDefaultDict(unittest.TestCase):
    def setUp(self) -> None:
        self.rdd = recur_defd(int)

    def test_init(self):
        self.assertTrue(recur_defd(bool).default == bool, 'self.default Err')
        self.assertTrue(recur_defd(float).defvalue == 0.0, 'self.defvalue Err')
        self.assertTrue(recur_defd(lambda: 333).defvalue == 333, 'self.defvalue Err')
        with self.assertRaises(TypeError):
            recur_defd(complex(2, 5))

    def test_setitem(self):
        self.rdd['a'] = 9
        self.assertTrue(self.rdd['a'] == 9, 'self.rdd[a] != 9')
        self.rdd['b'] = 'two'
        self.assertTrue(self.rdd.components['b'] == 'two', "rdd[b]!='two'")
        self.rdd['c']['d'] = 'CD'
        self.assertTrue(self.rdd['c']['d'] == 'CD', 'rdd[c][d]!=CD ')
        self.assertEqual(self.rdd.components['c'].components['d'], 'CD')
        with self.assertRaises(TypeError):
            self.rdd.__setitem__('f')

    def test_getiten(self):
        self.rdd['a']['b']
        self.assertTrue(self.rdd['a'] == recur_defd(int))
        self.assertTrue('b' in self.rdd['a'].components.keys(), "'b' не в ключах")
        with self.assertRaises(TypeError):
            self.rdd.__getitem__()

    def test_magicMethodStr(self):
        self.rdd['a']['b']
        self.rdd['c']['d'][1] = 100
        self.rdd['c']['d'][2] = 200
        print(str(self.rdd))
        self.assertEqual(self.rdd.__str__(), "{'a': {'b': {}}, 'c': {'d': {1: 100, 2: 200}}}")

    def test_staticStr(self):
        self.rdd['a']['b']
        self.rdd['c']['d'][1] = 100
        self.rdd['c']['d'][2] = 200
        print(str(self.rdd))
        self.assertEqual(recur_defd.str(self.rdd), {'a': {'b': {}}, 'c': {'d': {1: 100, 2: 200}}})

    def tearDown(self) -> None:
        del self.rdd


suite = unittest.TestLoader().loadTestsFromTestCase(TestDefaultDict)
unittest.TextTestRunner(verbosity=2).run(suite)
