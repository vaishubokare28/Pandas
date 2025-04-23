import pandas
a=pandas.Series(["john","blake","martin"])
print(a) 
#0      john
# 1     blake
# 2    martin
# dtype: object

print(a[0]) #john
print(a[1]) #blake
print(a[2]) #martin

data=pandas.Series(["john","blake","martin"],index=["a","b","c"])
print(data)
# a      john
# b     blake
# c    martin
# dtype: object

print(data.a) #john
print(data['b']) #blake
