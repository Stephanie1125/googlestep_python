from random import randint
import time
from functions import *

matrix_a = []
matrix_b = []
matrix_c = []

print("Let's create N*N matrix with built in rules!")
n = int(input("input a number N to generate N*N matrix > "))

# Initialize the matrices to all 0
for x in range(n):
    matrix_a.append([0] * n)
    matrix_b.append([0] * n)
    matrix_c.append([0] * n)

# assign values to matrix a & b follow rules
for i in range(n):
    for j in range(n):
        matrix_a[i][j] = i * n + j
        matrix_b[i][j] = j * n + i
        matrix_c[i][j] = 0

begin = time.time()

# test multiplication1 in functions.py
matrix_c = multiplication1(matrix_a, matrix_b)

end = time.time()

print("matrix c (%d * %d matrix) : " % (n, n))
print_matrix(matrix_c)
print("time: %.6f sec" % (end - begin))

total = 0
for i in range(n):
    for j in range(n):
        total += matrix_c[i][j]

print("sum: %.6f" % total)

