# Evaluation metrics and plotting for model predictions
import os
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_model(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    print(f"MSE: {mse:.2f}, R2: {r2:.2f}")
    return mse, r2

def plot_predictions(y_true, y_pred, filepath="results/figures/predictions.png"):
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    plt.figure(figsize=(6,6))
    sns.scatterplot(x=y_true, y=y_pred)
    plt.xlabel("True Values")
    plt.ylabel("Predicted Values")
    plt.title("True vs Predicted")
    plt.savefig(filepath)
    plt.close()