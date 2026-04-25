#Python Strings
# create string type variables
name = "Python"
print(name)
message = "I love Python."
print(message)

#Access String Characters in Python
greet = 'hello'
# access 1st index element
print(greet[1]) # "e"

#Slicing
greet = 'Hello'
# access character from 1st index to 3rd index
print(greet[1:4])  # "ell"

#Python Strings are Immutable(gives error if done)
message = 'Hola Amigos'
message[0] = 'H'
print(message)

#Python Multiline String
# multiline string
message = """
Never gonna give you up
Never gonna let you down
"""
print(message)

# Compare Two Strings
str1 = "Hello, world!"
str2 = "I love Swift."
str3 = "Hello, world!"
# compare str1 and str2
print(str1 == str2)
# compare str1 and str3
print(str1 == str3)

#Join Two or More Strings
greet = "Hello, "
name = "Jack"
# using + operator
result = greet + name
print(result)
# Output: Hello, Jack

#Iterate Through a Python String
greet = 'Hello'
# iterating through greet string
for letter in greet:
    print(letter)

#Python String Length
greet = 'Hello'
# count length of greet string
print(len(greet))
# Output: 5

#String Membership Test
print('a' in 'program') # True
print('at' not in 'battle') # False

#Escape Sequences in Python
example = "He said, "What's there?""
print(example) # throws error

#Solution:
# escape double quotes
example = "He said, \"What's there?\""
# escape single quotes
example = 'He said, "What\'s there?"'
print(example)
# Output: He said, "What's there?"