from src.api.weather_api import fetch_weather
from src.alerts.alert_engine import generate_alerts

city = input("Enter City Name: ")

data = fetch_weather(city)

if data:

    temp = data["current"]["temp_c"]
    humidity = data["current"]["humidity"]
    condition = data["current"]["condition"]["text"]
    wind = data["current"]["wind_kph"]

    alerts = generate_alerts(
        temp,
        humidity,
        condition,
        wind
    )

    print("\n🌦 WEATHER REPORT")
    print("-" * 30)

    print(f"City: {city}")
    print(f"Temperature: {temp} °C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {condition}")
    print(f"Wind Speed: {wind} kph")

    print("\n🚨 ALERTS")

    for alert in alerts:
        print(alert)

else:
    print("❌ Unable To Fetch Weather Data")