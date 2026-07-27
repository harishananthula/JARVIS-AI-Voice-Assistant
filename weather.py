import requests

from config import WEATHER_API_KEY
from speech import speak


def get_weather(city):

    if city == "":
        speak("Please tell me the city name.")
        return

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={WEATHER_API_KEY}&units=metric"
    )

    try:

        response = requests.get(url)

        data = response.json()

        print("\nAPI Response:")
        print(data)

        if str(data.get("cod")) != "200":
            speak(data.get("message", "Unable to get weather information."))
            return

        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        message = (
            f"The weather in {city} is {description}. "
            f"The temperature is {temperature:.1f} degrees Celsius. "
            f"It feels like {feels_like:.1f} degrees. "
            f"The humidity is {humidity} percent."
        )

        print(message)

        speak(message)

    except Exception as e:

        print(e)

        speak("Unable to get weather information.")