"""
=========================================
JARVIS AI VOICE ASSISTANT
Developer : Harish
Version   : 4.0
=========================================
"""

# ==========================================
# IMPORT MODULES
# ==========================================

from speech import speak, listen

import chrome_control
import browser
import youtube_control
import utils
import media
import wiki
import apps
import ai
import screenshot
import system_control
import weather
import email_sender
import whatsapp
from contacts import CONTACTS
import re
from config import USER_NAME, ASSISTANT_NAME




def extract_whatsapp_details(command):

    patterns = [

        r"send whatsapp to (.+?) saying (.+)",

        r"send whatsapp to (.+?) (.+)",

        r"send message to (.+?) saying (.+)",

        r"send message to (.+?) (.+)",

        r"message (.+?) saying (.+)",

        r"message (.+?) (.+)",

    ]

    for pattern in patterns:

        match = re.search(pattern, command)

        if match:

            return (
                match.group(1).strip().lower(),
                match.group(2).strip()
            )

    return None, None




# ==========================================
# MAIN FUNCTION
# ==========================================

def main():

    print("=" * 50)
    print("        JARVIS AI ASSISTANT")
    print("=" * 50)

    speak("Jarvis is now running.")

    while True:

        command = listen()

        if not command:
            continue

        command = command.lower()

        print(f"\nCommand : {command}")

        # ==========================================
        # GREETINGS
        # ==========================================

        if "hello" in command or "hi" in command:

            speak(f"Hello {USER_NAME}. Nice to see you.")

        elif "how are you" in command:

            speak("I am doing great. Thank you for asking.")

        elif "your name" in command:

            speak(f"My name is {ASSISTANT_NAME}.")

        elif "who created you" in command:

            speak(f"I was created by {USER_NAME} using Python.")

        elif "thank you" in command:

            speak("You're welcome.")

        elif "good morning" in command:

            speak(f"Good Morning {USER_NAME}.")

        elif "good afternoon" in command:

            speak(f"Good Afternoon {USER_NAME}.")

        elif "good evening" in command:

            speak(f"Good Evening {USER_NAME}.")

        elif "good night" in command:

            speak(f"Good Night {USER_NAME}.")

        # ==========================================
        # TIME & DATE
        # ==========================================

        elif "time" in command:

            utils.tell_time()

        elif "date" in command:

            utils.tell_date()

        elif "day" in command:

            utils.tell_day()

        # ==========================================
        # WHATSAPP
        # ==========================================

        elif (
            "send whatsapp" in command
            or "send message" in command
            or "message" in command
        ):

            name, message = extract_whatsapp_details(command)

            # Ask for name only if it wasn't spoken
            while not name:

                speak("Whom should I send the message to?")

                name = listen()

                if not name:
                    continue

                name = name.strip().lower()

            if name not in CONTACTS:

                speak(f"{name} is not in your contacts.")
                continue

            # Ask for message only if it wasn't spoken
            while not message:

                speak("What is the message?")

                message = listen()

                if not message:
                    continue

            number = CONTACTS[name]["phone"]

            whatsapp.send_whatsapp(number, message)
        elif "open visual studio code" in command or "open vs code" in command:

            speak("Opening Visual Studio Code.")
            apps.open_vscode()

        elif "open notepad" in command:

            speak("Opening Notepad.")
            apps.open_notepad()

        elif "open calculator" in command:

            speak("Opening Calculator.")
            apps.open_calculator()

        elif "open paint" in command:

            speak("Opening Paint.")
            apps.open_paint()

        elif "open command prompt" in command or "open cmd" in command:

            speak("Opening Command Prompt.")
            apps.open_cmd()

        elif "open file explorer" in command:

            speak("Opening File Explorer.")
            apps.open_explorer()

        elif "open settings" in command:

            speak("Opening Settings.")
            apps.open_settings()

        elif "open camera" in command:

            speak("Opening Camera.")
            apps.open_camera()

        elif "open task manager" in command:

            speak("Opening Task Manager.")
            apps.open_task_manager()

        elif "open recycle bin" in command:

            speak("Opening Recycle Bin.")
            apps.open_recycle_bin()

        # ==========================================
        # FOLDERS
        # ==========================================

        elif "open downloads" in command:

            speak("Opening Downloads.")
            apps.open_downloads()

        elif "open documents" in command:

            speak("Opening Documents.")
            apps.open_documents()

        elif "open pictures" in command:

            speak("Opening Pictures.")
            apps.open_pictures()

        elif "open videos" in command:

            speak("Opening Videos.")
            apps.open_videos()

        elif "open music" in command:

            speak("Opening Music folder.")
            apps.open_music()
        # ==========================================
        # SCREENSHOT
        # ==========================================

        elif (
            "take screenshot" in command
            or "capture screen" in command
            or "save screenshot" in command
        ):

            screenshot.take_screenshot()
        # ==========================================
        # CLOSE APPLICATIONS
        # ==========================================

        elif "close chrome" in command:

            apps.close_chrome()

        elif "close notepad" in command:

            apps.close_notepad()

        elif "close calculator" in command:

            apps.close_calculator()

        elif "close paint" in command:

            apps.close_paint()

        elif "close command prompt" in command or "close cmd" in command:

            apps.close_cmd()
        
        # ==========================================
        # VOLUME CONTROL
        # ==========================================

        elif "increase volume" in command:

            system_control.volume_up()

        elif "decrease volume" in command:

            system_control.volume_down()

        elif "mute volume" in command:

            system_control.mute_volume()

        elif "unmute volume" in command:

            system_control.unmute_volume()

        elif "max volume" in command or "maximum volume" in command:

            system_control.max_volume()
        # ==========================================
        # BRIGHTNESS CONTROL
        # ==========================================

        elif "increase brightness" in command:

            system_control.increase_brightness()

        elif "decrease brightness" in command:

            system_control.decrease_brightness()

        elif "maximum brightness" in command:

            system_control.max_brightness()

        elif "minimum brightness" in command:

            system_control.min_brightness()

        elif "set brightness to" in command:

            try:

                value = ''.join(filter(str.isdigit, command))

                system_control.set_brightness(int(value))

            except Exception:

                speak("Please tell a valid brightness value.")        
        # ==========================================
        # WEATHER
        # ==========================================

        elif command.startswith("weather in"):

            city = command.replace("weather in", "").strip()

            weather.get_weather(city)

        elif command.startswith("temperature in"):

            city = command.replace("temperature in", "").strip()

            weather.get_weather(city)

        elif command.startswith("what is the weather in"):

            city = command.replace("what is the weather in", "").strip()

            weather.get_weather(city)

        # ==========================================
        # MEDIA & SEARCH
        # ==========================================

        elif command.startswith("play"):

            song = command.replace("play", "").strip()

            if song:
                speak(f"Playing {song}.")
                media.play_song(song)
            else:
                speak("Please tell me the song name.")

        # ==========================================
        # GOOGLE SEARCH
        # ==========================================

        elif command.startswith("search google for"):

            query = command.replace(
                "search google for",
                ""
            ).strip()

            if query:
                speak(f"Searching Google for {query}.")
                media.google_search(query)
            else:
                speak("Please tell me what to search.")

        # ==========================================
        # YOUTUBE SEARCH
        # ==========================================

        elif command.startswith("search youtube for"):

            query = command.replace(
                "search youtube for",
                ""
            ).strip()

            if query:
                speak(f"Searching YouTube for {query}.")
                media.youtube_search(query)
            else:
                speak("Please tell me what to search.")

        # ==========================================
        # WIKIPEDIA
        # ==========================================

        elif command.startswith("who is"):

            person = command.replace("who is", "").strip()

            if person:
                wiki.search_person(person)

        elif command.startswith("what is"):

            topic = command.replace("what is", "").strip()

            if topic:
                wiki.search_person(topic)

        # ==========================================
        # EXIT
        # ==========================================

        elif (
            "bye" in command
            or "exit" in command
            or "quit" in command
            or "stop jarvis" in command
        ):

            speak(f"Goodbye {USER_NAME}.")
            speak("Have a wonderful day.")
            break
         # ==========================================
        
        # ==========================================
        # EMAIL
        # ==========================================

        elif (
            "send email" in command
            or "send mail" in command
            or "email" in command
        ):

            speak("Whom should I send the email to?")

            name = listen().lower()

            if not name:
                speak("I didn't get the contact name.")
                continue

            if name not in CONTACTS:
                speak("Contact not found.")
                continue

            receiver = CONTACTS[name]

            speak("What is the subject?")

            subject = listen()

            if not subject:
                speak("Subject not received.")
                continue

            speak("What is the message?")

            body = listen()

            if not body:
                speak("Message not received.")
                continue

            email_sender.send_email(receiver, subject, body)

        # ==========================================
        # WHATSAPP
        # ==========================================

        elif (
            "send whatsapp" in command
            or "send message" in command
            or "message" in command
        ):

            name, message = extract_whatsapp_details(command)

            # Ask for name only if it wasn't spoken
            while not name:

                speak("Whom should I send the message to?")

                name = listen()

                if not name:
                    continue

                name = name.strip().lower()

            if name not in CONTACTS:

                speak(f"{name} is not in your contacts.")
                continue

            # Ask for message only if it wasn't spoken
            while not message:

                speak("What is the message?")

                message = listen()

                if not message:
                    continue

            number = CONTACTS[name]["phone"]

            whatsapp.send_whatsapp(number, message)
            
        
       # ==========================================
        # CHROME AUTOMATION
        # ==========================================

        # ==========================================
        # CHROME AUTOMATION
        # ==========================================

        elif "search" in command:

            query = command.replace("search", "").strip()

            chrome_control.search_google(query)


        elif (
            "close tab" in command
            or "close current tab" in command
            or "close this tab" in command
        ):

            chrome_control.close_tab()


        elif (
            "new tab" in command
            or "open new tab" in command
        ):

            chrome_control.new_tab()


        elif (
            "next tab" in command
            or "switch tab" in command
        ):

            chrome_control.next_tab()


        elif (
            "previous tab" in command
            or "last tab" in command
            or "back tab" in command
        ):

            chrome_control.previous_tab()


        elif "refresh" in command:

            chrome_control.refresh()


        elif "go back" in command:

            chrome_control.go_back()


        elif "go forward" in command:

            chrome_control.go_forward()


        elif (
            "downloads" in command
            or "download history" in command
        ):

            chrome_control.downloads()
        ## ==========================================
        # YOUTUBE AUTOMATION
        # ==========================================

        elif "pause video" in command or "pause youtube" in command:
            youtube_control.play_pause()

        elif (
            "play video" in command
            or "resume video" in command
            or "resume youtube" in command
        ):
            youtube_control.play_pause()

        elif "next video" in command:
            youtube_control.next_video()

        elif "previous video" in command:
            youtube_control.previous_video()

        elif (
            "mute video" in command
            or "mute youtube" in command
        ):
            youtube_control.mute()

        elif (
            "fullscreen" in command
            or "full screen" in command
        ):
            youtube_control.fullscreen()

        elif "theater mode" in command:
            youtube_control.theater_mode()

        elif (
            "increase youtube volume" in command
            or "youtube volume up" in command
        ):
            youtube_control.increase_volume()

        elif (
            "decrease youtube volume" in command
            or "youtube volume down" in command
        ):
            youtube_control.decrease_volume()

        elif (
            "forward video" in command
            or "skip forward" in command
        ):
            youtube_control.forward()

        elif (
            "back video" in command
            or "rewind video" in command
        ):
            youtube_control.backward()

        elif (
            "captions" in command
            or "subtitles" in command
        ):
            youtube_control.captions()
        # ==========================================
        # AI ASSISTANT
        # =========================================

        else:

            speak("Let me think.")

            try:

                answer = ai.ask_ai(command)

                print("\n===================================")
                print("AI RESPONSE")
                print("===================================\n")

                print(answer)

                speak(answer)

            except Exception as e:

                print(e)
                speak("Sorry. AI is not available right now.")


# ==========================================
# START PROGRAM
# ==========================================

if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        print("\nJarvis stopped by user.")

    except Exception as e:

        print(f"\nUnexpected Error: {e}")