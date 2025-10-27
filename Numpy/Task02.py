import numpy as np

# 1. Create arrays
array_1D = np.arange(1, 11)                # 1D array from 1 to 10
array_2D = np.arange(1, 10).reshape(3, 3)  # 2D array 3x3 from 1 to 9

# 2. Display properties for both arrays
print("1D Array:", array_1D)
print("Dimensions:", array_1D.ndim)
print("Shape:", array_1D.shape)
print("Size (total elements):", array_1D.size)
print("Data Type:", array_1D.dtype)
print("Item Size (bytes per element):", array_1D.itemsize)
print("-" * 40)

print("2D Array:\n", array_2D)
print("Dimensions:", array_2D.ndim)
print("Shape:", array_2D.shape)
print("Size (total elements):", array_2D.size)
print("Data Type:", array_2D.dtype)
print("Item Size (bytes per element):", array_2D.itemsize)
print("-" * 40)

# 3. Create a 3x3 array of floats and convert it to integers
float_array = np.array([[1.2, 2.5, 3.9],
                        [4.7, 5.1, 6.8],
                        [7.3, 8.6, 9.0]])

int_array = float_array.astype(int)  # Convert float → int

print("Float Array:\n", float_array)
print("Converted Integer Array:\n", int_array)
