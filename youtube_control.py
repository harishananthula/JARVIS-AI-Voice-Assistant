import pyautogui
import pygetwindow as gw
import time
from speech import speak


def activate_chrome():
    windows = gw.getWindowsWithTitle("Chrome")

    if windows:
        windows[0].activate()
        time.sleep(0.8)

def mute():
    activate_chrome()
    pyautogui.press("m")        


def next_video():
    activate_chrome()
    pyautogui.hotkey("shift", "n")


def previous_video():
    activate_chrome()
    pyautogui.hotkey("shift", "p")
    speak("Playing previous video.")




def fullscreen():
    activate_chrome()
    pyautogui.press("f")


def theater_mode():
    pyautogui.press("t")
    speak("Theater mode enabled.")


def increase_volume():
    pyautogui.press("up")
    speak("Volume increased.")


def decrease_volume():
    pyautogui.press("down")
    speak("Volume decreased.")


def forward():
    pyautogui.press("l")   # Skip ahead 10 seconds
    speak("Skipped forward.")


def backward():
    pyautogui.press("j")   # Go back 10 seconds
    speak("Skipped backward.")


def captions():
    pyautogui.press("c")
    speak("Captions toggled.")