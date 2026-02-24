import pandas as pd
std_data = [
    ("John", 85),
    ("Alice", 92),
    ("Bob", 78),
    ("Eve", 90)
]
df=pd.DataFrame(std_data, columns=["Name", "Score"])
print(df)
print(df.head())
print(df.tail())
print(df.shape)
print(df.describe())
print(df.dtypes())
print(df.index())