import pandas
data={"rollno":[1,2],"name":["sachin","ramesh"]}
first=pandas.DataFrame(data)

data={"rollno":[1,2],"marks":[90,70]}
second=pandas.DataFrame(data)

mergeresult=first.merge(second)
print(mergeresult)