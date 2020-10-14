import time
import unittest
from My_xrange__9 import xrange


class TestXrange(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass\n=======")

    @classmethod
    def tearDownClass(cls) -> None:
        print("=======\ntearDownClass")

    def setUp(self) -> None:
        self.xr1 = xrange(7, 20, 4)
        self.xr2 = xrange(6, 10)
        self.xr3 = xrange(15000)
        self.t0 = time.time()
        super(TestXrange, self).setUp()

    def tearDown(self) -> None:
        t1 = time.time() - self.t0
        print(t1)
        print('End of "%s"' % self._testMethodName)
        del self.xr1, self.xr2, self.xr3, self.t0

    def test_first(self):
        self.assertEqual(self.xr1.first, 7, "Error First!")
        self.assertTrue(self.xr2.first == 6, "Err First xr2")
        self.assertEqual(self.xr3.first, 0, "Err First xr3")
        with self.assertRaises(ValueError):
            xrange(10, 1)

    def test_last(self):
        self.assertTrue(self.xr1.last == 20, 'Not number 48?')
        self.assertEqual(self.xr2.last, 10, 'xr2.last != 10')
        self.assertNotEqual(self.xr3.last, 14999, 'xrange(15000).last = 14999')

    def test_step(self):
        self.assertTrue(self.xr1.step == 4, 'xr1.step != 1')
        self.assertEqual(self.xr3.step, 1, 'xrange(15).step != 1')

    def test_elem(self):
        self.assertEqual(self.xr1.elem, [7, 11, 15, 19], 'No match')
        self.assertTrue(self.xr2.elem == [6, 7, 8, 9], 'No match')
        self.assertIs(self.xr3.elem, self.xr3._xrange__elem, 'assertNotIs _xrange__elem')  # частно скрытый

    def test__reversed_(self):
        self.assertEqual(reversed(self.xr1), [19, 15, 11, 7], "don't work __reversed__")
        self.assertTrue(reversed(self.xr2) == [9, 8, 7, 6], "don't work __reversed__")

    def test__len_(self):
        self.assertTrue(len(self.xr2) == 4, "__LEN__ warning")
        self.assertTrue(len(self.xr3) == 15000, 'len(xrange(15000)) != 15000')

    def test__getitem_(self):
        self.assertTrue(self.xr1[1] == 11, "ind не тот")
        self.assertTrue(self.xr2[2] == 8, "ind не тот")
        self.assertTrue(self.xr3[4444] == 4444, "ind не тот")
        self.assertIs(self.xr1[0], self.xr1.elem[0])
        self.assertIs(self.xr3[555], self.xr3.elem[555])

    def test_count(self):
        self.assertTrue(self.xr3.count(7777) == 1, "count(7) in xrange(15000) != 1")
        self.assertNotEqual(self.xr1.count(8) == 1, 'count(8) in xrange(7, 20, 4)')

    def test_index(self):
        self.assertTrue(self.xr3.index(14999) == 14999, 'индекс не верен')
        self.assertEqual(self.xr1.index(11), 1, 'проверь индекс')
        with self.assertRaises(ValueError):
            self.xr2.index(-5)

    def test__string_(self):
        self.assertEqual(str(self.xr1), "xrange(7, 20, 4)", 'check __repr__')
        self.assertEqual(str(self.xr2), "xrange(6, 10, 1)", 'check __repr__')
        self.assertEqual(str(self.xr3), "xrange(0, 15000, 1)", 'check __repr__')

    def test__next_(self):
        itr = iter(self.xr3)
        self.assertEqual(next(itr), 0, 'next(iter(xrange(15000)_1 != 0')
        self.assertEqual(next(itr), 1, 'next_2 != 1')
        self.assertEqual(next(itr), 2, 'next_3 != 2')


if __name__ == "__main__":
    unittest.main()
