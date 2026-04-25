#installing pandas
#C:\Users\Your Name>pip install pandas

#Importing pandas
import pandas as pd

my_dataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

my_var = pd.DataFrame(my_dataset)

print(my_var)

