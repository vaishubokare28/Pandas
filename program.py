import pandas as pd

# Sample Data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Age': [20, 21, 19, 22, 20, 23],
    'Gender': ['F', 'M', 'M', 'M', 'F', 'M'],
    'Marks': [85, 78, 92, 88, 76, 95],
    'Subject': ['Math', 'Science', 'Math', 'English', 'Science', 'Math'],
    'Grade': ['B', 'C', 'A', 'B', 'C', 'A']
}

# Load data into a DataFrame
df = pd.DataFrame(data)

# Explore the data
print("DataFrame:")
print(df)

print("\nData Information:")
print(df.info())

print("\nData Description:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Display Marks mean, mode, and median
print("\nMarks Statistics:")
print(f"Mean: {df['Marks'].mean()}")
print(f"Mode: {df['Marks'].mode()[0]}")
print(f"Median: {df['Marks'].median()}")
