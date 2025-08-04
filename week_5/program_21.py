# Step 1: Create a list
my_list = [10, 20, 30]
print("Original list:", my_list)

# 1) insert(index, value) → Insert value at a specific index
my_list.insert(1, 15)  # Insert 15 at index 1
print("After insert(1, 15):", my_list)

# 2) remove(value) → Remove the first occurrence of value
my_list.remove(20)  # Removes the number 20 from the list
print("After remove(20):", my_list)

# 3) append(value) → Add value at the end
my_list.append(40)  # Appends 40 at the end
print("After append(40):", my_list)

# 4) len(list) → Returns the number of elements
length = len(my_list)
print("Length of the list:", length)

# 5) pop(index) → Removes and returns element at index
popped = my_list.pop(2)  # Removes item at index 2
print("After pop(2):", my_list)
print("Popped value:", popped)

# 6) clear() → Removes all elements
my_list.clear()
print("After clear():", my_list)