#Example file for EDA


import pandas as pd
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.data_processing import load_data
import seaborn as sns
import matplotlib.pyplot as plt

df = load_data("data/assessment_parcels.csv")


# Check first 10 rows and datatype of total assessed value
print(df['total_assessed_value'].head(10))
print(df['total_assessed_value'].dtype)



print(df.columns)

# Basic statistics for Total assessed value

statistics_eda = df['total_assessed_value'].describe().to_frame(name = 'Total Assessed Value Stats')
print(statistics_eda)

print(df['total_assessed_value'].isnull().sum())


# Hist plot of assessed values
plt.figure(figsize=(10,6))
sns.histplot(df['total_assessed_value'],
             bins=50,
             log_scale=True,
             color='grey')
plt.xlabel("Total Assessed Value (Logged Scale)")
plt.title("Assessed Value Distribution")
plt.savefig("results/figures/assessed_value_distribution.png")
plt.close()

statistics_eda.to_csv("results/outputs/eda_statistics.csv")