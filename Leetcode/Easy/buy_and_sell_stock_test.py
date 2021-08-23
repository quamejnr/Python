import unittest
from buy_and_sell_stock import max_profit


class MaxProfitTestCase(unittest.TestCase):
    def test_max_profit(self):
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(max_profit([7, 6, 4, 3, 1]), 0)
        self.assertEqual(max_profit([2, 6, 4, 7, 9]), 7)


if __name__ == '__main__':
    unittest.main()
