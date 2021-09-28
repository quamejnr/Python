import unittest
from maximum_sub_array import max_sub_array


class MaximumSubArrayTestCase(unittest.TestCase):
    def test_max_sub_array(self):
        self.assertEqual(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(max_sub_array([1]), 1)
        self.assertEqual(max_sub_array([5, 4, -1, 7, 8]), 23)


if __name__ == '__main__':
    unittest.main()
