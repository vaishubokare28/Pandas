import pandas
data={"name":["sachine","rahul","virendra","sourav"],
      "department":["it","it","comp","comp"],
      "slaray":[2000,1000,3000,4000]}

result=pandas.DataFrame(data)
print(result)

print(result.dtypes) #dtypes-it returns data type in dataframe

#iloc-integer indexing
print(result.iloc[0,1])

print(result.iloc[2,2]) #iloc[row index,column index]
#dataframes iloc property accept row index and column index and gives value present at it