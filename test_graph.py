import unittest
from graphs import get_all_lines_from_file, making_dictionary, making_dictionary_with_stuff, sorting_dictionary,\
                    making_sorted_dictionary, making_sorted_dictionary_with_stuff


class TestGraphic(unittest.TestCase):
    def test_get_all_lines_from_file(self):
        expect = ['date,resource,count\n', '2020-01, 118, 14\n', '2020-02, 118, 18\n', '2020-03, 118, 19\n',
                  '2020-04, 118, 18\n', '2020-05, 118, 15\n', '2020-06, 118, 10\n', '2020-07, 118, 5\n',
                  '2020-08, 118, 1\n', '2020-09, 118, 0\n', '2020-10, 118, 1\n', '2020-11, 118, 4\n',
                  '2020-12, 118, 9\n', '2020-01, 202, 0\n', '2020-02, 202, 0\n', '2020-03, 202, 0\n',
                  '2020-04, 202, 0\n', '2020-05, 202, 0\n', '2020-06, 202, 1\n', '2020-07, 202, 1\n',
                  '2020-08, 202, 1\n', '2020-09, 202, 1\n', '2020-10, 202, 1\n', '2020-11, 202, 2\n',
                  '2020-12, 202, 2\n', '2020-01, 119, 11\n', '2020-02, 119, 11\n', '2020-03, 119, 12\n',
                  '2020-04, 119, 12\n', '2020-05, 119, 12\n', '2020-06, 119, 12\n']
        result = get_all_lines_from_file('data.txt')
        self.assertEqual(expect, result)

    def test_making_dictionary(self):
        expect = {'date': '2020-01',
                  'resource': '118',
                  'count': '14'}
        result = making_dictionary('2020-01, 118, 14', 'date,resource,count')
        self.assertEqual(expect, result)

    def test_making_dictionary_with_stuff(self):
        expect = {'date': '2020-01',
                  'resource': '118',
                  'stuff_id': 'Connor',
                  'count': '14'}
        result = making_dictionary_with_stuff('2020-01, 118, Connor, 14', 'date,resource,stuff_id,count')
        self.assertEqual(expect, result)

    def test_sorting_dictionary(self):
        expect = [{'date': '2020-01', 'resource': '121', 'stuff_id': 'Richard', 'count': '21'},
                  {'date': '2020-03', 'resource': '119', 'stuff_id': 'Connor', 'count': '17'},
                  {'date': '2020-06', 'resource': '118', 'stuff_id': 'Reed', 'count': '10'}]
        result = sorting_dictionary([{'date': '2020-03', 'resource': '119', 'stuff_id': 'Connor', 'count': '17'},
                                     {'date': '2020-06', 'resource': '118', 'stuff_id': 'Reed', 'count': '10'},
                                     {'date': '2020-01', 'resource': '121', 'stuff_id': 'Richard', 'count': '21'}])
        self.assertEqual(expect, result)

    def test_making_sorted_dictionary(self):
        expect = [{'date': '2020-01', 'resource': '121', 'count': '21'},
                  {'date': '2020-03', 'resource': '119', 'count': '17'},
                  {'date': '2020-06', 'resource': '118', 'count': '10'}]
        result = making_sorted_dictionary(['2020-03, 119, 17\n', '2020-06, 118, 10\n', '2020-01, 121, 21\n'],
                                          'date,resource,count')
        self.assertEqual(expect, result)

    def test_making_sorted_dictionary_with_stuff(self):
        expect = [{'date': '2020-02', 'resource': '121', 'stuff_id': 'Richard', 'count': '21'},
                  {'date': '2020-03', 'resource': '119', 'stuff_id': 'Connor', 'count': '17'},
                  {'date': '2020-07', 'resource': '118', 'stuff_id': 'Gavin', 'count': '10'}]
        result = making_sorted_dictionary_with_stuff(['2020-03, 119, Connor, 17\n', '2020-07, 118, Gavin, 10\n',
                                                      '2020-02, 121, Richard, 21\n'], 'date,resource,stuff_id,count')
        self.assertEqual(expect, result)


if __name__ == "__main__":
    unittest.main()