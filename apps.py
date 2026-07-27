import os
import subprocess
from pathlib import Path

# -----------------------------
# Windows Apps
# -----------------------------

def open_notepad():
    os.system("notepad")


def open_calculator():
    os.system("calc")


def open_paint():
    os.system("mspaint")


def open_cmd():
    os.system("start cmd")


def open_explorer():
    os.system("explorer")


def open_settings():
    os.system("start ms-settings:")


def open_camera():
    os.system("start microsoft.windows.camera:")


# -----------------------------
# VS Code
# -----------------------------

def open_vscode():
    os.system("code")


# -----------------------------
# Google Chrome
# -----------------------------

def open_chrome():

    chrome_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]

    for path in chrome_paths:
        if os.path.exists(path):
            subprocess.Popen(path)
            return

    print("Chrome not found.")


# -----------------------------
# User Folders
# -----------------------------

HOME = Path.home()


def open_downloads():
    os.startfile(HOME / "Downloads")


def open_documents():
    os.startfile(HOME / "Documents")


def open_pictures():
    os.startfile(HOME / "Pictures")


def open_videos():
    os.startfile(HOME / "Videos")


def open_music():
    os.startfile(HOME / "Music")


# -----------------------------
# Task Manager
# -----------------------------

def open_task_manager():
    os.system("taskmgr")


# -----------------------------
# Recycle Bin
# -----------------------------

def open_recycle_bin():
    os.system("start shell:RecycleBinFolder")


# -----------------------------
# CLOSE APPS
# -----------------------------

def close_chrome():
    os.system("taskkill /F /IM chrome.exe")


def close_notepad():
    os.system("taskkill /F /IM notepad.exe")


def close_calculator():
    os.system("taskkill /F /IM CalculatorApp.exe")
    os.system("taskkill /F /IM calculator.exe")


def close_paint():
    os.system("taskkill /F /IM mspaint.exe")


def close_cmd():
    os.system("taskkill /F /IM cmd.exe")