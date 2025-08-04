# Program to CREATE, JOIN, and EXTRACT substrings in a string

# Step 1: Create two strings
string1 = "Python"
string2 = "Programming"

# Step 2: Concatenate the strings with a space
concatenated_string = string1 + " " + string2

# Step 3: Print the concatenated string
print("Concatenated String:", concatenated_string)

# Step 4: Extract the first 6 characters
substring1 = concatenated_string[0:6]  # "Python"
print("Substring (first 6 characters):", substring1)

# Step 5: Extract substring from index 7 to the end
substring2 = concatenated_string[7:]  # "Programming"
print("Substring from index 7 to end:", substring2)

# Step 6: Access a specific character at index 1
specific_character = concatenated_string[1]  # "y"
print("Specific character at index 1:", specific_character)

# Step 7: Extract substring using negative indexing
# Total string: "Python Programming"
# Length = 18, "Programming" is last 11 characters
substring3 = concatenated_string[-11:]  # "Programming"
print("Substring using negative indexing:", substring3)
