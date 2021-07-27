import unittest
from converting_to_base import base_number, base_number_rec


class ConvertingToBaseTest(unittest.TestCase):
    def test_base_number(self):
        self.assertEqual(base_number(20, 2), 10100)
        self.assertEqual(base_number(10, 5), 20)
        self.assertEqual(base_number(14, 3), 112)

    # def test_base_number_rec(self):
    #     self.assertEqual(base_number_rec(20, 2), 10100)
    #     self.assertEqual(base_number_rec(10, 5), 20)
    #     self.assertEqual(base_number_rec(14, 3), 112)


if __name__ == '__main__':
    unittest.main()
