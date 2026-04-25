#Create a Python Tuple
numbers = (1, 2, -5)
print(numbers)

#Access Items Using Index
languages = ('Python', 'Swift', 'C++')
# access the first item
print(languages[0])   # Python

#Tuple Cannot be Modified(Gives an error)
cars = ('BMW', 'Tesla', 'Ford', 'Toyota')
# trying to modify a tuple
cars[0] = 'Nissan'  # error
print(cars)

#Python Tuple Length
cars = ('BMW', 'Tesla', 'Ford', 'Toyota')
print('Total Items:', len(cars))

#Iterate Through a Tuple
fruits = ('apple','banana','orange')
# iterate through the tuple
for fruit in fruits:
    print(fruit)

#