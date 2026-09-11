import pandas as pd

# Pandas is mainly used to work with 
# tabular data — data arranged in rows and columns.

# There are two broad ways to get data into Pandas:
# 1. Create data yourself
data = {
    "Name": ["Om", "Rahul", "Ankit"],
    "Age": [22, 23, 21],
    "City": ["Pune", "Mumbai", "Delhi"]
}

print(data)

df=pd.DataFrame(data)
print(df)
# 2. Load existing data
# students.csv
# students.xlsx
# students.json
# Pandas provides functions to load these files:

# ->pd.read_csv()
#"Read this CSV file and convert its 
# contents into a Pandas DataFrame."

# CSV stands for Comma-Separated Values.
# A CSV file might look like this:
# Name,Age,City
# Om,22,Pune
# Rahul,23,Mumbai
# Ankit,21,Delhi

# ->pd.read_excel()
# Excel files can contain multiple sheets.
# For example:
# students.xlsx
# Sheet 1 → Students
# Sheet 2 → Marks
# Sheet 3 → Attendance
# You can specify which sheet to load:

# df = pd.read_excel(
#     "students.xlsx",
#     sheet_name="Marks"
# )

# You can also use the sheet number:
# df = pd.read_excel(
#     "students.xlsx",
#     sheet_name=1
# )

# ->pd.read_json()


# Series
# A Series is essentially a single column of data.
names = pd.Series(["Om", "Rahul", "Ankit"])
print(names)

# You can specify the index yourself:
names = pd.Series(
    ["Om", "Rahul", "Ankit"],
    index=["a", "b", "c"]
)
print(names)
print(names["a"])
# Series = one-dimensional labeled data.

# An important relationship is:
# A DataFrame is made up of multiple Series (columns).
# Dataframes are 2D

df=pd.read_csv("Pandas/Datasets/pokemon.csv")
# This tries to find the file from the current dir rather than
# the position from the file being executed
# print(df)

# head() shows the first 5 rows of a DataFrame by default.
print(df.head(3))

# tail() does the opposite.
# It shows the last 5 rows by default.
print(df.tail(3))

# df.shape
# shape tells you the size of the DataFrame.
print(df.shape)

# df.columns tells you the names of all columns.
print(df.columns)

# to convert the columns to a normal list 
print(df.columns.tolist())

# dtypes tells you the data type of each column.
print(df.dtypes)
# object
# Usually represents text/string data in Pandas.
# Newer Pandas versions distinguish more clearly between:
# object — a general Python/object dtype
# str — actual string data

# df.info with one command, you get a quick overview of:
# Number of rows
# Number of columns
# Column names
# Missing values
# Data types
# Memory usage
print(df.info())

# describe() gives you statistical information about numerical columns.
print(df.describe())
# By default, describe() mainly focuses on numerical columns.

# You can also specifically describe categorical/text columns:
df.describe(include="str")

# Selecting one column — df["column"]
# To select a single column:
print(df["Name"])

# Selecting multiple columns
# To select multiple columns, pass a list of column names:
print(df[["Name", "HP"]])

# .loc[] is used to select data using labels.
# The basic syntax is:
# df.loc[row, column]
print(df.loc[0, "Name"])

# Selecting an entire row
print(df.loc[1])
# Selecting multiple rows
print(df.loc[0:2]) #end is inclusive

# Selecting specific rows and columns
print(df.loc[0:2, ["Name", "Type 1"]])


# .iloc[] is used to select data based on integer position.
# .loc → label
# .iloc → position
print(df.iloc[0,1])

# Selecting a row
print(df.iloc[0])

# Selecting multiple rows
print(df.iloc[0:3])
# With .iloc, the ending position is not included.

# Selecting rows and columns
print(df.iloc[0:3, 0:2])


# Boolean filtering
print(df["Type 1"]=="Fire")
# this only classifies if the row is true or not
print(df[df["Type 1"]=="Fire"])
# this uses the classification to choose only true vals
