import os
from src.data_processor import read_and_sum_column

def test_sum_column():
    file_path = os.path.join(os.path.dirname(__file__), '..', 'sample.csv')
    result = read_and_sum_column(file_path)
    assert result == 6, f"Expected sum is 6, but got {result}"
