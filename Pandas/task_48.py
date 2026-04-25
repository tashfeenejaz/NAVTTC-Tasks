#Show the relationship between the columns:
import pandas as pd
df = pd.read_csv('iris_multi_class.csv')
df.corr()

