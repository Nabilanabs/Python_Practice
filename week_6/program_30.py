#write a program to double a given number and add two number using lambda()

#this line creates a lambda function and assigns it to a varible 

# Lambda to double a number
double = lambda x: x * 2

# Lambda to add two numbers
add = lambda a, b: a + b

# Example usage
number = int(input("Enter  Number To Double : "))
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))

print("Double of", number, "is:", double(number))
print("Sum of", num1, "and", num2, "is:", add(num1, num2))