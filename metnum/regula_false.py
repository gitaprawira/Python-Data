def fungsi(x):
    return x**3 + 4*x**2 - 10

def regula_false(a, b, tolerance, iter):
    if fungsi(a) * fungsi(b) >= 0:
        print("Tidak ada akar di interval ini.")
        return None

    while True:
        # Hitung titik palsu
        c = (a * fungsi(b) - b * fungsi(a)) / (fungsi(b) - fungsi(a))
        # Hitung nilai fungsi di titik palsu
        fc = fungsi(c)
        iter += 1

        # Periksa apakah toleransi sudah terpenuhi
        if abs(fc) < tolerance:
            return print(f"Akar yang ditemukan: {c} pada iterasi ke: {iter}")

        # Memperbarui interval
        if fungsi(a) * fc < 0:
            b = c  # Akar terletak di [a, c]
        else:
            a = c  # Akar terletak di [c, b]

# Interval awal dan toleransi
a = 1
b = 2
iter = 0
tolerance = 0.001
regula_false(a, b, tolerance, iter)