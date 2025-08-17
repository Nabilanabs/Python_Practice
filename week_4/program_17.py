# Input the file name
file_name = input("Enter the file name: ")

# Read file and collect unique words
with open(file_name, 'r') as file:
    words = file.read().split()

unique_words = sorted(set(words))  # Remove duplicates and sort

# Print unique words
print("Unique words in alphabetical order:")
for word in unique_words:
    print(word)
