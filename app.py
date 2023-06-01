import requests
from datetime import datetime, timedelta

 # Make a request to the OpenWeatherMap API to retrieve the weather forecast by returning a json data
def get_weather_forecast(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city_name,  # Specify the city name for the forecast
        "appid": api_key,  # Include your OpenWeatherMap API key
        "units": "metric"  # Use metric units for temperature
    }
# Send the API request
    response = requests.get(base_url, params=params) 
# Parse the response as JSON
    weather_data = response.json()  

    # Extract the relevant weather information from the API response like date temeperaute and other features
    forecast = []
    for prediction in weather_data["list"]:
        forecast.append({
            "date": datetime.fromtimestamp(prediction["dt"]),
            "description": prediction["weather"][0]["description"],
            "temp_min": prediction["main"]["temp_min"],
            "temp_max": prediction["main"]["temp_max"],
            "humidity": prediction["main"]["humidity"]
        })
    return forecast


#print weather forecast
def print_weather_forecast(forecast):

#print the forecast header for the five days along with details in a for loop
    print("-" * 68)
    print(f" Weather forecast for {forecast[0]['date'].strftime('%A, %B %d')}")
    print("-" * 68)
    print("TIME        DESCRIPTION                          TEMP (C)    HUMIDITY")
    print("-" * 68)

     # Print each of the forecasts for the next five days in a for loop for 12 hour time intervals
    for daily_forecast in forecast:
        date_string = daily_forecast["date"].strftime("%H:%M")
        description = daily_forecast["description"].capitalize()
        temperature = daily_forecast["temp_max"]
        humidity = daily_forecast["humidity"]
        print(f"{date_string:8}    {description:30} {temperature:6}      {humidity:6}%")
    print("-" * 68)


#give the main function
def main():
    # Enter your OpenWeatherMap API key here
    api_key = '2fd12545a95e925217919cfe171a10a6'

    # Prompt the user to enter a city name
    city_name = input("Enter the name of a city whose weather you want to see: ")

    # Get the weather forecast for the next five days
    forecast = get_weather_forecast(city_name, api_key)
    
    # Print the forecast to the screen
    print_weather_forecast(forecast)

if name == 'main':
    main()
