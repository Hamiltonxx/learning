import numpy as np

vector_row = np.array([1, 2, 3])
vector_column = np.array([[1], [2], [3]])

matrix = np.array([[1, 2, 3], [4, 5, 6]])

print(vector_row.shape)
print(vector_column.shape)
print(matrix.shape)

print(vector_row)
print(vector_column)
print(matrix)

# sparse matrix
# from scipy import sparse
# matrix_sparse = sparse.csr_matrix(matrix)

vector = np.zeros(shape=5)
print(vector)
matrix = np.full(shape=(3,3), fill_value=1)
print(matrix)
matrix_random = np.random.rand(3,3)
print(matrix_random)

print(vector_row[2])
print(matrix[1,1])

matrix = np.array([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12]])
print(matrix.shape)
print(matrix.size)
print(matrix.ndim)

# apply function to all elements
add_100 = np.vectorize(lambda x:x+100)
added = add_100(matrix)
print(added)
print(matrix + 100)

print(np.max(added))
print(np.min(added))
print(np.max(matrix, axis=0))
print(np.max(matrix, axis=1))

print(np.mean(matrix))
print(np.var(matrix))
print(np.std(matrix))

matrix_reshaped = matrix.reshape(2,6)
print(matrix_reshaped)

matrix_transposed = matrix.T 
print(matrix_transposed)

matrix_flattened = matrix.flatten()
print(matrix_flattened)

print(np.linalg.matrix_rank(matrix))
print(matrix.diagonal())

vector_a = np.array([1,2,3])
vector_b = np.array([4,5,6])
print(vector_a @ vector_b)