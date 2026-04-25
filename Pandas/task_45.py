#Load the CSV into a DataFrame
import pandas as pd

df = pd.read_csv('iris_multi_class.csv')
print(df.to_string())

#Print the DataFrame without the to_string() method:
df = pd.read_csv('iris_multi_class.csv')
print(df)

#Check the number of maximum returned rows
print(pd.options.display.max_rows)

#Increase the maximum number of rows to display the entire DataFrame
pd.options.display.max_rows = 9999
df = pd.read_csv('iris_multi_class.csv')
print(df)

