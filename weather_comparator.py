# weather_comparator.py
# This Python script compares the weather (temperature) of multiple cities using OpenWeatherMap API

import requests

# API key for OpenWeatherMap (replace 'YOUR_OPENWEATHERMAP_API_KEY' with your actual API key)
API_KEY = 'YOUR_OPENWEATHERMAP_API_KEY'

def get_weather_data(city):
    """
    Fetches weather data for a given city from OpenWeatherMap API.
    
    Args:
    city (str): Name of the city to fetch the weather for.
    
    Returns:
    dict: Contains the city name, temperature, and weather description.
    """
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        # Extracting the required data (temperature and description)
        city_name = data['name']
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        return {"city": city_name, "temperature": temperature, "description": description}
    else:
        # Return None if city is not found or there's an error
        return None

def compare_temperatures(cities):
    """
    Compares the temperatures of multiple cities.
    
    Args:
    cities (list): A list of city names to compare weather for.
    """
    weather_data = [] # To store weather data for all cities
    
    # Fetch and store weather data for each city
    for city in cities:
        data = get_weather_data(city)
        if data:
            weather_data.append(data)
        else:
            print(f"Could not retrieve weather data for city: {city}")
    
    # Check if we have at least two cities' data
    if len(weather_data) < 2:
        print("Not enough data to compare.")
        return
    
    # Find the city with the highest temperature
    hottest_city = max(weather_data, key=lambda x: x['temperature'])
    
    # Display the comparison result
    print("\nWeather comparison between cities:")
    for data in weather_data:
        print(f"{data['city']} - {data['temperature']}°C, {data['description']}")
    
    print(f"\nThe hottest city is {hottest_city['city']} with {hottest_city['temperature']}°C.")

# Main function to run the script
if __name__ == "__main__":
    # Ask the user for city names, separated by commas
    cities_input = input("Enter city names separated by commas: ")
    cities_list = [city.strip() for city in cities_input.split(",")]
    
    # Compare the weather of the provided cities
    compare_temperatures(cities_list)
# API Key Setup:

The script uses OpenWeatherMap API to fetch weather data. Replace YOUR_OPENWEATHERMAP_API_KEY with your actual API key from OpenWeatherMap.
get_weather_data(city):

This function fetches the weather data for a city, such as temperature and description.
If the city is not found or there is an error, it returns None.
compare_temperatures(cities):

This function accepts a list of cities, fetches the weather for each, and then compares their temperatures.
It finds and prints the hottest city among the list of provided cities.
It handles errors such as cities not found and ensures there are at least two cities to compare.
Main Block:

The script prompts the user to input city names separated by commas. It then calls the compare_temperatures() function to fetch and compare the weather data for those cities.
