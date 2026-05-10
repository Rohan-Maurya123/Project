import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

BASE_URL = "http://api.weatherapi.com/v1/current.json"


def fetch_weather(city):

    params = {
        "key": API_KEY,
        "q": city
    }

    try:
        response = requests.get(BASE_URL, params=params)

        response.raise_for_status()

        return response.json()

    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)

    except requests.exceptions.ConnectionError as errc:
        print("Connection Error:", errc)

    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)

    except requests.exceptions.RequestException as err:
        print("Request Error:", err)

    return None