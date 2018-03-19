import pandas as pd
import numpy as np

rng = np.random.RandomState(42)
ser = pd.Series(rng.randint(0, 10, 4))
print(ser)

df = pd.DataFrame(rng.randint(0, 10, (3, 4)), columns=['A', 'B', 'C', 'D'])
print(df)

print(np.sin(df * np.pi / 4))

area = pd.Series({'Alaska': 1723337, 'Texas': 695662,
                  'California': 423967}, name='area')
population = pd.Series({'California': 38332521, 'Texas': 26448193,
                        'New York': 19651127}, name='population')

print(population / area)

A = pd.DataFrame(rng.randint(0, 20, (2, 2)),
                 columns=list('AB'))

B = pd.DataFrame(rng.randint(0, 10, (3, 3)),
                 columns=list('BAC'))


print(A+B)

A = rng.randint(10, size=(3, 4))

df = pd.DataFrame(A, columns=list('QRST'))
halfrow = df.iloc[0, ::2]
print(A)
print(halfrow)
print(df-halfrow)
