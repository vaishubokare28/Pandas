#series class is for 1d array
#dataframe class is for  2d array

import pandas
data={
    "name":["sachin","rahul","virendra","sourav"],
    "department":["it","it","comp","comp"],
    "salary":[1000,2000,3000,4000]
}
df=pandas.DataFrame(data)
# print(df)
selectecolunsdata=df.filter(items=["name"])  #select name from employee;
print(selectecolunsdata)

filterbasecondition=df[df["salary"]>2000] #select * from employee where salary>2000;
print(filterbasecondition)

filterbasedcondition=df[(df["salary"]>1000) & (df["department"]=="it")]#select * from employee where salary>1000 and department="it"
print(filterbasedcondition)

sortedresult=df.sort_values(by="name") #select *from employee order by name;
print(sortedresult)