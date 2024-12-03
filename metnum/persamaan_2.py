import numpy as np
from method import jacobi_method

# Matriks koefisien (A) dan vektor konstanta (b)

A = np.array([
    [2, -1, 3, -1],
    [1, 2, -1, 2],
    [3, 1, -4, 1],
    [4, -3, -2, 3]
])
b = np.array([17, 11, 4, 9])

# Toleransi epsilon
epsilon = 0.001

# Maximum Iterasi
max_iterations = 100

# Menyelesaikan SPL menggunakan metode Jacobi
try:
    solution, iterations = jacobi_method(A, b, epsilon, max_iterations)
    print("Solusi:", solution)
    print("Jumlah iterasi:", iterations)
except ValueError as e:
    print(e)