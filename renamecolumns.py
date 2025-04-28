import pandas as pd
students={"firstname":["john","jane","jade"],
      "lastname":["deo","done","do"]
      }

#convert student names into dataframe

df=pd.DataFrame(students)
print(df)

df=df.rename(columns={"firstname":"fname","lastname":"lname"})
print(df)