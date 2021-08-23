import unittest
from range_sum_query import NumArray


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.num_array = NumArray([-2, 0, 3, -5, 2, -1])

    def test_sum_range(self):
        self.assertEqual(self.num_array.sum_range(0, 2), 1)
        self.assertEqual(self.num_array.sum_range(2, 5), -1)
        self.assertEqual(self.num_array.sum_range(0, 5), -3)


if __name__ == '__main__':
    unittest.main()
