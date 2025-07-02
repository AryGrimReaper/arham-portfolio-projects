import requests

# actual API key
api_key = "e152859dbd231f1314cb27ec2502bceb"
base_url = "http://api.openweathermap.org/data/2.5/weather"

while True:
    city = input("Enter your city (or type 'exit' to quit): ")
    
    if city.lower() == "exit":
        print("Exiting weather checker.")
        break

# Parameters for the request
    params = {
    "q": city,
    "appid": api_key,
    "units": "metric"  # Use "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            print("Weather in " + city + ": " + weather)
            print("Temperature: " + str(temperature) + "°C")
        else:
           print("City not found or API error.")
    except:
        print("There was a problem connecting to the API.")

