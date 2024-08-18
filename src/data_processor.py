import pandas as pd

def read_and_sum_column(file_path):
    df = pd.read_csv(file_path)
    return df['column1'].sum()
