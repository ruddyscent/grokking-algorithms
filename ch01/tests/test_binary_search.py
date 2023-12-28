import unittest
from binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(binary_search([], 1), None)

    def test_single_element_list_found(self):
        self.assertEqual(binary_search([1], 1), 0)

    def test_single_element_list_not_found(self):
        self.assertEqual(binary_search([1], 2), None)

    def test_multiple_elements_list_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_multiple_elements_list_not_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), None)

if __name__ == '__main__':
    unittest.main()