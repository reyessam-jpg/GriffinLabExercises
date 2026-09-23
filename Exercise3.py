import numpy as np 
import pandas as pd

matrix1 = np.array([[2,3],[5,7]])
matrix2 = np.array([[11,13],[17,19]])

matrix_add_A = matrix1 + matrix2
print(matrix_add_A)

matrix_add_B = np.zeros([2,2])

matrix_add_B[0,0] = matrix1[0,0] + matrix2[0,0]
matrix_add_B[0,1] = matrix1[0,1] + matrix2[0,1]
matrix_add_B[1,0] = matrix1[1,0] + matrix2[1,0]
matrix_add_B[1,1] = matrix1[1,1] + matrix2[1,1]

print(matrix_add_B)

matrix_dot = matrix1 @ matrix2
print(matrix_dot)

std_add = matrix1 + matrix2
std_sub = matrix1 - matrix2
elem_mult = matrix1 * matrix2
print(std_add, std_sub, matrix_dot, elem_mult, sep='\n')

