import pandas as pd

df = pd.read_csv("data_products.csv")

print(df)
df.to_json("data_products.json")
print(50*'-')

df = pd.read_csv("data_products.csv", index_col=0)
print(df)
