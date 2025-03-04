import pandas as pd


def read_file(file_path):
    return pd.read_csv(file_path)

def read_json(file_path):
    return pd.read_json(file_path)