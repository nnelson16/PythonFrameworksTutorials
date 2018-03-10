import numpy as np


x = np.array([1, 2, 3, 4, 5])
print(x < 3)

rng = np.random.RandomState(0)
x = rng.randint(10, size=(3, 4))
print(x)
print(np.count_nonzero(x < 6))
print(np.sum(x < 6, axis=1))
