import numpy as np

# 1. Create array from 1–12 and reshape it
arr = np.arange(1, 13)
print("Original 1D Array:\n", arr)

reshaped_3x4 = arr.reshape(3, 4)
print("\nReshaped to (3x4):\n", reshaped_3x4)

reshaped_2x6 = arr.reshape(2, 6)
print("\nReshaped to (2x6):\n", reshaped_2x6)
print("-" * 40)

# 2. Using flatten() and ravel()
array_2D = np.array([[1, 2, 3], [4, 5, 6]])

flat_array = array_2D.flatten()  # returns a copy
ravel_array = array_2D.ravel()   # returns a view (if possible)

print("Original 2D Array:\n", array_2D)
print("Flattened Array:", flat_array)
print("Raveled Array:", ravel_array)

# Modify flattened and raveled arrays
flat_array[0] = 99
ravel_array[1] = 77

print("\nAfter modifying:")
print("Flattened Array:", flat_array)
print("Raveled Array:", ravel_array)
print("Original 2D Array after modification:\n", array_2D)
print("-" * 40)

# 3. Given array (3x3) → Convert to 1D
arr2 = np.arange(1, 10).reshape(3, 3)
print("Original 3x3 Array:\n", arr2)

flattened = arr2.flatten()
raveled = arr2.ravel()

print("Flattened 1D Array:", flattened)
print("Raveled 1D Array:", raveled)

# Modify raveled array
raveled[0] = 999
print("\nAfter modifying raveled array:")
print("Raveled:", raveled)
print("Original Array (affected?):\n", arr2)
