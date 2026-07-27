import webbrowser

from speech import speak


def open_google():
    speak("Opening Google")
    webbrowser.open("https://www.google.com")


def open_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")


def open_chatgpt():
    speak("Opening Chat GPT")
    webbrowser.open("https://chat.openai.com")


def open_github():
    speak("Opening GitHub")
    webbrowser.open("https://github.com")


def open_linkedin():
    speak("Opening LinkedIn")
    webbrowser.open("https://www.linkedin.com")


def open_instagram():
    speak("Opening Instagram")
    webbrowser.open("https://www.instagram.com")

