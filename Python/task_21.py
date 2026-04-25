#Python List
# a list of three elements
ages = [19, 26, 29]
print(ages)

#List Items of Different Types
# a list containing strings, numbers and another list
student = ['Jack', 32, 'Computer Science', [2, 4]]
print(student)
# an empty list
empty_list = []
print(empty_list)

#Access List Elements
languages = ['Python', 'Swift', 'C++']
# access the first element
print('languages[0] =', languages[0])
# access the third element
print('languages[2] =', languages[2])

#Negative Indexing
languages = ['Python', 'Swift', 'C++']
# access the last item
print('languages[-1] =', languages[-1])
# access the third last item
print('languages[-3] =', languages[-3])

#Slicing of a List in Python
my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm']
print("my_list =", my_list)
# get a list with items from index 2 to index 4 (index 5 is not included)
print("my_list[2: 5] =", my_list[2: 5])
# get a list with items from index 2 to index -3 (index -2 is not included)
print("my_list[2: -2] =", my_list[2: -2])
# get a list with items from index 0 to index 2 (index 3 is not included)
print("my_list[0: 3] =", my_list[0: 3])

#Omitting Start and End Indices in Slicing
my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm']
print("my_list =", my_list)
# get a list with items from index 5 to last
print("my_list[5: ] =", my_list[5: ])
# get a list from the first item to index -5
print("my_list[: -4] =", my_list[: -4])
# omitting both start and end index
# get a list from start to end items
print("my_list[:] =", my_list[:])

#Add Elements to a Python List
fruits = ['apple', 'banana', 'orange']
print('Original List:', fruits)
fruits.append('cherry')
print('Updated List:', fruits)

#Add Elements at the Specified Index
fruits = ['apple', 'banana', 'orange']
print("Original List:", fruits)
fruits.insert(2, 'cherry')
print("Updated List:", fruits)


#Add Elements to a List From Other Iterables
numbers = [1, 3, 5]
print('Numbers:', numbers)
even_numbers  = [2, 4, 6]
print('Even numbers:', numbers)
# adding elements of one list to another
numbers.extend(even_numbers)
print('Updated Numbers:', numbers)

#Change List Items
colors = ['Red', 'Black', 'Green']
print('Original List:', colors)
# change the first item to 'Purple'
colors[0] = 'Purple'
# change the third item to 'Blue'
colors[2] = 'Blue'
print('Updated List:', colors)

#Remove an Item From a List
numbers = [2,4,7,9]
# remove 4 from the list
numbers.remove(4)
print(numbers)

#Remove One or More Elements of a List
names = ['John', 'Eva', 'Laura', 'Nick', 'Jack']
# delete the item at index 1
del names[1]
print(names)
# delete items from index 1 to index 2
del names[1: 3]
print(names)
# delete the entire list
del names
# Error! List doesn't exist.
print(names)

#Python List Length
cars = ['BMW', 'Mercedes', 'Tesla']
print('Total Elements:', len(cars))

#Iterating Through a List
fruits = ['apple', 'banana', 'orange']
# iterate through the list
for fruit in fruits:
    print(fruit)

