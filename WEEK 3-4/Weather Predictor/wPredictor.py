import requests
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime

# WeatherAPI key
API_KEY = "c7a5dd3f877e4851991164619251706"

# Number of past days to check
DAYS = 7

def fetch_weather_data(city, days):
    """Pulls average daily temperatures for the past 'days' days for a given city."""
    weather_data = []

    for i in range(days):
        date = (datetime.datetime.now() - datetime.timedelta(days=i + 1)).strftime("%Y-%m-%d")
        url = "http://api.weatherapi.com/v1/history.json?key=" + API_KEY + "&q=" + city + "&dt=" + date

        response = requests.get(url)

        if response.status_code == 200:
            try:
                data = response.json()
                avg_temp = data['forecast']['forecastday'][0]['day']['avgtemp_c']
                weather_data.append((date, avg_temp))
            except (KeyError, IndexError):
                # If the API didn't return proper data, skip this day
                continue
        else:
            # Invalid city or request error
            return None

    if not weather_data:
        return None

    return pd.DataFrame(weather_data, columns=["date", "temp_c"]).sort_values("date")

def run_weather_prediction():
    while True:
        city_input = input("Enter a city name: ").strip()
        city = city_input.title()

        print("Getting weather data for", city, "...")

        df = fetch_weather_data(city, DAYS)
        if df is not None:
            break
        else:
            print("Could not fetch data. Please enter a valid city.")

    df["day_num"] = range(1, len(df) + 1)

    # Create and train the prediction model
    model = LinearRegression()
    model.fit(df[["day_num"]], df["temp_c"])

    # Predict the temperature for the next day
    next_day = pd.DataFrame([[DAYS + 1]], columns=["day_num"])
    predicted_temp = model.predict(next_day)[0]

    # Plot the results
    plt.plot(df["day_num"], df["temp_c"], marker='o', label="Previous Temperatures")
    plt.plot(DAYS + 1, predicted_temp, marker='x', color='red', label="Predicted: %.2f°C" % predicted_temp)

    plt.xlabel("Day Number")
    plt.ylabel("Average Temperature (°C)")
    plt.title(city + " - Temperature Over Last " + str(DAYS) + " Days and Tomorrow's Prediction")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    print("Predicted average temperature for tomorrow in", city + ":", "%.2f°C" % predicted_temp)

def main():
    print("Welcome to the Simple Weather Forecast Program")
    while True:
        run_weather_prediction()
        again = input("Would you like to check another city? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("Goodbye Habibi.")
            break

if __name__ == "__main__":
    main()
