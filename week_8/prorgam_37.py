import csv

# Read the CSV file
file_name = input("Enter the CSV file name: ")

with open(file_name, 'r') as file:
    reader = list(csv.reader(file))  # Convert to list for easy indexing

# Print first 5 rows
print("First 5 rows:")
for row in reader[:5]:
    print(row)

# Print last 5 rows
print("\nLast 5 rows:")
for row in reader[-5:]:
    print(row)
