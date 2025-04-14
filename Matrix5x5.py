# Matriks A (5x5)
A = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [10, 9, 8, 7, 6],
    [5, 4, 3, 2, 1],
    [2, 4, 6, 8, 10]
]

# Matriks B (5x5)
B = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1]
]

hasil = []
for i in range(5):
    baris = []  # Menyimpan satu baris hasil
    for j in range(5):
        total = 0
        for k in range(5):
            total += A[i][k] * B[k][j]
        baris.append(total)
    hasil.append(baris)

# Tampilkan hasil perkalian
print("\nHasil Perkalian Matriks A x B:\n")
for baris in hasil:
    print(baris)

