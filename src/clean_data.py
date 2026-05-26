import pandas as pd


df = pd.read_csv("data/insurance_data.csv")

# Example cleaning
df = df.drop_duplicates()

# Fill missing numeric values
numeric_cols = df.select_dtypes(include="number").columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Save cleaned data
df.to_csv(
    "data/insurance_data_cleaned.csv",
    index=False
)

print("Cleaned dataset saved.")
