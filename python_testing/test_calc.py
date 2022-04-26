import unittest
from calc import add, divide


class TestCalc(unittest.TestCase):

    def test_add(self):
        a = 3
        b = 6
        expected_result = 9
        actual_result = add(a, b)
        self.assertEqual(actual_result, expected_result)

    def test_divide(self):
        a = 4
        b = 2
        expected_result = 2
        actual_result = divide(a, b)
        self.assertEqual(actual_result, expected_result)

    def test_divide_by_zero(self):
        a = 4
        b = 0
        with self.assertRaises(ZeroDivisionError):
            divide(a, b)
        