import numpy as np


# Python code to compute the inner inner product and norm
x = np.array([[1], [0], [-1]])
y = np.array([[3], [2], [0]])

z = np.dot(np.transpose(x), y)
print(z)
