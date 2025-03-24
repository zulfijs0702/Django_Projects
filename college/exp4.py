import requests
api_key = "9ca9b5aca134652bae0f6927aef1b742"
city = "city"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url)
if response.status_code == 200:
    weather_data = response.json()
    print(f"Temperature: {weather_data['main'] ['temp']}K")
    print(f"Weather: {weather_data['weather'] [0] ['description']}")
else:
    print("Failed to fetch weather data.")