# Find square root of real or complex numbers

# Importing the complex math module
import cmath

num = 1+2j

# To take input from the user
#num = eval(input('Enter a number: '))

num_sqrt = cmath.sqrt(num)
print(f"The square root of {num} is : {num_sqrt:.3f}")