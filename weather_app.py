import requests

API_KEY = "610b92da2c9fa607b0df534797daa6e5"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    wind = data["wind"]["speed"]
    country = data["sys"]["country"]

    print("\nWeather Information")
    print("-------------------")
    print("City:", city, ",", country)
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Wind Speed:", wind, "m/s")
    print("Condition:", description)

else:
    print("Error:", data["message"])