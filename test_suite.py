import unittest
import pandas as pd
import os

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
class test_read_csv_file(unittest.TestCase):
    def test_read_csv_file(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))

        test_file_path = os.path.join(script_dir, 'Madrid Daily Weather 1997-2015.csv')

        result = read_csv_file(test_file_path)

        self.assertIsInstance(result, pd.DataFrame)


if __name__ == '__main__':
    unittest.main()