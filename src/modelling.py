import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
from pathlib import Path

# Load data
data_path = Path("data/Assessment_Parcels.csv")
df = pd.read_csv(data_path)

#display columns
print("Columns in dataset:", df.columns.tolist())


# Clean and prepare numeric columns
df['total_living_area_Num'] = pd.to_numeric(df['total_living_area'], errors='coerce')
df['assessed_land_area_Num'] = pd.to_numeric(df['assessed_land_area'], errors='coerce')
df['total_assessed_value_Num'] = pd.to_numeric(df['total_assessed_value'], errors='coerce')

# Check for missing values
print("Missing values:\n", df[['total_living_area_Num', 'assessed_land_area_Num', 'total_assessed_value_Num']].isna().sum())


# Drop rows with missing values in any of these columns
df = df.dropna(subset=['total_living_area_Num', 'assessed_land_area_Num', 'total_assessed_value_Num'])


# Features and target
X = df[['total_living_area_Num', 'assessed_land_area_Num']]
y = df['total_assessed_value_Num']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_preds = lr.predict(X_test)

# Random Forest Regressor
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_preds = rf.predict(X_test)

def evaluate(model_name, y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return f"{model_name} -> MAE: {mae:,.2f}, R²: {r2:.3f}"

results = [
    evaluate("Linear Regression", y_test, lr_preds),
    evaluate("Random Forest", y_test, rf_preds)
]

# -----------------------------
# Save detailed model evaluation as table
# -----------------------------
eval_df = pd.DataFrame({
    "Model": ["Linear Regression", "Random Forest"],
    "MAE": [
        round(mean_absolute_error(y_test, lr_preds), 2),
        round(mean_absolute_error(y_test, rf_preds), 2)
    ],
    "R2": [
        round(r2_score(y_test, lr_preds), 3),
        round(r2_score(y_test, rf_preds), 3)
    ]
})

# Use existing folder
output_dir = Path("results/outputs")

# Save evaluation table as CSV
eval_file = output_dir / "model_evaluation.csv"
eval_df.to_csv(eval_file, index=False, encoding="utf-8")
print(f"Model evaluation saved to {eval_file}")


# -----------------------------
# Example prediction using Random Forest
# -----------------------------
example_1 = pd.DataFrame({
    "total_living_area_Num": [1500],
    "assessed_land_area_Num": [4000]
})

example_1['predicted_value_Num'] = np.round(rf.predict(example_1), 2)

# Example prediction using Linear Regression
example_2 = pd.DataFrame({
    "total_living_area_Num": [1500],
    "assessed_land_area_Num": [4000]
})
example_2['predicted_value_Num'] = np.round(lr.predict(example_2), 2)


# Save example prediction
example_1.to_csv(output_dir / "example_prediction_rf.csv", index=False)
example_2.to_csv(output_dir / "example_prediction_lr.csv", index=False)

# -----------------------------
# Print results
# -----------------------------
print("\nModel evaluation:")
print("\n".join(results))

print("\nExample prediction for Random Forest:")
print(example_1)

print("\nExample prediction for Linear Regression:")
print(example_2)

# -----------------------------
# Save models
# -----------------------------
#joblib.dump(rf, output_dir / "rf_model.pkl")
joblib.dump(lr, output_dir / "linear_model.pkl")