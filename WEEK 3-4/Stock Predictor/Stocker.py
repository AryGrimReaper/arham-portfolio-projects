import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings

# Suppress all warnings (including FutureWarning from yfinance)
warnings.filterwarnings("ignore")

# Top 20 stocks
stocks = {
    "1": "AAPL",   # Apple
    "2": "MSFT",   # Microsoft
    "3": "GOOGL",  # Alphabet
    "4": "AMZN",   # Amazon
    "5": "TSLA",   # Tesla
    "6": "META",   # Meta Platforms
    "7": "NFLX",   # Netflix
    "8": "NVDA",   # NVIDIA
    "9": "JPM",    # JPMorgan
    "10": "AMD",   # AMD
    "11": "BABA",  # Alibaba
    "12": "INTC",  # Intel
    "13": "DIS",   # Disney
    "14": "V",     # Visa
    "15": "MA",    # Mastercard
    "16": "PEP",   # PepsiCo
    "17": "KO",    # Coca-Cola
    "18": "WMT",   # Walmart
    "19": "PYPL",  # PayPal
    "20": "NKE"    # Nike
}

def get_interval():
    print("Choose how you want the x-axis to be shown:")
    print("1. Daily")
    print("2. 5-Day")
    print("3. Monthly")
    print("4. Yearly")
    while True:
        interval_choice = input("Enter a number (1-4): ").strip()
        if interval_choice == "1":
            return "daily"
        elif interval_choice == "2":
            return "5d"
        elif interval_choice == "3":
            return "monthly"
        elif interval_choice == "4":
            return "yearly"
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

def analyze_stock(stock):
    # Extended start date to allow yearly resampling
    df = yf.download(stock, start="2023-01-01", end="2024-06-01", auto_adjust=False)

    df.columns = [col if isinstance(col, str) else col[0] for col in df.columns]

    df["Tomorrow"] = df["Close"].shift(-1)
    df.dropna(inplace=True)
    df.reset_index(inplace=True)
    df["Target"] = (df["Tomorrow"].to_numpy() > df["Close"].to_numpy()).astype(int)
    df["Open-Close"] = df["Open"] - df["Close"]
    df["High-Low"] = df["High"] - df["Low"]

    X = df[["Close", "Volume", "Open-Close", "High-Low"]]
    y = df["Target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    last_row = X.iloc[-1:]
    if not last_row.empty:
        prediction = model.predict(last_row)[0]
        direction = "UP" if prediction == 1 else "DOWN"
        print("Prediction for", stock, "tomorrow:", direction)
    else:
        print("Not enough data to make a prediction.")

    interval = get_interval()

    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)

    if interval == "daily":
        df_resampled = df
    elif interval == "5d":
        df_resampled = df.resample("5D").mean()
    elif interval == "monthly":
        df_resampled = df.resample("M").mean()
    elif interval == "yearly":
        df_resampled = df.resample("Y").mean()
    else:
        df_resampled = df

    df_resampled["Close"].plot(title=stock + " Closing Prices", figsize=(10, 5))
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.grid(True)
    plt.show()

while True:
    print("Choose a stock to analyze:")
    for key, ticker in stocks.items():
        print(key + ".", ticker)

    stock = None
    while not stock:
        choice = input("Enter a number (1-20): ").strip()
        if choice in stocks:
            stock = stocks[choice]
        else:
            print("Invalid choice. Please enter a number between 1 and 20.")

    analyze_stock(stock)

    again = input("Would you like to analyze another stock? (yes/no): ").strip().lower()
    if again != "yes":
        print("Exiting.")
        break
