import numpy as np
from module.universal_functions import get_matrix


def multiply(a, b):
    try:
        result = np.matmul(a, b)
        return np.around(result, 3)
    except ValueError as e:
        print(e)
        exit()


print("Matrix 1")
matrix1 = get_matrix()

print("\nMatrix 2")
matrix2 = get_matrix()

print("\nMultiplication:")
print(multiply(matrix1, matrix2))
