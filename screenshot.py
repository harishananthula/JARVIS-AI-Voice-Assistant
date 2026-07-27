"""
=========================================
SCREENSHOT MODULE
Developer : Harish
=========================================
"""

import os
import pyautogui

from datetime import datetime

from speech import speak


# ==========================================
# SCREENSHOT DIRECTORY
# ==========================================

SCREENSHOT_FOLDER = "screenshots"

os.makedirs(SCREENSHOT_FOLDER, exist_ok=True)


# ==========================================
# TAKE SCREENSHOT
# ==========================================

def take_screenshot():

    try:

        filename = datetime.now().strftime(
            "Screenshot_%Y%m%d_%H%M%S.png"
        )

        filepath = os.path.join(
            SCREENSHOT_FOLDER,
            filename
        )

        screenshot = pyautogui.screenshot()

        screenshot.save(filepath)

        speak("Screenshot taken successfully.")

        print(f"\nSaved : {filepath}")

    except Exception as e:

        print(e)

        speak("Unable to take screenshot.")