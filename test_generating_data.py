import unittest
from generating_data import data_with_sin, data_with_ln, data_with_parabola, forming_data


class TestGeneratingData(unittest.TestCase):
    def test_data_with_sin(self):
        expect = ['2020-01, 118, 14', '2020-02, 118, 18', '2020-03, 118, 19', '2020-04, 118, 18', '2020-05, 118, 15',
                  '2020-06, 118, 10', '2020-07, 118, 5', '2020-08, 118, 1', '2020-09, 118, 0', '2020-10, 118, 1',
                  '2020-11, 118, 4', '2020-12, 118, 9']
        result = data_with_sin(10, '118', 0)
        self.assertEqual(expect, result)

    def test_data_with_sin_with(self):
        expect = ['2020-01, 118, Richard, 14', '2020-02, 118, Richard, 18', '2020-03, 118, Richard, 19',
                  '2020-04, 118, Richard, 18', '2020-05, 118, Richard, 15', '2020-06, 118, Richard, 10',
                  '2020-07, 118, Richard, 5', '2020-08, 118, Richard, 1', '2020-09, 118, Richard, 0',
                  '2020-10, 118, Richard, 1', '2020-11, 118, Richard, 4', '2020-12, 118, Richard, 9']
        result = data_with_sin(10, '118', 'Richard')
        self.assertEqual(expect, result)

    def test_data_with_parabola(self):
        expect = ['2020-01, 121, 19', '2020-02, 121, 20', '2020-03, 121, 21', '2020-04, 121, 22', '2020-05, 121, 23',
                  '2020-06, 121, 24', '2020-07, 121, 25', '2020-08, 121, 26', '2020-09, 121, 27', '2020-10, 121, 28',
                  '2020-11, 121, 29', '2020-12, 121, 30']
        result = data_with_parabola(50, '121', 0)
        self.assertEqual(expect, result)

    def test_data_with_parabola_with_stuff(self):
        expect = ['2020-01, 121, Gavin, 19', '2020-02, 121, Gavin, 20', '2020-03, 121, Gavin, 21',
                  '2020-04, 121, Gavin, 22', '2020-05, 121, Gavin, 23', '2020-06, 121, Gavin, 24',
                  '2020-07, 121, Gavin, 25', '2020-08, 121, Gavin, 26', '2020-09, 121, Gavin, 27',
                  '2020-10, 121, Gavin, 28', '2020-11, 121, Gavin, 29', '2020-12, 121, Gavin, 30']
        result = data_with_parabola(50, '121', 'Gavin')
        self.assertEqual(expect, result)

    def test_data_with_lh(self):
        expect = ['2020-01, 118, 13', '2020-02, 118, 13', '2020-03, 118, 13', '2020-04, 118, 13', '2020-05, 118, 13',
                  '2020-06, 118, 14']
        result = data_with_ln(10000, '118', 0)
        self.assertEqual(expect, result)

    def test_data_with_lh_with_stuff(self):
        expect = ['2020-01, 118, Daniel, 10', '2020-02, 118, Daniel, 11', '2020-03, 118, Daniel, 11',
                  '2020-04, 118, Daniel, 12', '2020-05, 118, Daniel, 12', '2020-06, 118, Daniel, 12']
        result = data_with_ln(10, '118', 'Daniel')
        self.assertEqual(expect, result)

    def test_forming_data(self):
        expect = '2020-01, 118, 74\n2020-02, 118, 93\n2020-03, 118, 99\n2020-04, 118, 93\n2020-05, 118, 75\n' \
                 '2020-06, 118, 50\n2020-07, 118, 25\n2020-08, 118, 6\n2020-09, 118, 0\n2020-10, 118, 6\n' \
                 '2020-11, 118, 24\n2020-12, 118, 49\n2020-01, 202, 20\n2020-02, 202, 21\n2020-03, 202, 22\n' \
                 '2020-04, 202, 23\n2020-05, 202, 24\n2020-06, 202, 25\n2020-07, 202, 26\n2020-08, 202, 27\n' \
                 '2020-09, 202, 28\n2020-10, 202, 29\n2020-11, 202, 30\n2020-12, 202, 31\n2020-01, 119, 11\n' \
                 '2020-02, 119, 11\n2020-03, 119, 12\n2020-04, 119, 12\n2020-05, 119, 12\n2020-06, 119, 12\n'
        result = forming_data(50, 0)
        self.assertEqual(expect, result)


if __name__ == "__main__":
    unittest.main()