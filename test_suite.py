import unittest
import pandas as pd
import os
from scipy.stats import kendalltau

'''
########## EXAMPLE TEST ############
from my_functions import add_numbers

class TestFunction(unittest.TestCase):

    def test_addition(self):
        result = add_numbers(3,5)
        self.assertEqual(result, 8)
        
if __name__ == '__main__':
    unittest.main()
########## EXAMPLE TEST ############
'''
######### TEST 1: READING CSV FILE ##############
from my_functions import read_csv_file
class test_read_csv_file(unittest.TestCase):
    def test_read_csv_file(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))

        test_file_path = os.path.join(script_dir, 'Madrid Daily Weather 1997-2015.csv')

        result = read_csv_file(test_file_path)

        self.assertIsInstance(result, pd.DataFrame)


if __name__ == '__main__':
    unittest.main()
    

######### TEST 2: CONVERTING CET COLUMN TO DATETIME FORMAT ############## 
from my_functions import convert_column_to_datetime
class test_convert_column_to_datetime(unittest.TestCase):
    def test_convert_column_to_datetime(self):
        test_data = pd.DataFrame({
            'CET': ['2022-01-01 12:00:00', '2022-01-02 15:30:00', '2022-01-03 18:45:00'],'Temperature': [10, 15, 20]})

        column_name = 'CET'

        result = convert_column_to_datetime(test_data.copy(), column_name)

        self.assertIsInstance(result, pd.DataFrame)

        self.assertTrue(pd.api.types.is_datetime64_any_dtype(result[column_name]))


if __name__ == '__main__':
    unittest.main()
    

######### TEST 3: SET CET COLUMN AS INDEX ##############
from my_functions import set_cet_as_index
class test_set_CET_as_index(unittest.TestCase):
    def test_set_cet_as_index(self):
        test_data = pd.DataFrame({
            'CET': ['2022-01-01 12:00:00', '2022-01-02 15:30:00', '2022-01-03 18:45:00'],'Temperature': [10, 15, 20]})

        result = set_cet_as_index(test_data.copy())

        self.assertIsInstance(result, pd.DataFrame)

        self.assertTrue('CET' in result.index.names)


if __name__ == '__main__':
    unittest.main()
    

######### TEST 4: PEARSON CORRELATION COEFFICIENT FOR MIN AND MAX TEMP COLUMNS ##############
from my_functions import calculate_correlation
class test_calculate_correlation(unittest.TestCase):
    def test_calculate_correlation(self):
        test_data = pd.read_csv('Madrid Daily Weather 1997-2015.csv')

        column2 = 'Min TemperatureC'
        column1 = 'Max TemperatureC'

        result = calculate_correlation(test_data.copy(), column2, column1)

        self.assertIsInstance(result, float)


if __name__ == '__main__':
    unittest.main()
    

######### TEST 5: KENDALL RANK CORRELATION FOR MIN AND MAX HUMIDITY COLUMNS ##############
from my_functions import calculate_kendall_correlation
class test_calculate_kendall_correlation(unittest.TestCase):
    def test_calculate_kendall_correlation(self):
        test_data = pd.read_csv('Madrid Daily Weather 1997-2015.csv')
        
        column2 = ' Min Humidity'
        column1 = 'Max Humidity'

        result = calculate_kendall_correlation(test_data.copy(), column2, column1)

        self.assertIsInstance(result, float)


if __name__ == '__main__':
    unittest.main()
    
    

######### TEST 6: SPEARMAN CORRELATION FOR MIN AND MAX SEA LEVEL PRESSURE COLUMNS ##############
from my_functions import calculate_spearman_correlation
class test_calculate_spearman_correlation(unittest.TestCase):
    def test_calculate_spearman_correlation(self):
        test_data = pd.read_csv('Madrid Daily Weather 1997-2015.csv')

        column2 = ' Min Sea Level PressurehPa'
        column1 = ' Max Sea Level PressurehPa'

        result = calculate_spearman_correlation(test_data.copy(), column2, column1)

        self.assertIsInstance(result, float)


if __name__ == '__main__':
    unittest.main()
    
    

######### TEST 7: POINT_BISERIAL CORRELATION FOR EVENTS AND MEAN DEW POINT COLUMNS ##############
from my_functions import calculate_point_biserial_correlation
class test_calculate_PointBiserial_correlation(unittest.TestCase):
    def test_calculate_point_biserial_correlation(self):
        test_data = pd.read_csv('Madrid Daily Weather 1997-2015.csv')
        
        test_data['EventsCategory'] = test_data[' Events'].notnull().astype(int)

        continuous_column = 'MeanDew PointC'
        binary_column = 'EventsCategory'

        result = calculate_point_biserial_correlation(test_data.copy(), continuous_column, binary_column)

        self.assertIsInstance(result, float)


if __name__ == '__main__':
    unittest.main()