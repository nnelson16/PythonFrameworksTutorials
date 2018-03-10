import numpy as np

def selection_sort(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x

x = np.array([2, 1, 4, 3, 5])
print(selection_sort(x))

x = np.array([2, 1, 4, 3, 5])
print(np.sort(x))

x = np.array([2, 1, 4, 3, 5])
i = np.argsort(x)
print(i)

x = np.array([7, 2, 3, 1, 6, 5, 4])
print(np.partition(x, 3))
