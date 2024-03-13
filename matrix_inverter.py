import numpy as np
from numpy.linalg import inv
from module.universal_functions import get_matrix

print("Matrix:")
matrix = get_matrix()
inverted_matrix = inv(matrix)
inverted_matrix = np.around(inverted_matrix, 3)
print("\nInverted:")
print(inverted_matrix)
