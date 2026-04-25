#Load a CSV file into a Pandas DataFrame
import pandas as pd

df = pd.read_csv('iris_multi_class.csv')

print(df.to_string())