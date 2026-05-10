def generate_alerts(temp, humidity, weather_condition, wind_speed):

    alerts = []

    if temp > 35:
        alerts.append("🔥 High Temperature Alert")

    if humidity > 80:
        alerts.append("💧 High Humidity Alert")

    if "rain" in weather_condition.lower():
        alerts.append("🌧 Rain Alert")

    if wind_speed > 40:
        alerts.append("🌪 High Wind Alert")

    if temp < 5:
        alerts.append("❄ Cold Weather Alert")

    if not alerts:
        alerts.append("✅ Weather Conditions Normal")

    return alerts