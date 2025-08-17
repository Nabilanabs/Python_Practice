# Demonstrating dictionaries in Python

# Creating a dictionary
student = {
    "name": "Nabila",
    "age": 21,
    "course": "Computer Science"
}

# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])

# Adding a new key-value pair
student["grade"] = "A"
print("After adding grade:", student)

# Updating a value
student["age"] = 22
print("After updating age:", student)

# Removing a key-value pair
del student["course"]
print("After deleting course:", student)

# Looping through dictionary
print("All keys and values:")
for key, value in student.items():
    print(key, ":", value)
