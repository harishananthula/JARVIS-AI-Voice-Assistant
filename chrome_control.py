import webbrowser
import pyautogui
import time

from speech import speak


def search_google(query):
    speak(f"Searching Google for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")


def new_tab():
    pyautogui.hotkey("ctrl", "t")
    speak("Opened a new tab.")


def close_tab():
    pyautogui.hotkey("ctrl", "w")
    speak("Closed the current tab.")


def next_tab():
    pyautogui.hotkey("ctrl", "tab")
    speak("Switched to the next tab.")


def previous_tab():
    pyautogui.hotkey("ctrl", "shift", "tab")
    speak("Switched to the previous tab.")


def refresh():
    pyautogui.press("f5")
    speak("Refreshing the page.")


def go_back():
    pyautogui.hotkey("alt", "left")
    speak("Going back.")


def go_forward():
    pyautogui.hotkey("alt", "right")
    speak("Going forward.")


def downloads():
    pyautogui.hotkey("ctrl", "j")
    speak("Opening downloads.")