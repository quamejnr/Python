import unittest
from finding_prime import is_prime, is_factor, square_root


class FindingPrimeTest(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(is_prime(35), False)
        self.assertEqual(is_prime(55), False)
        self.assertEqual(is_prime(13), True)
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(2), True)

    def test_is_factor(self):
        self.assertEqual(is_factor(35, 5), True)
        self.assertEqual(is_factor(41, 7), False)
        self.assertEqual(is_factor(73, 3), False)

    def test_square_root(self):
        self.assertEqual(square_root(36), 6.0)
        self.assertEqual(square_root(49), 7.0)
        self.assertEqual(square_root(12), 3.4641016151377545870548926830117)


if __name__ == '__main__':
    unittest.main()
