# Temperature Conversion: Celsius <-> Fahrenheit

# Convert Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(celsius, "°C is", fahrenheit, "°F")

# Convert Fahrenheit to Celsius
fahrenheit = float(input("\nEnter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(fahrenheit, "°F is", celsius, "°C")
