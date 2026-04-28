import pandas as pd

# -----------------------------------
# 1. Load the preprocessed dataset
# -----------------------------------
df = pd.read_csv(r"C:\Users\DELL\Downloads\Internship Project\Module 2\preprocessed_dataset.csv")

# -----------------------------------
# 2. Convert the date columns 
# -----------------------------------
df['Manufacturing Date'] = pd.to_datetime(df['Manufacturing Date'])
df['Expiry Date'] = pd.to_datetime(df['Expiry Date'])

# -----------------------------------
# 3. Set Optimal reference date
# -----------------------------------
today = pd.to_datetime("2025-06-30")

# -----------------------------------
# 4. Create Days Remaining
# -----------------------------------
df['Days_Remaining'] = (df['Expiry Date'] - today).dt.days

# Handle negative values (for already expired)
df['Days_Remaining'] = df['Days_Remaining'].apply(lambda x: max(x, 0))

# -----------------------------------
# 5. Create Stock Cover Days
# -----------------------------------
df['Stock_Cover_Days'] = df['Current Stock'] / df['Sales Velocity (units/day)']

# -----------------------------------
# 6. Estimated Sales before expiry
# -----------------------------------
df['Estimated_Sales'] = df['Sales Velocity (units/day)'] * df['Days_Remaining']

# -----------------------------------
# 7. Estimated Unsold Quantity
# -----------------------------------
df['Estimated_Unsold_Quantity'] = df['Current Stock'] - df['Estimated_Sales']

# Avoid negative values
df['Estimated_Unsold_Quantity'] = df['Estimated_Unsold_Quantity'].apply(lambda x: max(x, 0))

# -----------------------------------
# 8. Final checking
# -----------------------------------
print("\nSample Data with New Features:\n")
print(df[['Days_Remaining', 'Stock_Cover_Days', 'Estimated_Unsold_Quantity']].head())

print("\nDataset Info:\n")
print(df.info())

print("\nStatistics:\n")
print(df[['Days_Remaining', 'Stock_Cover_Days']].describe())

# -----------------------------------
# 9. Save the feature engineered dataset
# -----------------------------------
df.to_csv(r"C:\Users\DELL\Downloads\Internship Project\Module 2\feature_engineered_dataset.csv", index=False)

print("\nFeature engineered dataset saved successfully")


