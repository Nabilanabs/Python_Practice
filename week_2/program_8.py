# Program to find the largest of three numbers

# Function to find the largest number
def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Input three numbers
print("Enter three numbers:")
number1 = float(input("Number 1: "))
number2 = float(input("Number 2: "))
number3 = float(input("Number 3: "))

# Find the largest number
largest_number = find_largest(number1, number2, number3)

# Print the result
print(f"The largest number among {number1}, {number2}, and {number3} is: {largest_number}")