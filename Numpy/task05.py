import numpy as np

# 1. Element-wise operations (Vectorized)
A = np.random.randint(1, 20, 5)
B = np.random.randint(1, 20, 5)

print("Array A:", A)
print("Array B:", B)
print("-" * 40)

print("Addition:", A + B)
print("Subtraction:", A - B)
print("Multiplication:", A * B)
print("Division:", A / B)
print("-" * 40)

# 2. Apply mathematical functions using vectorization
arr = np.random.randint(1, 10, 5)
print("Original Array:", arr)

sqrt_arr = np.sqrt(arr)
exp_arr = np.exp(arr)
sin_arr = np.sin(arr)

print("Square Root:", sqrt_arr)
print("Exponential:", exp_arr)
print("Sine:", sin_arr)
print("-" * 40)

# 3. Celsius to Fahrenheit conversion (vectorized)
celsius = np.array([0, 10, 20, 25, 30, 35, 40, 50, 60, 100])
fahrenheit = (celsius * 9/5) + 32

print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)
