#example file for EDA

import pandas as pd
from src.data_loader import load_data
import seaborn as sns
import matplotlib.pyplot as plt

df = load_data("data/assessment_parcels.csv")

# Podstawowa eksploracja
print(df.describe())

# Histogram ceny
plt.figure(figsize=(6,4))
sns.histplot(df['price'], bins=50)
plt.title("Price Distribution")
plt.savefig("results/figures/price_distribution.png")
plt.close()