import pandas as pd
df = pd.read_csv("data/raw_superstore.csv")
print(df.info())
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True, errors='coerce')
df['Postal Code'] = df['Postal Code'].fillna(0)
df = df.drop_duplicates()
df['Order Year'] = df['Order Date'].dt.year
df['Order Month'] = df['Order Date'].dt.month
df.to_csv("data/cleaned_superstore.csv", index=False)
print("Data cleaning completed successfully!")
