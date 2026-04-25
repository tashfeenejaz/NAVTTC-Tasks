#Return a new Data Frame with no empty cells
import pandas as pd
df = pd.read_csv('iris_multi_class.csv')
new_df = df.dropna()
print(new_df.to_string())

#Remove all rows with NULL values:
df.dropna(inplace = True)
print(df.to_string())

#Replace NULL values with the number 130
df.fillna(130, inplace = True)

#Replace NULL values in the "Calories" columns with the number 4.8
df.fillna({"sepal_length": 4.8}, inplace=True)

#Calculate the MEAN, and replace any empty values with it
x = df["sepal_length"].mean()
df.fillna({"sepal_length": x}, inplace=True)

#Calculate the MEDIAN, and replace any empty values with it
x = df["sepal_length"].median()
df.fillna({"sepal_length": x}, inplace=True)

#Calculate the MODE, and replace any empty values with it
x = df["sepal_length"].mode()[0]
df.fillna({"sepal_length": x}, inplace=True)

#