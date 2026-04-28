import pandas as pd

# Load dataset from the folder
df = pd.read_csv(r"C:\Users\DELL\Downloads\Internship Project\Module 2\herbal_erp_dataset_11000_realistic.csv")

# -------------------------------
# Convert date columns
# -------------------------------
df['Manufacturing Date'] = pd.to_datetime(df['Manufacturing Date'], errors='coerce')
df['Expiry Date'] = pd.to_datetime(df['Expiry Date'], errors='coerce')

# -------------------------------
# Remove rows with invalid dates
# -------------------------------
df = df.dropna(subset=['Manufacturing Date', 'Expiry Date'])

# -------------------------------
# Remove duplicates
# -------------------------------
df = df.drop_duplicates()

# -------------------------------
# Check missing values
# -------------------------------
print("Missing values:\n", df.isnull().sum())

# Drop remaining null values
df = df.dropna()

# -------------------------------
# Fix data types
# -------------------------------
df['Current Stock'] = pd.to_numeric(df['Current Stock'], errors='coerce')
df['Sales Velocity (units/day)'] = pd.to_numeric(df['Sales Velocity (units/day)'], errors='coerce')

# Remove rows where conversion failed
df = df.dropna()

# -------------------------------
# Remove invalid values
# -------------------------------
df = df[df['Current Stock'] > 0]
df = df[df['Sales Velocity (units/day)'] > 0]
df = df[df['Expiry Date'] > df['Manufacturing Date']]

# -------------------------------
# Reset index
# -------------------------------
df = df.reset_index(drop=True)

# -------------------------------
# Final checking 
# -------------------------------
print("\nCleaned Dataset Info: ")
print(df.info())

print("\nSample Data: ")
print(df.head())

# -------------------------------
# Save preprocessed dataset 
# -------------------------------
df.to_csv(r"C:\Users\DELL\Downloads\Internship Project\Module 2\preprocessed_dataset.csv", index=False)

print("\nPreprocessed dataset saved")


