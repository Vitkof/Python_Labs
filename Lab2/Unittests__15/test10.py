import unittest
import time
from Sequence__10 import Sequence


class TestSequence(unittest.TestCase):
    def setUp(self) -> None:
        self.t0 = time.time()
        self.seq = Sequence([17, '54fg3', complex(2, 5), 33, 2, 'slonim5'])
        self.seq2 = Sequence([29, True, 2.71, 'Exponent'])
        self.seq3 = Sequence(range(25))

    def tearDown(self) -> None:
        t1 = time.time()-self.t0
        print(t1, f"\nEnd of '{self._testMethodName}'")
        del self.seq, self.t0

    def test_grouper(self):
        self.assertEqual(set(self.seq2.grouper(5)[0]), {29, True, 2.71, 'Exponent', None}, "test_grouper_err")
        with self.assertRaises(TypeError):
            self.seq.grouper()

    def test_filPrime(self):
        self.assertTrue(set(self.seq.filtrPrime()) == {2, 17}, "Что-то не так в filtrPrime")
        self.assertTrue(set(self.seq2.filtrPrime()) == {29}, "Что-то не так в filtrPrime")
        self.assertTrue(set(self.seq3.filtrPrime()) == {1, 2, 3, 5, 7, 11, 13, 17, 19, 23}, 'test_fPrime,line 3')

    def test_filNumber(self):
        self.assertTrue(set(self.seq.filtrNumber()) == {2, 17, 33, (2+5j)}, "Что-то не так в filNumber")
        self.assertTrue(set(self.seq2.filtrNumber()) == {29, 2.71}, "Что-то не так в test_filNumber,line 2")


if __name__ == "__main__":
    unittest.main()
