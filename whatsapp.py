"""
=====================================
WHATSAPP MODULE
Developer : Harish
=====================================
"""

import pywhatkit
import time
from speech import speak


def send_whatsapp(number, message):

    try:

        speak("Opening WhatsApp.")

        pywhatkit.sendwhatmsg_instantly(
            phone_no=number,
            message=message,
            wait_time=20,
            tab_close=True,
            close_time=5
        )

        time.sleep(3)

        speak("Message sent successfully.")

    except Exception as e:

        print("WhatsApp Error:", e)
        speak("Unable to send WhatsApp message.")