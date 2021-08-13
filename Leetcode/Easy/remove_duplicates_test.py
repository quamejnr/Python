import unittest
from remove_duplicates import remove_duplicates, remove_duplicates2


class RemoveDuplicatesTestCase(unittest.TestCase):
    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)
        self.assertEqual(remove_duplicates([1, 1, 2]), 2)
        self.assertEqual(remove_duplicates([0, 1, 2, 3, 4]), 5)

    def test_remove_duplicates2(self):
        self.assertEqual(remove_duplicates2([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)
        self.assertEqual(remove_duplicates2([1, 1, 2]), 2)
        self.assertEqual(remove_duplicates2([0, 1, 2, 3, 4]), 5)


if __name__ == '__main__':
    unittest.main()
