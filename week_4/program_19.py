class PowerCalculator:
    def __init__(self, x, n):
        self.x = x
        self.n = n

    def calculate(self):
        result = 1
        for _ in range(self.n):
            result *= self.x
        return result

# Example usage
base = float(input("Enter the base (x): "))
exponent = int(input("Enter the exponent (n): "))
calculator = PowerCalculator(base, exponent)
print(f"{base} to the power of {exponent} is {calculator.calculate()}")
