# Data cleaning means fixing problems in a 
# dataset before analyzing it.

import pandas as pd

# Missing Values
# A missing value means some data is not available.
# Pandas commonly represents missing values as NaN.
data = {
    "Name": ["Om", "Rahul", "Ankit", "Priya"],
    "Age": [22, None, 21, 24],
    "City": ["Pune", "Mumbai", None, "Pune"]
}
df = pd.DataFrame(data)
print(df,"\n")
# Rahul → Age is missing
# Ankit → City is missing
print(df.isna(),"\n")
print(df.isnull(),"\n")
# Both check for missing values.

# fillna() is used to replace missing values with another value.
df["Age"]=df["Age"].fillna(0)
print(df)
df["City"]=df["City"].fillna("Unknown")
print(df,"\n")

# Filling with the mean
# For numerical data, you can replace missing values
# with the column's mean:
df = pd.DataFrame(data)
df["Age"]=df["Age"].fillna(df["Age"].mean())
print(df,"\n")

# dropna() is used to remove rows containing missing values.
df = pd.DataFrame(data)
df=df.dropna()
print(df,"\n")

# for a particular column
df = pd.DataFrame(data)
df=df.dropna(subset="Age")
print(df, "\n")

# duplicated() checks for duplicate rows.
data = {
    "Name": ["Om", "Rahul", "Ankit", "Priya","Ankit"],
    "Age": [22, None, 21, 24,21],
    "City": ["Pune", "Mumbai", None, "Pune", None]
}
df = pd.DataFrame(data)
print(df,"\n")
print(df.duplicated(),"\n")
# The entire row needs to be duplicate of an existing row 
# True means:
# This row is a duplicate of an earlier row.

# drop_duplicates() actually removes duplicate rows.
print(df.drop_duplicates(),"\n")


# Changing Types — astype()
# Sometimes data is stored using the wrong data type.
# You can check:
print("yo? ",df["Age"].dtype,"\n")
# If you want to convert it to an integer:
# df["Age"] = df["Age"].astype(str)
print(df,"\n")

# .str is used to perform string operations on an entire Pandas column.
df = pd.DataFrame(data)
print(df,"\n")
df["Name"]=df["Name"].str.upper()
print(df,"\n")

# Common .str operations include:
# .str.upper()
# .str.lower()
# .str.strip()
# .str.replace()

# You can rename columns using rename().
df = pd.DataFrame(data)
print(df,"\n")
df=df.rename(columns={
    "City":"Location"
})
print(df,"\n")


data = {
    "Name": ["Om", "Rahul", "Ankit", "Priya", "Neha"],
    "Age": [22, 23, 21, 24, 22],
    "Salary": [35000, 40000, 30000, 45000, 38000],
    "City": ["Pune", "Mumbai", "Delhi", "Pune", "Mumbai"]
}
df = pd.DataFrame(data)

# sort_values() is used to sort rows based on a column.
print(df,"\n")
df=df.sort_values("Age")
print(df,"\n")
df=df.sort_values("Age", ascending=False)
# for descending
print(df,"\n")

# replace() is used to replace specific values with other values.
df["City"] = df["City"].replace("Pune", "Pune City")
# You can replace multiple values using a dictionary:
df["City"] = df["City"].replace({
    "Pune": "Pune City",
    "Mumbai": "Mumbai City"
})

# map() is used to transform each value in a Series
# according to a mapping.
data={
    "City": ["Pune","Mumbai","Delhi","Pune","Mumbai"]
}
df=pd.DataFrame(data)
print(df,"\n")
city_codes = {
    "Pune": "PN",
    "Mumbai": "MU",
    "Delhi": "DL"
}

df["City_Code"] = df["City"].map(city_codes)
print(df,"\n")

# apply() is used to apply a function to each value in a Series.
data = {
    "Name": ["Om", "Rahul", "Ankit", "Priya"],
    "Age": [22, None, 21, 24],
    "City": ["Pune", "Mumbai", None, "Pune"]
}

def age_increace(age):
    return age+1

df=pd.DataFrame(data)
print(df,"\n")
df["Age"]=df["Age"].apply(age_increace)
print(df,"\n")

# Using a lambda function
# You can also write it directly:
# df["Salary"] = df["Salary"].apply(lambda x: x * 1.10)

# value_counts() tells you how many times each value
# appears in a column.
print(df["City"].value_counts(),"\n")

# groupby() is used when you want to divide data into groups
# based on a column and then perform calculations on each group.
data = {
    "Name": ["Om", "Rahul", "Ankit", "Priya", "Neha", "Aman"],
    "Department": ["IT", "HR", "IT", "HR", "IT", "HR"],
    "Salary": [35000, 30000, 40000, 45000, 38000, 32000]
}

df = pd.DataFrame(data)
df=df.groupby("Department")["Salary"].mean()
print(df,"\n")
# syntax:
# df.groupby("column_to_group_by")["column_to_calculate"].calculation()

# agg() means aggregate.
# It allows you to perform multiple calculations at once.
df = pd.DataFrame(data)
print(df,"\n")
df = df.groupby("Department")["Salary"].agg(["max","min"])
print(df,"\n")

# agg() with different functions for different columns
# Suppose we have:
# df=df.groupby("Department").agg({
#     "Salary": ["mean", "max"],
#     "Age": "min"
# })


