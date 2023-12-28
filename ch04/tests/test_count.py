import unittest
from count import count

class TestCount(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count([]), 0)

    def test_single_element_list(self):
        self.assertEqual(count([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(count([1, 2, 3, 4, 5]), 5)

    def test_nested_list(self):
        self.assertEqual(count([1, [2, 3], 4, 5]), 4)

if __name__ == '__main__':
    unittest.main()