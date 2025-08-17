# Constructing the given star pattern using nested loops

rows = 5  # maximum stars in the middle row

# Increasing part
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Decreasing part
for i in range(rows - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
