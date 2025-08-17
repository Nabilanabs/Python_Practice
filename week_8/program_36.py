# Create a 2D "array" using a list of lists
arr = [[1, 2, 3], [4, 5, 6]]

# 1. Type of array
print("Type of array:", type(arr))

# 2. Axes of array (number of dimensions)
axes = 2 if all(isinstance(i, list) for i in arr) else 1
print("Number of axes:", axes)

# 3. Shape of array
rows = len(arr)
cols = len(arr[0]) if axes == 2 else 1
print("Shape of array:", (rows, cols))

# 4. Type of elements in array
element_type = type(arr[0][0]) if axes == 2 else type(arr[0])
print("Data type of elements:", element_type)
