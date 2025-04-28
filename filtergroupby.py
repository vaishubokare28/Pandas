import pandas
data={
    "name":["sachin","rahul","virendra","sourav"],
    "department":["it","it","comp","comp"],
    "salary":[1000,2000,3000,4000]
}
dataframe=pandas.DataFrame(data)
print(dataframe)

#result=dataframe.groupby("department").filter(lambda record:record["salary"].sum()>4000)

result=dataframe.groupby("department").filter(lambda record:record["salary"].sum()<4000)
#select department ,count (department) from employee group by department having sum(salary)<4000 ;

#select department ,count (department) from employee group by department;
# it    2
# comp  2

print(result)