import unittest
from quicksort import quicksort

class TestQuicksort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(quicksort([]), [])

    def test_single_element_list(self):
        self.assertEqual(quicksort([1]), [1])

    def test_multiple_elements_list(self):
        self.assertEqual(quicksort([5, 3, 6, 2, 10]), [2, 3, 5, 6, 10])

    def test_negative_numbers(self):
        self.assertEqual(quicksort([-1, -2, -3, -4, -5]), [-5, -4, -3, -2, -1])

    def test_mixed_numbers(self):
        self.assertEqual(quicksort([-1, 0, 1, 2, -2]), [-2, -1, 0, 1, 2])

if __name__ == '__main__':
    unittest.main()