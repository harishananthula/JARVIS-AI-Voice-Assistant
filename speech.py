"""
=========================================
SPEECH MODULE
Developer : Harish
=========================================
"""

import pyttsx3
import speech_recognition as sr

from config import USER_NAME, ASSISTANT_NAME
from config import VOICE_INDEX, SPEECH_RATE


# ==========================================
# TEXT TO SPEECH SETUP
# ==========================================

engine = pyttsx3.init()

voices = engine.getProperty("voices")

engine.setProperty("voice", voices[VOICE_INDEX].id)

engine.setProperty("rate", SPEECH_RATE)


# ==========================================
# SPEAK FUNCTION
# ==========================================

def speak(text):

    print(f"{ASSISTANT_NAME}: {text}")

    engine.say(text)

    engine.runAndWait()


# ==========================================
# LISTEN FUNCTION
# ==========================================

def listen():

    recognizer = sr.Recognizer()

    recognizer.pause_threshold = 1.2
    recognizer.non_speaking_duration = 0.5
    recognizer.dynamic_energy_threshold = True

    try:

        with sr.Microphone() as source:

            print("\n🎤 Listening...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=10
            )

            print("Recognizing...")

            command = recognizer.recognize_google(audio)

            command = command.lower().strip()

            print(f"{USER_NAME}: {command}")

            return command

    except sr.WaitTimeoutError:

        print("No speech detected.")

        speak("I didn't hear anything.")

        return ""

    except sr.UnknownValueError:

        print("Speech not recognized.")

        speak("Sorry, I couldn't understand.")

        return ""

    except sr.RequestError as e:

        print(f"Speech Recognition Error: {e}")

        speak("Speech recognition service is unavailable.")

        return ""

    except Exception as e:

        print(f"Unexpected Error: {e}")

        return ""