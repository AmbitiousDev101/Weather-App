import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
      
    if response.status_code == 200:
        data = response.json()    #JSON to python dictionary 
        
        weather = {                                  # Extracting weather information
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather
    else:
        return None

api_key = 'API_KEY'  #Replace 'API_KEY' with an OpenWeatherMap API key (You can get it by signing up for free, make sure it is quoted as a string)
city = input("Enter the name of the city: ")
weather_info = get_weather(city, api_key)

if weather_info:  #not None
    print(f"City: {weather_info['city']}")
    print(f"Temperature: {weather_info['temperature']}°C")
    print(f"Weather: {weather_info['description'].capitalize()}")
    print(f"Humidity: {weather_info['humidity']}%")
    print(f"Wind Speed: {weather_info['wind_speed']} m/s")
else:
    print("Could not retrieve weather data. Please check the city name or API key.")
