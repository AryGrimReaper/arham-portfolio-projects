import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import os

def load_data():
    try:
        if os.path.exists("housing.csv"):
            df = pd.read_csv("housing.csv")
        else:
            # Fallback data
            data = {
                "size": [2100, 1600, 2400, 1400, 3000, 1800],
                "bedrooms": [3, 2, 4, 2, 4, 3],
                "age": [15, 10, 5, 20, 8, 12],
                "price": [400000, 330000, 490000, 299000, 540000, 350000]
            }
            df = pd.DataFrame(data)
        return df
    except Exception as e:
        print("Failed to load data:", e)
        return None

def train_model(df):
    try:
        X = df[["size", "bedrooms", "age"]]
        y = df["price"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LinearRegression()
        model.fit(X_train, y_train)

        score = model.score(X_test, y_test)
        return model, score, X_test, y_test
    except Exception as e:
        print("Could not train the model:", e)
        return None, None, None, None

def predict_price(model):
    try:
        size = int(input("Enter the size of the house in sq ft: "))
        bedrooms = int(input("Enter number of bedrooms: "))
        age = int(input("Enter the age of the house in years: "))

        # Use DataFrame with correct feature names to avoid warning
        features = pd.DataFrame([[size, bedrooms, age]], columns=["size", "bedrooms", "age"])
        prediction = model.predict(features)[0]

        print(f"Predicted house price is around ${round(prediction)}")
    except ValueError:
        print("Please enter valid numeric inputs.")
    except Exception as e:
        print("Something went wrong while predicting:", e)

def plot_predictions(model, X_test, y_test):
    try:
        y_pred = model.predict(X_test)

        plt.scatter(y_test, y_pred, color='skyblue', edgecolor='black')
        plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
        plt.xlabel("Actual Price")
        plt.ylabel("Predicted Price")
        plt.title("Actual vs Predicted House Prices")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print("Failed to plot predictions:", e)

def main():
    print("Welcome to the House Price Predictor")

    df = load_data()
    if df is None:
        return

    model, score, X_test, y_test = train_model(df)
    if model is None:
        return

    print(f"Model trained successfully. Accuracy: {round(score * 100, 2)}%")

    while True:
        print("\n Menu")
        print("1. Predict a price")
        print("2. Visualize predictions")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            predict_price(model)
        elif choice == "2":
            plot_predictions(model, X_test, y_test)
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input. Please choose 1, 2 or 3.")

if __name__ == "__main__":
    main()
