# Create a tuple
my_tuple = (1, 2, 3)
print("Original tuple:", my_tuple)

# 1) Add items (create a new tuple)
my_tuple = my_tuple + (4, 5)
print("After adding items:", my_tuple)

# 2) len()
print("Length of tuple:", len(my_tuple))

# 3) Check for item in tuple
item_to_check = 3
print(f"Is {item_to_check} in tuple?", item_to_check in my_tuple)

# 4) Access items
print("First item:", my_tuple[0])
print("Last item:", my_tuple[-1])
print("Slice (2nd to 4th):", my_tuple[1:4])
