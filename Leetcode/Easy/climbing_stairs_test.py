import unittest
from climbing_stairs import climbing_stairs


class ClimbingStairsTestCase(unittest.TestCase):
    def test_climbing_stairs(self):
        self.assertEqual(climbing_stairs(2), 2)
        self.assertEqual(climbing_stairs(3), 3)
        self.assertEqual(climbing_stairs(5), 8)
        self.assertEqual(climbing_stairs(1), 1)


if __name__ == '__main__':
    unittest.main()
