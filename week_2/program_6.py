# Demonstrating tuples in Python

# Creating a tuple
my_tuple = ("apple", "banana", "cherry", 42, 3.14)

# Accessing elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing a tuple
print("Slice (1 to 3):", my_tuple[1:4])

# Looping through a tuple
print("All elements in tuple:")
for item in my_tuple:
    print(item)

# Tuple length
print("Length of tuple:", len(my_tuple))

# Nested tuple
nested = ("car", ("bike", "bus"))
print("Nested tuple:", nested)
print("Access nested element:", nested[1][0])
