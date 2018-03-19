import numpy as np
import pandas as pd


data = pd.Series([1, np.nan, 'hello', None])
print(data.isnull())
print(data.dropna())

data = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
print(data)
print(data.fillna(0))
