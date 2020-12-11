import unittest
from complex_number import ComplexNumber

class TestComplexNumber(unittest.TestCase):
    def test_sum(self):
        num1 = ComplexNumber(5, 10)
        num2 = ComplexNumber(3, 4)
        expect = ComplexNumber(8, 14)
        result = num1.add(num2)
        self.assertEqual(expect, result)
    def test_sub(self):
        num1 = ComplexNumber(5, 10)
        num2 = ComplexNumber(3, 4)
        expect = ComplexNumber(2, 6)
        result = num1.sub(num2)
        self.assertEqual(expect, result)
    def test_mod(self):
        num = ComplexNumber(3, 4)
        expect = 5
        result = num.mod()
        self.assertEqual(expect, result)
    def test_sub(self):
        num1 = ComplexNumber(5, 10)
        num2 = ComplexNumber(3, 4)
        expect = ComplexNumber(2, 6)
        result = num1.sub(num2)
        self.assertEqual(expect, result)
    def test_multiplication(self):
        num1 = ComplexNumber(5, 10)
        num2 = ComplexNumber(3, 4)
        expect = ComplexNumber(-25, 50)
        result = num1.multiplication(num2)
        self.assertEqual(expect, result)
if __name__ == 'main':
    unittest.main()

