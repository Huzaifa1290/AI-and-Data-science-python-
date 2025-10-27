import numpy as np
import time

# Create a normal Python list of 100000 numbers
python_list = list(range(100000))

# Create a NumPy array of the same numbers
numpy_array = np.arange(100000)

# Measure time for Python list
start_time = time.time()
python_result = [x * 5 for x in python_list]
python_time = time.time() - start_time

# Measure time for NumPy array
start_time = time.time()
numpy_result = numpy_array * 5
numpy_time = time.time() - start_time

# Display results
print(f"Time taken by Python list: {python_time:.6f} seconds")
print(f"Time taken by NumPy array: {numpy_time:.6f} seconds")

# Compare which is faster
if numpy_time < python_time:
    print("✅ NumPy is faster than Python lists!")
else:
    print("⚙️ Python lists are faster this time (rare case).")
