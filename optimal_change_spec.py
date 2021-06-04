import unittest
from optimal_change import optimal_change

class ChangeTestCase(unittest.TestCase):
    """Tests for optimal_change.py."""
    def test_edge_not_enough_money(self):
        self.assertEqual(optimal_change(4.5,2),-1)

    def test_edge_negative_money(self):
        self.assertEqual(optimal_change(-4.5,-2),-2)

    def test_no_change(self):
        self.assertEqual(optimal_change(10,10), 0)

    def test_change1(self):
        self.assertEqual(optimal_change(12.06, 100), {50: 1, 20: 1, 10: 1, 5: 1, 1: 2, 0.25: 3, 0.1: 1, 0.05: 1, 0.01: 4})

    def test_change2(self):
        self.assertEqual(optimal_change(45.14,50), {1: 4, 0.25: 3, 0.1: 1, 0.01: 1})

    def test_change3(self):
        self.assertEqual(optimal_change(12.21, 20), {5: 1, 1: 2, 0.25: 3, 0.01: 4})

#Run the unit tests if this file is being executed
if __name__ == '__main__':
    unittest.main()