from datetime import datetime

from speech import speak


def tell_time():

    current = datetime.now().strftime("%I:%M %p")

    speak(f"The current time is {current}")


def tell_date():

    current = datetime.now().strftime("%d %B %Y")

    speak(f"Today's date is {current}")


def tell_day():

    current = datetime.now().strftime("%A")

    speak(f"Today is {current}")