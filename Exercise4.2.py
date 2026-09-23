import numpy as np 
import pandas as pd

matrix1 = np.array([[2,3],[5,7]])
matrix2 = np.array([[11,13],[17,19]])

m1rows, m1cols = matrix1.shape
m2rows, m2cols = matrix2.shape

if m1rows == m2cols and m1cols == m2rows: 
    dim = max(m1rows, m1cols)
    matrix_dot = np.zeros([dim,dim])

loop_iter = dim**2
num = 0
row_index = 0
col_index = 0

for n in range(loop_iter): 
    