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
