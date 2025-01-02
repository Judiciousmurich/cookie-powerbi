import pandas as pd

# Load data
data = pd.read_csv('../data/raw/kevin_cookie_sales.csv')

# Example data cleaning: Remove duplicates, handle missing values, etc.
data = data.drop_duplicates()
data = data.fillna(0) 

# Example: Convert date column to datetime
data['Sale_Date'] = pd.to_datetime(data['Sale_Date'])

# Save cleaned data to a new file
data.to_csv('../data/transformed/kevin_cookie_sales_cleaned.csv', index=False)
print("Data cleaned and saved.")
