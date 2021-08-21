import unittest
from single_number import single_number


class SingleNumberTestCase(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(single_number([2, 2, 1]), 1)
        self.assertEqual(single_number([4, 1, 2, 1, 2]), 4)
        self.assertEqual(single_number([1]), 1)


if __name__ == '__main__':
    unittest.main()
