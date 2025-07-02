WEATHER PREDICTOR 
---------------------

This Python script uses the WeatherAPI to fetch past 7 days of weather data 
for any city and predicts tomorrow’s average temperature using a simple 
linear regression model.

---------------------
FEATURES
---------------------
- Uses real weather data from WeatherAPI
- Predicts tomorrow's temperature based on last 7 days
- Visual graph with matplotlib
- Built-in retry if user enters an invalid city
- Command-line interface

---------------------
HOW TO RUN
---------------------
1. Open terminal or command prompt.
2. Run the script:
   python weather.py
3. Enter any city name when prompted.
4. View a graph and predicted temperature for tomorrow.

---------------------
REQUIREMENTS
---------------------
Install the following libraries if not already installed:

   pip install requests pandas matplotlib scikit-learn

---------------------
HOW IT WORKS
---------------------
- Fetches average daily temperature for the last 7 days
- Uses linear regression to find the temperature trend
- Predicts the 8th day (tomorrow) based on the trend
- Plots the actual vs predicted temperatures using matplotlib

---------------------
API INFO
---------------------
- This uses a free API key from https://www.weatherapi.com/
- Make sure to replace the default API_KEY in the script with your own
- Note: Free keys are limited to 7-day history and limited requests

---------------------
TO DO / IDEAS
---------------------
- Add option to save graph or output
- Export results to CSV
- Use other ML models (Random Forest, SVR)
- Add future forecast mode

---------------------
AUTHOR
---------------------
Created by Arham during Week 2 of the Python AI.
