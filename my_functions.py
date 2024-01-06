import pandas as pd
'''
#example function:
def add_numbers(a,b):
    return a + b
'''

def read_csv_file(file_path):
    data = pd.read_csv(file_path)
    return data