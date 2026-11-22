import unittest
from app import calculate_discount

class TestDiscount(unittest.TestCase):
    def test_valid_discount(self):
        self.assertEqual(calculate_discount(100.0, 20.0), 80.0)

    def test_invalid_discount(self):
        with self.assertRaises(ValueError):
            calculate_discount(100.0, 150.0)

if __name__ == "__main__":
    unittest.main()

