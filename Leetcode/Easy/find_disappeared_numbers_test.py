import unittest
from find_disappeared_numbers import find_disappeared_numbers


class DisappearedNumbersTestCase(unittest.TestCase):
    def test_find_disappeared_numbers(self):
        self.assertEqual(find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]), [5, 6])
        self.assertEqual(find_disappeared_numbers([1, 1]), [2])


if __name__ == '__main__':
    unittest.main()
