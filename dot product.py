import numpy as np

# Function to create a matrix
def create_matrix(n):
    print("\nEnter the number of rows and columns for Matrix", n)
    row = int(input("Rows : "))
    col = int(input("Columns : "))

    print("Enter", row * col, "elements:")
    elements = list(map(int, input().split()))

    if len(elements) != row * col:
        print("Invalid number of elements!")
        return create_matrix(n)

    matrix = np.array(elements).reshape(row, col)

    print("\nMatrix", n)
    print(matrix)

    return matrix

# Input first matrix
matrix1 = create_matrix(1)

# Input second matrix
matrix2 = create_matrix(2)

# Check dimensions for matrix multiplication
if matrix1.shape[1] == matrix2.shape[0]:
    result = np.dot(matrix1, matrix2)
    print("\nDot Product (Matrix Multiplication):")
    print(result)
else:
    print("\nMatrix multiplication is not possible.")
    print("Number of columns of Matrix 1 must be equal to the number of rows of Matrix 2.")