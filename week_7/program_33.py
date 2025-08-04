from functools import reduce

# List of numbers
numbers = [5, 10, 15, 20, 25]

# Using reduce to calculate the sum
sum_of_numbers = reduce(lambda x, y: x + y, numbers)

# Display the result
print("The sum of the list elements is:", sum_of_numbers)