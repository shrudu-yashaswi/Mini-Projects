import requests

# Replace with your API key
API_KEY = "1cc54911f8459b6f1ce1014f11a65e06"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

# Build request URL
url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    main = data['main']
    temperature = main['temp']
    humidity = main['humidity']
    description = data['weather'][0]['description']
    print(f"\nWeather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {description}")
else:
    print("❌ City not found or error in API request.")