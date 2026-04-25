#Python Functions
def fun():
    print("Welcome to GFG")

#Calling a Function
print("\nCalling a Function:")
def fun():
    print("Welcome to GFG")
fun()


#Function Arguments
print("\nFunction Arguments:")
def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))

#Default Arguments
print("\nDefault Arguments:")
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(10)

# Keyword Arguments
print("\n Keyword Arguments: ")
def student(fname, lname):
    print(fname, lname)

student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')

#Positional Arguments:
print("\n: Positional Arguments:")
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Olivia", 27)

print("\nCase-2:")
nameAge(27, "Olivia")

#Arbitrary Arguments
print("\nArbitrary Arguments:")
def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myFun('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')

#Function within Functions
print("\nFunction within Functions:")
def f1():
    s = 'I love GeeksforGeeks'

    def f2():
        print(s)

    f2()
f1()

#Anonymous Functions
print("\nAnonymous Functions:")
def c1(x): return x*x*x
c2 = lambda x : x*x*x

print(c1(7))
print(c2(7))

#Return Statement
print("\nReturn Statement:")
def sq_value(num):
    """This function returns the square
    value of the entered number"""
    return num**2

print(sq_value(2))
print(sq_value(-4))

#Pass by Reference and Pass by Value
print("\nPass by Reference and Pass by Value:")
def myFun(x):
    x[0] = 20

lst = [10, 11, 12, 13]
myFun(lst)
print(lst)

def myFun2(x):
    x = 20

a = 10
myFun2(a)
print(a)

#Recursive Functions
print("\nRecursive Functions:")
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4))