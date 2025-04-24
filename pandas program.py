# pip install pandas
import pandas as pd
df=pd.read_csv('Iris_missingdata.csv')
print(df)

# #to display all records
# print(df.to_string())

# #to display first 15 records
# print(df.head(15))

# #to display last 7 records
# print(df.tail(7))

# #it returns no of rows and no of columns
# print(df.shape)

# #NaN- return True otherwise it returns False
# print(df.isnull())

# print(df.isnull().sum())

# print(df.fillna("Hello"))

# #delete NaN records
# d4=df.dropna()
# print(d4)

# df

# df.describe()

# #mean()-sum of elements/total no of records
# print(df['SepalLengthCm'].mean())

# print(df['SepalWidthCm'].mean())

# #mode()- it returns frequency of elements
# print(df['SepalWidthCm'].mode())

# #it reurns mid values
# print(df['SepalWidthCm'].median())

# print(df['PetalLengthCm'].mean())

# print(df['PetalLengthCm'].mode())

# print(df['PetalLengthCm'].median())