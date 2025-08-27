import numpy as np

# Creating Arrays in NumPy
a = np.array([1, 2, 3])
print(a)

#The type of the array can be checked using the type function, which will return numpy.ndarray.
b = np.array([[1, 2, 3], [4, 5, 6]])

# The type remains ndarray, but the interpreter recognizes it as a two-dimensional array.
a = np.array([1, 2, 3], dtype=float)
print(a)

# Similarly, you can set the data type to string:
a = np.array([1, 2, 3], dtype=str)
print(a)
print(len(a))
print(a.ndim)

# Array Shape and Data Type
print(a.shape)
print(a.dtype)

# Accessing and Modifying Array Elements
# You can access or change specific elements, rows, and columns in NumPy arrays using indexing and slicing.



