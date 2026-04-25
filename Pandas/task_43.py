#Create a simple Pandas Series from a list
import pandas as pd

a = [1, 7, 2]
my_var = pd.Series(a)
print(my_var)

#Return the first value of the Series
print(my_var[0])

#Create your own labels
a = [1, 7, 2]
my_var = pd.Series(a, index = ["x", "y", "z"])
print(my_var)

#Return the value of "y"
print(my_var["y"])

#Create a simple Pandas Series from a dictionary
calories = {"day1": 420, "day2": 380, "day3": 390}
my_var = pd.Series(calories)
print(my_var)

#Create a Series using only data from "day1" and "day2"
calories = {"day1": 420, "day2": 380, "day3": 390}
my_var = pd.Series(calories, index = ["day1", "day2"])
print(my_var)

#Create a DataFrame from two Series
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
my_var = pd.DataFrame(data)
print(my_var)



