import pandas as pd
df=pd.read_csv("student.csv")
print(df)
#       name  marks  age    city
# 0     john     78   23    pune
# 1  martine     88   20  mumbai
# 2    blake     89   21   nagar

import pandas as pd
data=pd.read_csv("course.csv")
print(data)
#    id     courses
# 0   1      python
# 1   2        java
# 2   3  mern stack
# 3   4     testing
# 4   5       cloud

import pandas as pd
read=pd.read_csv("Iris_missingdata.csv")
print(read)
#      Id  SepalLengthCm  ...  PetalWidthCm         Species
# 0      1            5.1  ...           0.2     Iris-setosa
# 1      1            5.1  ...           0.2     Iris-setosa
# 2      2            4.9  ...           0.2     Iris-setosa
# 3      3            4.7  ...           0.2     Iris-setosa
# 4      4            NaN  ...           0.2     Iris-setosa
# ..   ...            ...  ...           ...             ...
# 147  146            6.7  ...           2.3  Iris-virginica
# 148  147            6.3  ...           1.9  Iris-virginica
# 149  148            6.5  ...           2.0  Iris-virginica
# 150  149            6.2  ...           2.3  Iris-virginica
# 151  150            5.9  ...           1.8  Iris-virginica

# [152 rows x 6 columns]