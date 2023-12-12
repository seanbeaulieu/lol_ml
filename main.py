import numpy as np
import pandas as pd

# Load the CSV file into a DataFrame
file_path = 'lol_2023.csv'
lol_data = pd.read_csv(file_path, engine='python')

# Display the first few rows of the DataFrame
print(lol_data.head())