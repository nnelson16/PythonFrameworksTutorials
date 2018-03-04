import numpy as np

#integer array
x1 = np.array([1, 2, 3, 4, 5])


#explicitly set data type
x2 = np.array([1, 2, 3, 4], dtype='float32')


x3 = np.array([range(i, i + 3) for i in [2, 4, 6]])

x4 = np.zeros(10, dtype=int)

x5 = np.ones((3, 5), dtype=float)

x6 = np.full((3, 5), 3.14)

x7 = np.arange(0, 20, 2)

x8 = np.linspace(0, 1, 5)

x9 = np.random.random((3, 3))

x10 = np.random.normal(0, 1, (3, 3))

x11 = np.random.randint(0, 10, (3, 3))

x12 = np.eye(3)

x13 = np.empty(3)
print(x13)
