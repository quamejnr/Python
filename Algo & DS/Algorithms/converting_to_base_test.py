import unittest
from converting_to_base import base_number


class ConvertingToBaseTest(unittest.TestCase):
    def test_base_number(self):
        self.assertEqual(base_number(20, 2), 10100)
        self.assertEqual(base_number(10, 5), 20)
        self.assertEqual(base_number(14, 3), 112)


if __name__ == '__main__':
    unittest.main()
