import pandas as pd

data = {
    'apples': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}

purchases = pd.DataFrame(data)

print(type(purchases))
print(purchases)

print(50*'-')

purchases = pd.DataFrame(data, index=["Tom", "Alex", "Mike", "John"])

print(type(purchases))
print(purchases)
print(50*'-')
print(purchases.loc["Alex"])
