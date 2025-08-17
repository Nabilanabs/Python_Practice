# Function to multiply matrices
def multiply_matrices(A, B):
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    
    # Initialize result matrix with zeros
    result = [[0 for _ in range(p)] for _ in range(m)]
    
    # Multiply
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Example matrices
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]

# Multiply matrices
result = multiply_matrices(A, B)

# Print result
print("Result of multiplication:")
for row in result:
    print(row)
