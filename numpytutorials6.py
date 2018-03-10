import numpy as np
rand = np.random.RandomState(42)

x = rand.randint(100, size=10)
print(x)

print([x[3], x[7], x[2]])

X = np.arange(12).reshape((3, 4))
row = np.array([0, 1, 2])
col = np.array([2, 1, 3])
print(X[row, col])
