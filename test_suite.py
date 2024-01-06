import unittest
import pandas as pd

'''
from my_functions import add_numbers

class TestFunction(unittest.TestCase):

    def test_addition(self):
        result = add_numbers(3,5)
        self.assertEqual(result, 8)
        
if __name__ == '__main__':
    unittest.main()
'''
from my_functions import read_csv_file
class TestReadCSVFile(unittest.TestCase):
    def test_read_csv_file(self):
        test_file_path = 'C:/Users/nehadevaraj/Library/CloudStorage/OneDrive-QueenMary,UniversityofLondon/2nd year/professional software and career practices/DAT5092 final project/Madrid Daily Weather 1997-2015.csv'

        result = read_csv_file(test_file_path)

        self.assertIsInstance(result, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()