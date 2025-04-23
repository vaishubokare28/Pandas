import pandas as pd
student={
    "name":["john","blake","martin"],
    "marks":[56,67,78],
    "city":["pune","mumbai","nagar"]
}

df=pd.DataFrame(student)
print(df)
#      name  marks    city
# 0    john     56    pune
# 1   blake     67  mumbai
# 2  martin     78   nagar