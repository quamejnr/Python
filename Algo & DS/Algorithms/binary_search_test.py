import unittest
from binary_search import binary_search, binary_search_rec, occurrence, count_occurrences, finding_rotated_times


class BinarySearchTestCase(unittest.TestCase):
    def test_binary_search(self):
        self.assertEqual(binary_search(list(range(10)), 9), 9)
        self.assertEqual(binary_search(list(range(50)), 23), 23)
        self.assertEqual(binary_search([1, 3, 4, 8, 9, 12, 13, 16], 17), -1)

    def test_binary_search_rec(self):
        self.assertEqual(binary_search_rec([2, 5, 6, 7, 10, 12, 13, 16], 0, 7, 10), 4)
        self.assertEqual(binary_search_rec([2, 5, 6, 7, 33, 45, 47, 56], 0, 7, 45), 5)
        self.assertEqual(binary_search_rec([12, 25, 36, 47, 60, 72, 83, 96], 0, 7, 45), -1)

    def test_occurrence(self):
        self.assertEqual(occurrence([1, 3, 4, 8, 9, 10, 10, 10, 12, 13, 16], 10, True), 5)
        self.assertEqual(occurrence([2, 5, 6, 7, 33, 45, 45, 45, 47, 56], 45, False), 7)
        self.assertEqual(occurrence([2, 5, 6, 7, 33, 45, 47, 56], 10, True), -1)
        self.assertEqual(occurrence([2, 5, 6, 7, 33, 45, 47, 56], 7, True), 3)

    def test_count_occurrence(self):
        self.assertEqual(count_occurrences([1, 3, 4, 8, 9, 10, 10, 10, 12, 13, 16], 10), 3)
        self.assertEqual(count_occurrences([2, 5, 6, 7, 7, 33, 45, 45, 45, 47, 56], 7), 2)
        self.assertEqual(count_occurrences([2, 5, 6, 7, 33, 45, 47, 56], 10), -1)

    def test__finding_rotated_times(self):
        self.assertEqual(finding_rotated_times([17, 18, 4, 8, 9, 10, 10, 10, 12, 13, 16]), 2)
        self.assertEqual(finding_rotated_times([2, 5, 6, 7, 7, 33, 45, 45, 45, 47, 56]), 0)
        self.assertEqual(finding_rotated_times([66, 2, 5, 6, 7, 33, 45, 47, 56]), 1)


if __name__ == '__main__':
    unittest.main()
