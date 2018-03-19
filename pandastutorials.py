import numpy as np
import pandas as pd

data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data)
print(data.values)
print(data.index)

data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
print(data)

population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
population = pd.Series(population_dict)
print(population)
print(population['California'])
print(population['California':'Illinois'])

area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
             'Florida': 170312, 'Illinois': 149995}
area = pd.Series(area_dict)

states = pd.DataFrame({'population': population, 'area': area})
print(states)
print(states.index)
print(states.columns)
print(states['area'])

data = [{'a': i, 'b': 2 * i} for i in range(3)]
print(pd.DataFrame(data))

print(pd.DataFrame(np.random.rand(3, 2), columns=['foo', 'bar']
    , index=['a', 'b', 'c']))

ind = pd.Index([2, 3, 5, 7, 11])
print(ind)
