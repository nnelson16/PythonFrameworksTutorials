import pandas as pd

def make_df(cols, ind):
    """Quickly make a DataFrame"""
    data = {c: [str(c) + str(i) for i in ind]
            for c in cols}
    return pd.DataFrame(data, ind)

# example DataFrame
print(make_df('ABC', range(3)))

ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
print(pd.concat([ser1, ser2]))

df1 = make_df('AB', [1, 2])
df2 = make_df('AB', [3, 4])

print(pd.concat([df1, df2]))

df5 = make_df('ABC', [1, 2])
df6 = make_df('BCD', [3, 4])

print(pd.concat([df5, df6], join='inner'))
