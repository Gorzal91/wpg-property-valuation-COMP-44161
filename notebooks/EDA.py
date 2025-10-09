#example file for EDA

import pandas as pd
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.data_processing import load_data
import seaborn as sns
import matplotlib.pyplot as plt

df = load_data("data/assessment_parcels.csv")

print(df['total_assessed_value'].head(10))
print(df['total_assessed_value'].dtype)



print(df.columns)
# Basic statistics
print(df.describe())
print(df['total_assessed_value'].min())
print(df['total_assessed_value'].max())
print(df['total_assessed_value'].mean())


# Hist plot of assessed values
plt.figure(figsize=(10,6))
sns.histplot(df['total_assessed_value'], bins=25, log_scale= True)
plt.xlabel("Total Assessed Value")
plt.title("Assessed Value Distribution")
plt.savefig("results/figures/price_distribution.png")
plt.close()