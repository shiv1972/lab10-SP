# https://github.com/shiv1972/lab10-SP.git
# Partner 1: Shivam Patel
# Partner 2: Shivam Patel

import unittest
import math
from calculator import add, subtract, multiply, divide, logarithm, exponent, square_root, hypotenuse


class TestCalculator(unittest.TestCase):

    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(5, 10), -5)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):  # 3 assertions
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 10), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(divide(2, 10), 5)
        self.assertEqual(divide(5, 20), 4)
        self.assertEqual(divide(4, 16), 4)

    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 1000), 3)
        self.assertAlmostEqual(logarithm(3, 27), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, -5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(-3, -4), 5)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(16), 4)
        self.assertAlmostEqual(square_root(0), 0)
        with self.assertRaises(ValueError):
            square_root(-9)

if __name__ == "__main__":
    unittest.main()