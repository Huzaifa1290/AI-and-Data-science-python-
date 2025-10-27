import numpy as np

# Create a 3×3 matrix
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Original Matrix A:\n", A)
print("Shape of A:", A.shape)
print("-" * 40)

# 1(a) Add 10 (scalar broadcasting)
# Prediction: shape will remain (3, 3)
add_scalar = A + 10
print("A + 10:\n", add_scalar)
print("Shape:", add_scalar.shape)
print("-" * 40)

# 1(b) Add a row vector [1, 2, 3] (row broadcasting)
# Prediction: shape will remain (3, 3)
row_vector = np.array([1, 2, 3])
add_row = A + row_vector
print("A + [1, 2, 3]:\n", add_row)
print("Shape:", add_row.shape)
print("-" * 40)

# 1(c) Add a column vector [[1], [2], [3]] (column broadcasting)
# Prediction: shape will remain (3, 3)
column_vector = np.array([[1], [2], [3]])
add_column = A + column_vector
print("A + [[1], [2], [3]]:\n", add_column)
print("Shape:", add_column.shape)
