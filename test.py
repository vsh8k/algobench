import numpy as np

# Example array
my_array = np.array([4, 7, 1, 9, 3, 9, 8, 4, 6, 10])

# Calculate the index to sort up to 95%
index_to_sort = int(len(my_array) * 0.99)

# Partially sort up to the calculated index
sorted_array = np.partition(my_array, index_to_sort)

# Print the result
print("Original array:", my_array)
print("Partially sorted array (95%):", sorted_array)