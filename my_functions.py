import pandas as pd
from scipy.stats import kendalltau
from scipy.stats import spearmanr
from scipy.stats import pointbiserialr

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


######### TEST 6: SPEARMAN CORRELATION FOR MIN AND MAX SEA LEVEL PRESSURE COLUMNS ##############
def calculate_spearman_correlation(data, column1, column2):
    spearman_correlation, _ = spearmanr(data[column1], data[column2])
    return spearman_correlation



######### TEST 7: POINT_BISERIAL CORRELATION FOR EVENTS AND MEAN DEW POINT COLUMNS ##############
'''def calculate_point_biserial_correlation(data, continuous_column, binary_column):
    point_biserial_correlation, _ = pointbiserialr(data[continuous_column], data[binary_column])
    return point_biserial_correlation'''

def calculate_point_biserial_correlation(data, continuous_column, binary_column):
    data[binary_column] = ((data[continuous_column].notnull()) & (data[continuous_column].astype(str).str.strip() != '')).astype(int)
    return pointbiserialr(data[continuous_column], data[binary_column])[0]

