import unittest
from fact import fact

class TestFact(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(fact(1), 1)
        self.assertEqual(fact(2), 2)
        self.assertEqual(fact(3), 6)
        self.assertEqual(fact(4), 24)
        self.assertEqual(fact(5), 120)

if __name__ == '__main__':
    unittest.main()