# Define a function to accept a matrix of integers from the user
def get_matrix(prompt, rows, cols):
    print(prompt)
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter value for row {i+1}, column {j+1}: "))
            row.append(value)
        matrix.append(row)
    return matrix

# Accept two matrices from the user
rows = int(input("Enter the number of rows for both matrices: "))
cols = int(input("Enter the number of columns for both matrices: "))
matrix1 = get_matrix("Enter the values for matrix 1:", rows, cols)
matrix2 = get_matrix("Enter the values for matrix 2:", rows, cols)

# Calculate and display row sums for both matrices
print("Row sums:")
for i in range(rows):
    row_sum1 = sum(matrix1[i])
    row_sum2 = sum(matrix2[i])
    print(f"Matrix 1: {row_sum1}, Matrix 2: {row_sum2}")

# Calculate and display column sums for both matrices
print("Column sums:")
for j in range(cols):
    col_sum1 = sum(matrix1[i][j] for i in range(rows))
    col_sum2 = sum(matrix2[i][j] for i in range(rows))
    print(f"Matrix 1: {col_sum1}, Matrix 2: {col_sum2}")

# Calculate and display diagonal sums for both matrices
print("Diagonal sums:")
diag_sum1 = sum(matrix1[i][i] for i in range(min(rows, cols)))
diag_sum2 = sum(matrix2[i][i] for i in range(min(rows, cols)))
print(f"Matrix 1: {diag_sum1}, Matrix 2: {diag_sum2}")

# Calculate and display addition of both matrices
print("Matrix addition:")
addition_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]
for row in addition_matrix:
    print(row)

# Calculate and display multiplication of both matrices
print("Matrix multiplication:")
multiplication_matrix = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(cols)) for j in range(cols)] for i in range(rows)]
for row in multiplication_matrix:
    print(row)
