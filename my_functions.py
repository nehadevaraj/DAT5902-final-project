import pandas as pd

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