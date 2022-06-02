import pandas as pd

df = pd.read_json("movies.json")
print(df)


df.to_csv("movies.csv")
