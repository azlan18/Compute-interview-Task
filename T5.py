import numpy as np

# Reading input as a space separated string and split it into a list of numbers
input_str = input("Enter space-separated numbers: ")
numbers = input_str.split()

# Convert the list of numbers to a NumPy array and reverse it
numpy_array = np.array(numbers, dtype=float)[::-1]

# Print the reversed NumPy array
print(numpy_array)
