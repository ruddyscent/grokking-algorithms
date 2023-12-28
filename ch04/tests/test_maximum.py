import unittest
from maximum import maximum

class TestMaximum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(maximum([]), None)

    def test_single_element_list(self):
        self.assertEqual(maximum([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(maximum([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(maximum([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(maximum([-1, 0, 1, 2, -2]), 2)

if __name__ == '__main__':
    unittest.main()