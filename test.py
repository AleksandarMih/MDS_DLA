import numpy as np
matrix=np.zeros((15, 10))
matrix2=np.zeros((3, 3))
col, row = np.meshgrid(np.arange(3), np.arange(3))
matrix_2D = np.zeros((5, 5))
seeds = np.linspace(0,5-1,3,dtype=int)
col, row = np.meshgrid(np.arange(5), np.arange(5))
matrix_2D[4, seeds] = 1
matrix_2D[row <= 2] = 2
print(matrix_2D)