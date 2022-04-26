import unittest
from calc_cls import Calc


class TestCalc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.c = Calc(4, 2)
        cls.c2 = Calc(4, 0)
        # print('setUp')

    def test_add(self):
        expected_result = 6
        actual_result = self.c.add()
        self.assertEqual(actual_result, expected_result)
        # print('test_add')

    def test_divide(self):
        expected_result = 2
        actual_result = self.c.divide()
        self.assertEqual(actual_result, expected_result)
        # print('test_divide')

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.c2.divide()
        # print('test_divide_by_zero')
    
    @classmethod
    def tearDownClass(cls):
        del cls.c
        del cls.c2
        # print('tearDown')

if __name__ == "__main__":
    unittest.main()