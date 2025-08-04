# Step 1: Define a function that takes two lists as input
def are_lists_equal(list1, list2):
    # Step 2: Use '==' to check if both lists are equal
    # This checks:
    # - Same length
    # - Same elements
    # - Same order
    return list1 == list2  # Returns True if equal, else False

# Step 3: Create some example lists
a = [1, 2, 3]      # First list
b = [1, 2, 3]      # Second list (same as first)
c = [3, 2, 1]      # Third list (same elements but different order)

# Step 4: Test the function and print the results
print(are_lists_equal(a, b))  # Should print True because both are exactly the same
print(are_lists_equal(a, c))  # Should print False because the order is different