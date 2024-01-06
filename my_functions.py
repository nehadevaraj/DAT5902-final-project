import pandas as pd
from scipy.stats import kendalltau

'''
########## EXAMPLE TEST ############
#example function:
def add_numbers(a,b):
    return a + b
########## EXAMPLE TEST ############
'''

######### TEST 1: READING CSV FILE ##############
def read_csv_file(file_path):
    data = pd.read_csv(file_path)
    return data


######### TEST 2: CONVERTING CET COLUMN TO DATETIME FORMAT ##############
def convert_column_to_datetime(data, column_name):
    data[column_name] = pd.to_datetime(data[column_name])
    return data


######### TEST 3: SET CET COLUMN AS INDEX ##############
def set_cet_as_index(data):
    data.set_index('CET', inplace=True)
    return data


######### TEST 4: PEARSON CORRELATION COEFFICIENT FOR MIN AND MAX TEMP COLUMNS ##############
def calculate_correlation(data, column1, column2):
    correlation_coefficient = data[column1].corr(data[column2], method='pearson')
    return correlation_coefficient


######### TEST 5: KENDALL RANK CORRELATION FOR MIN AND MAX HUMIDITY COLUMNS ##############
def calculate_kendall_correlation(data, column1, column2):
    kendall_correlation = data[column1].corr(data[column2], method='kendall')
    return kendall_correlation