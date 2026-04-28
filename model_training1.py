import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# -----------------------------------
# 1. Load the final dataset
# -----------------------------------
df = pd.read_csv(r"C:\Users\DELL\Downloads\Internship Project\Module 2\final_dataset.csv")

# -----------------------------------
# 2. Select the input features and target variables
# -----------------------------------
X = df[['Current Stock',
        'Sales Velocity (units/day)',
        'Days_Remaining',
        'Stock_Cover_Days']]

y = df['Expiry Risk Level']

# -----------------------------------
# 3. Encode the target labels
# -----------------------------------
le = LabelEncoder()
y = le.fit_transform(y)

# -----------------------------------
# 4. Split the dataset into training and testing sets
# -----------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------------
# 5. Train using Logistic Regression model
# -----------------------------------
lr_model = LogisticRegression(max_iter=1000, class_weight='balanced')
lr_model.fit(X_train, y_train)

# -----------------------------------
# 6. Train using Random Forest model
# -----------------------------------
rf_model = RandomForestClassifier(n_estimators=100, class_weight='balanced')
rf_model.fit(X_train, y_train)

# -----------------------------------
# 7. To get Predictions
# -----------------------------------
lr_pred = lr_model.predict(X_test)
rf_pred = rf_model.predict(X_test)

# -----------------------------------
# 8. To evaluate the models
# -----------------------------------
print("\nLogistic Regression Accuracy:", accuracy_score(y_test, lr_pred))
print("\nRandom Forest Accuracy:", accuracy_score(y_test, rf_pred))

print("\nRandom Forest Classification Report:\n")
print(classification_report(y_test, rf_pred))

# -----------------------------------
# 9. To save the best model for using
# -----------------------------------
joblib.dump(rf_model, r"C:\Users\DELL\Downloads\Internship Project\Module 2\expiry_risk_prediction_model.pkl")

print("\nExpiry Risk Prediction Model is saved successfully")

