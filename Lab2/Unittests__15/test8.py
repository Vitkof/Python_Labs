import unittest
from time import process_time
from Cached__8 import fibo, cach_fibo, my_faktarial, my_cach_faktarial, cached


class TestCached(unittest.TestCase):
    def setUp(self) -> None:
        self.fibo = fibo(30)
        self.cach_fibo = cach_fibo(30)

    def tearDown(self) -> None:
        del self.fibo, self.cach_fibo

    def test_fibo(self):
        self.assertEqual(fibo(1), 1)
        self.assertTrue(fibo(10) == cach_fibo(10), "fibo(10) != cach_fibo(10)")

    def test_timeWithoutCached(self):
        t0 = process_time()
        print("FiboWithout(30) = {}".format(fibo(30)))
        t1 = process_time()
        print(t1-t0)

    def test_timeWithCached(self):
        t0 = process_time()
        print("FiboCache(30) = {}".format(cach_fibo(30)))
        t1 = process_time()
        print(t1-t0)

    def test_MyFaktarialWithoutCached(self):
        t0 = process_time()
        print("MyFaktarial_Without(150) =", my_faktarial(150))
        t1 = process_time()
        print(t1-t0)

    def test_MyFaktarialWithCached(self):
        t0 = process_time()
        print("MyFaktarial_Cache(150) =", my_cach_faktarial(150))
        t1 = process_time()
        print(t1-t0)


if __name__ == "__main__":
    unittest.main()
