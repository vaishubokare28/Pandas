import pandas
data={
    "name":["sachin","rahul","virendra","sourav"],
    "department":["it","it","comp","comp"],
    "salary":[1000,2000,3000,4000]
}
dataframe=pandas.DataFrame(data)
print(dataframe)

groups=dataframe.groupby("department")

for department ,group in groups:
    print(department,"\n",group)   #
#select department ,count (department) from employee group by department;

print(groups["salary"].sum())
print(groups["salary"].sum().reset_index())