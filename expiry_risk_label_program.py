import pandas as pd

# -----------------------------------
# 1. Load the feature engineered dataset
# -----------------------------------
df = pd.read_csv(r"C:\Users\DELL\Downloads\Internship Project\Module 2\feature_engineered_dataset.csv")

# -----------------------------------
# 2. Define risk classification logic
# -----------------------------------
def risk_level(row):
    if row['Stock_Cover_Days'] > row['Days_Remaining']:
        return "High"
    elif row['Stock_Cover_Days'] > 0.7 * row['Days_Remaining']:
        return "Medium"
    else:
        return "Low"

# -----------------------------------
# 3. Apply function to create target column
# -----------------------------------
df['Expiry Risk Level'] = df.apply(risk_level, axis=1)

# -----------------------------------
# 4. Check distribution of risk levels
# -----------------------------------
print("\nRisk Level Distribution:\n")
print(df['Expiry Risk Level'].value_counts())

# -----------------------------------
# 5. Preview dataset
# -----------------------------------
print("\nSample Data:\n")
print(df[['Days_Remaining', 'Stock_Cover_Days', 'Expiry Risk Level']].head())

# -----------------------------------
# 6. Save the final dataset
# -----------------------------------
df.to_csv(r"C:\Users\DELL\Downloads\Internship Project\Module 2\final_dataset.csv", index=False)

print("\nFinal dataset with Expiry Risk Level is saved successfully")

