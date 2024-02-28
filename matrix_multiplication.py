import numpy as np


def string_to_number(number):
    try:
        return int(number)
    except ValueError:
        return float(number)

def create_matrix():
    matrix_rows = []
    while True:
        row = []
        numbers = input()
        if numbers == "end":
            return matrix_rows
        numbers = numbers.split(",")
        for number in numbers:
            row.append(string_to_number(number))
        matrix_rows.append(row)
        
def multiply(a, b):
    try:
        result = np.matmul(a, b)
        return result
    except ValueError as e:
        print(e)
        exit()


print("Matrix 1")
matrix1 = create_matrix()
a = np.array(matrix1)

print("\nMatrix 2")
matrix2 = create_matrix()
b = np.array(matrix2)

print("\nMultiplication:")
print(multiply(a, b))
