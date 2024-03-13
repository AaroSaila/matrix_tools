import numpy as np


def string_to_number(number):
    try:
        return int(number)
    except ValueError:
        return float(number)

def get_matrix():
    matrix_rows = []
    while True:
        row = []
        numbers = input()
        if numbers == "end":
            break
        numbers = numbers.split()
        for number in numbers:
            row.append(string_to_number(number))
        matrix_rows.append(row)
    matrix = np.array(matrix_rows)
    return matrix
