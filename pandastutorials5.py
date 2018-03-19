import pandas as pd
index = [('California', 2000), ('California', 2010),
         ('New York', 2000), ('New York', 2010),
         ('Texas', 2000), ('Texas', 2010)]
populations = [33871648, 37253956,
               18976457, 19378102,
               20851820, 25145561]
index = pd.MultiIndex.from_tuples(index)
pop = pd.Series(populations, index=index)
print(index)
print(pop)

index = pd.MultiIndex.from_tuples(index)

pop = pop.reindex(index)
print(pop)

pop_df = pd.DataFrame({'total': pop,
                       'under18': [9267089, 9284094,
                                   4687374, 4318033,
                                   5906301, 6879014]})
pop_df
print(pop_df)
