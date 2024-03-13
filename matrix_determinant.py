from numpy.linalg import det
from module.universal_functions import get_matrix


matrix = get_matrix()
print(det(matrix))
