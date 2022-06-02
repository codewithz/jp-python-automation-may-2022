import pandas as pd


df = pd.read_csv("blog_dataset.csv")
print(df)

print(30*'-')
print(df.head(6))

print(30*'-')
print(df.tail(4))

print(30*'-')
print(df.describe())
# describe() lists out different descriptive statistical measures
# for all numerical columns in our dataset

print(30*'-')
print(df.memory_usage(deep=True))

print(30*'-')
df['Gender'] = df.Gender.astype('category')
df['Name'] = df.Name.astype('string')
print(df)

print(30*'-')
print(df.dtypes)

print(30*'-')
print(df.loc[1])
print(df.loc[0:4, ['Name', 'Age', 'Gender']])

print(30*'-')
print(df['DOB'])
print(30*'-')
df['DOB'] = pd.to_datetime(
    df['DOB'], infer_datetime_format=False, format='%d-%m-%Y')
print(df['DOB'])

print(30*'-')
print(df['State'].value_counts())

print(30*'-')
df.drop_duplicates(inplace=True)
print(df)

print(30*'-')
print(df.groupby(by='State').Salary.mean())
