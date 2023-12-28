import unittest
from typing import List, SupportsComplex
from sum import sum

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum([0, 0, 0, 0, 0]), 0)
        self.assertEqual(sum([-1, -2, -3, -4, -5]), -15)
        self.assertEqual(sum([]), 0)

if __name__ == '__main__':
    unittest.main()