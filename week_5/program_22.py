# 1. Create a dictionary
student = {
    "name": "Alice",
    "age": 22,
    "course": "Computer Science"
}

# 2. Print the dictionary
print("Student Dictionary:", student)

# 3. Access items (using key)
print("Name:", student["name"])
print("Age:", student["age"])

# 4. Use get() method
print("Course (using get):", student.get("course"))
print("Grade (using get with default):", student.get("grade", "Not Assigned"))

# 5. Change values
student["age"] = 23  # updating age
student["name"] = "Bob"  # changing name
print("Updated Dictionary:", student)

# 6. Use len() to find number of key-value pairs
print("Number of items in dictionary:", len(student))