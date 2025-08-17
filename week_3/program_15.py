# Define the function (module part)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b  # This won't be used

# Main program (importing "add" conceptually)
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print(f"Sum: {add(x, y)}")