# merge() is used to combine two DataFrames based on a common column.
employees={
    "ID":[1,2,3,4],
    "Name":["Om","Rahul","Ankit","Priya"]
}
df_employees=pd.DataFrame(employees)
salary={
    "ID":[1,2,3,6],
    "Salary":[300, 400, 500, 100]
}
df_salary=pd.DataFrame(salary)

merge=pd.merge(df_employees,df_salary,on="ID")
print(merge,"\n")
# syntax 
# result = pd.merge(
#     employees,
#     salaries,
#     on="ID", column to join on
#     how="inner" type of join
# )

# Inner Join
# An inner join keeps only the rows where the
# key exists in both DataFrames.

# Left Join
# A left join keeps everything from the left DataFrame,
# and matching data from the right DataFrame.

# Right Join
# A right join keeps everything from the right DataFrame,
# and matching data from the left DataFrame.

# Outer Join
# An outer join keeps everything from both DataFrames.


# concat() is used to stick DataFrames together.
# Unlike merge(), it doesn't primarily match rows using a common key.
concat=pd.concat([df_salary,df_employees], ignore_index=True)
# ignore_index is to keep a consitant index for the entire
# Concated table
print(concat,"\n")
concat=pd.concat([df_salary,df_employees], ignore_index=False, axis=1)
# the ignore index with axis 1 turns the column names to id too
# soo we keep it false 
print(concat,"\n")

# join() is another way to combine DataFrames,
# usually using their index.
employees = pd.DataFrame({
    "Name": ["Om", "Rahul", "Ankit"],
    "Age": [22, 23, 21]
}, index=[1, 2, 3])

salary = pd.DataFrame({
    "Salary": [35000, 40000, 30000]
}, index=[1, 2, 3])
print(employees,"\n")
print(salary,"\n")
result = employees.join(salary)
print(result,"\n")
# join by default performs left join
# You can specify another type:
# employees.join(salary, how="inner")
# employees.join(salary, how="right")
# employees.join(salary, how="outer")

# join()
# Combine mainly based on index.


data = {
    "Name": ["Om", "Rahul", "Ankit", "Priya"],
    "JoiningDate": ["2024-01-15", "2024-05-20", "2025-02-10", "2025-08-25"]
}
df = pd.DataFrame(data)
# pd.to_datetime() converts values into Pandas' datetime format.
print(df["JoiningDate"].dtype,"\n")
df["JoiningDate"]=pd.to_datetime(df["JoiningDate"])
print(df["JoiningDate"].dtype,"\n")
# The column is now treated as actual dates rather than ordinary text.
# Once Pandas recognizes the values as dates, you can easily:
# Extract year/month/day
# Compare dates
# Filter dates
# Sort dates


# extracting year month and day from this 
print(df["JoiningDate"].dt.year,"\n")
print(df["JoiningDate"].dt.month,"\n")
print(df["JoiningDate"].dt.day,"\n")

# Once the column is datetime, you can filter rows based on dates.
# For example, get employees who joined after January 1, 2025:
# df[df["JoiningDate"] > "2025-01-01"]

# Filtering within a date range
# Suppose you want dates between January 1 and June 30, 2025:
# df[
#     (df["JoiningDate"] >= "2025-01-01") &
#     (df["JoiningDate"] <= "2025-06-30")
# ]


data = {
    "Name": ["Om", "Rahul", "Ankit", "Priya", "Neha", "Aman"],
    "Age": [22, 23, 21, 24, 22, 25],
    "Salary": [35000, 40000, 30000, 45000, 38000, 500000],
    "City": ["Pune", "Mumbai", "Delhi", "Pune", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data)

# Correlation measures how two numerical variables are related.
print(df["Age"].corr(df["Salary"]),"\n")
# print(df["Age"].corr(df["City"]),"\n")
# strings can not be compared

# The result is between:
# -1 and +1
# Positive correlation
# If one variable tends to increase when the other increases:
# Negative correlation
# If one tends to increase while the other decreases:

# You can also calculate correlations between all numerical columns:
# df.corr(numeric_only=True)
# Important
# Correlation does not mean causation.
# If two things are correlated, it doesn't automatically mean one
# causes the other.


# Unique values are the different values that appear in a column.
print(df["City"].unique(),"\n")

# Number of unique values
print(df["City"].nunique(),"\n")

# value_counts() tells you how many times each value appears.
print(df["Age"].value_counts(),"\n")


# Finding outliers using IQR
# A common method is the IQR (Interquartile Range).
q1=df["Salary"].quantile(.25)
q3=df["Salary"].quantile(.75)

iqr=q3-q1

low=q1-1.5*iqr
high=q3+1.5*iqr

print(df[(
    (df["Salary"]<low) |
    (df["Salary"]>high)
)],"\n")

# EDA = Exploratory Data Analysis.
# It means:
# Exploring a dataset to understand what's 
# inside it before doing deeper analysis.

# Simple EDA Workflow
# Dataset
#    ↓
# head()
#    ↓
# shape
#    ↓
# columns / dtypes
#    ↓
# missing values
#    ↓
# duplicates
#    ↓
# describe()
#    ↓
# unique values / counts
#    ↓
# mean / median
#    ↓
# correlation
#    ↓
# outliers
#    ↓
# Understand the dataset