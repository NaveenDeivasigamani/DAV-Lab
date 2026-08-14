import pandas as pd

# Read data from a CSV/text file
text_df = pd.read_csv("Google_data (2b.c1).csv")

# Read data from an Excel file
excel_df = pd.read_excel(
    "data (2c2).xlsx",
    sheet_name="Sheet1"
)

# Read data from a web-based source
web_df = pd.read_csv(
    "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
)

# Display the first few rows of each dataset
print("Text/CSV Data:")
print(text_df.head())

print("\nExcel Data:")
print(excel_df.head())

print("\nWeb Data:")
print(web_df.head())

# Handle missing values
text_df = text_df.ffill()
excel_df = excel_df.bfill()
web_df = web_df.dropna()

# Save processed data
text_df.to_csv(
    "processed_text.csv",
    index=False
)

excel_df.to_excel(
    "processed_excel.xlsx",
    index=False
)

print("\nProcessed files saved successfully.")
