import numpy as np

# Fungsi Jacobi
def jacobi_method(A, b, epsilon, max_iterations):
    n = len(b)
    x = np.zeros(n)  # Inisialisasi awal x (semua nol)
    x_new = np.zeros(n)
    
    for iteration in range(max_iterations):
        for i in range(n):
            sigma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sigma) / A[i][i]
        
        # Hitung error relatif
        error = np.linalg.norm(x_new - x, ord=np.inf) / np.linalg.norm(x_new, ord=np.inf)
        if error < epsilon:
            return x_new, iteration + 1
        
        x = x_new.copy()
    
    raise ValueError("Metode Jacobi tidak konvergen dalam jumlah iterasi maksimum.")