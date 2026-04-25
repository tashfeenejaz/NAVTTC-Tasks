# using for loop with list of strings
print("using for loop with list of strings:")
s = ["Geeks", "for", "Geeks"]
for i in s:
    print(i)

# Iterating over characters of strings
print("\nIterating over characters of strings:")
s = ["Geeks", "for", "Geeks"]
s = "Geeks"
for i in s:
    print(i)

#Using range() with For Loop
print("\nUsing range() with For Loop")
for i in range(0, 10, 2):
    print(i)

#Control Statements with For Loop
# Prints all letters except 'e' and 's'
print("\nPrints all letters except 'e' and 's':")
for i in 'geeksforgeeks':
    if i == 'e' or i == 's':
        continue
    print(i)

#Break with For Loop
print("Use Of break as soon it sees e: ")
for i in 'geeksforgeeks':
    # break the loop as soon it sees 'e'
    # or 's'
    if i == 'e' or i == 's':
        break

print(i)

#Pass Statement with For Loop
# An empty loop
for i in 'geeksforgeeks':
    pass
print(i)

#Else Statement with For Loops
for i in range(1, 4):
    print(i)
else:  # Executed because no break in for
    print("No Break\n")

#Using Enumerate with for loop
print("\nUsing Enumerate with for loop")
li = ["eat", "sleep", "repeat"]

for i, j in enumerate(li):
    print (i, j)

#Nested For Loops
print("\nNested For Loops:")
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

