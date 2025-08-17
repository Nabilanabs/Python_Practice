# Input the three sides
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Sort sides so the largest is last
sides = sorted([a, b, c])
if sides[2]**2 == sides[0]**2 + sides[1]**2:
    print("This is a right triangle.")
else:
    print("This is NOT a right triangle.")
