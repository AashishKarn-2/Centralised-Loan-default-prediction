import numpy as np
import pandas as pd

def load_data():
    # Load the data
    df = pd.read_csv('data.csv')
    return df