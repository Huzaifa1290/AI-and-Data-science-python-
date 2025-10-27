import numpy as np

# 1(a) Zero matrix of size 4×4
zeros_matrix = np.zeros((4, 4))
print("a) Zero Matrix (4x4):\n", zeros_matrix)
print("-" * 40)

# 1(b) One matrix of size 3×2
ones_matrix = np.ones((3, 2))
print("b) One Matrix (3x2):\n", ones_matrix)
print("-" * 40)

# 1(c) Identity matrix of size 5×5
identity_matrix = np.eye(5)
print("c) Identity Matrix (5x5):\n", identity_matrix)
print("-" * 40)

# 1(d) Constant values array filled with 7
constant_array = np.full((3, 3), 7)
print("d) Constant Array filled with 7 (3x3):\n", constant_array)
print("-" * 40)

# 1(e) Random integer array of size (3×4), with values between 10 and 99
random_int_array = np.random.randint(10, 100, size=(3, 4))
print("e) Random Integer Array (3x4):\n", random_int_array)
print("-" * 40)

# 2. Using np.arange() to generate array from 5 to 50 with step size 5
arange_array = np.arange(5, 55, 5)  # Includes 5, 10, ..., 50
reshaped_array = arange_array.reshape(3, 3)

print("Array from 5 to 50 with step size 5:\n", arange_array)
print("Reshaped Array (3x3):\n", reshaped_array)
