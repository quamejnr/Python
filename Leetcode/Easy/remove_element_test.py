import unittest
from remove_element import remove_element


class RemoveElementTest(unittest.TestCase):
    def test_remove_element(self):
        self.assertEqual(remove_element([3, 2, 2, 3], 3), 2)
        self.assertEqual(remove_element(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2), 5)


if __name__ == '__main__':
    unittest.main()
