import numpy as np

# Given array
arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print("Original Array:\n\n\n", arr)
print("-" * 40)

# 1. Extract the second row
second_row = arr[1]
print("1. Second Row:\n\n\n", second_row)
print("-" * 40)
# 2. Extract the first two rows and the second two columns
first_two_rows_second_two_cols = arr[0:2, 2:4]
print("2. First two rows and second two columns:\n\n\n", first_two_rows_second_two_cols)
print("-" * 40)
# 3. Extract the last column using slicing
last_column = arr[:, -1]
print("3. Last Column:\n\n\n", last_column)
print("-" * 40)
# 4. Replace the middle row with [1, 2, 3, 4]
arr[1] = [1, 2, 3, 4]
print("4. Array after replacing middle row:\n\n\n", arr)
print("-" * 40)