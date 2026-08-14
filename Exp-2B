import pandas as pd

# Load dataset into a DataFrame
df = pd.read_csv("data.csv")

# Display first and last few rows
print("First 5 rows:\n", df.head())
print("Last 5 rows:\n", df.tail())

# Check data types and general information
df.info()

# Summary statistics
print("Summary statistics:\n", df.describe())

# Handle missing values
numeric_columns = df.select_dtypes(include="number").columns
df[numeric_columns] = df[numeric_columns].fillna(
    df[numeric_columns].mean()
)

# Create a new column
df["Reviews_Doubled"] = df["Reviews"] * 2

# Create a Series and perform operations
series = df["Reviews"]
print("Series addition:\n", series + 10)

# Filter rows based on conditions
filtered_df = df[
    (df["Reviews"] > 50) &
    (df["Rating"] < 5)
]

print("Filtered DataFrame:\n", filtered_df)

# Grouping and aggregation
grouped = df.groupby("Category")["Rating"].mean()
print("Grouped mean:\n", grouped)

# Sorting
df_sorted = df.sort_values(
    by="Rating",
    ascending=False
)

print("Sorted DataFrame:\n", df_sorted)

# Boolean masking
masked_df = df[
    df["Rating"] > df["Rating"].median()
]

print("Masked DataFrame:\n", masked_df)

# Remove duplicate rows and drop missing values
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Create a new DataFrame with selected columns
subset_df = df[
    ["App", "Category", "Rating", "Reviews"]
]

# Save the new DataFrame to a CSV file
subset_df.to_csv(
    "filtered_data.csv",
    index=False
)

# Compute summary statistics
print("Total Reviews:", df["Reviews"].sum())
print("Mean Rating:", df["Rating"].mean())
print("Standard Deviation of Rating:", df["Rating"].std())
