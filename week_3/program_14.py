# Module part
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence[:n]

# Main program
num = int(input("Enter how many Fibonacci numbers you want: "))
print(f"Fibonacci sequence: {fibonacci(num)}")
