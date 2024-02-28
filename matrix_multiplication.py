import numpy as np


def create_matrix():
    matrix_rows = []
    while True:
        row = []
        numbers = input()
        if numbers == "end":
            return matrix_rows
        numbers = numbers.split(",")
        for number in numbers:
            row.append(int(number))
        matrix_rows.append(row)
        

print("Matrix 1")
matrix1 = create_matrix()
a = np.array(matrix1)

print("\nMatrix 2")
matrix2 = create_matrix()
b = np.array(matrix2)

print("\nMultiplication:")
print(np.matmul(a, b))
