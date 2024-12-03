import numpy as np
from method import jacobi_method

# Matriks koefisien (A) dan vektor konstanta (b)
A = np.array([
    [3, -1, 2],
    [2, 3, -1],
    [1, -2, 3]
])
b = np.array([20, 15, 11])

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