# Data loading and preprocessing

import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:
    """Load and clean the property data from a CSV file."""
    return pd.read_csv(filepath)

if __name__ == "__main__":
    df = load_data("data/assessment_parcels.csv")
    print(df.head())