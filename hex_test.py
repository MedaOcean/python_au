import unittest
from hex_number import HexNumber
class TestHexNumber(unittest.TestCase):
    def test_sum(self):
        num_1= HexNumber('11F')
        num_2=HexNumber('2A')
        expect = '95'
        result = num_1.add(num_2)
        self.assertEqual(expect, result)

if __name__ == "__main__":
    unittest.main()