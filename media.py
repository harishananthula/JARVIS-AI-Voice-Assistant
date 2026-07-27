import pywhatkit
from speech import speak


# ==========================================
# Play Song
# ==========================================

def play_song(song):

    if not song:
        speak("Please tell me the song name.")
        return

    speak(f"Playing {song} on YouTube.")

    try:
        pywhatkit.playonyt(song)
    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry, I couldn't play the song.")


# ==========================================
# Google Search
# ==========================================

def google_search(query):

    if not query:
        speak("Please tell me what to search.")
        return

    speak(f"Searching Google for {query}.")

    try:
        pywhatkit.search(query)
    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry, I couldn't search Google.")


# ==========================================
# YouTube Search
# ==========================================

def youtube_search(video):

    if not video:
        speak("Please tell me what to search.")
        return

    speak(f"Searching YouTube for {video}.")

    try:
        pywhatkit.playonyt(video)
    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry, I couldn't search YouTube.")