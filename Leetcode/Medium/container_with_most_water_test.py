import unittest
from container_with_most_water import max_area


class MaxAreaTestCase(unittest.TestCase):
    def test_max_area(self):
        self.assertEqual(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
        self.assertEqual(max_area([1, 1]), 1)
        self.assertEqual(max_area([4, 3, 2, 1, 4]), 16)


if __name__ == '__main__':
    unittest.main()
