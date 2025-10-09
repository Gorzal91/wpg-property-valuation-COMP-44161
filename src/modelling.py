from sklearn.linear_model import LinearRegression
import joblib

def train_linear_model(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model

def save_model(model, filepath):
    joblib.dump(model, filepath)

if __name__ == "__main__":
    # Example usage (to be replaced with actual data loading and preprocessing)
    pass