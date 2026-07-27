import screen_brightness_control as sbc
from ctypes import POINTER, cast

from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

from speech import speak


def get_volume():

    devices = AudioUtilities.GetSpeakers()

    interface = devices.Activate(
        IAudioEndpointVolume._iid_,
        CLSCTX_ALL,
        None
    )

    volume = cast(interface, POINTER(IAudioEndpointVolume))

    return volume


def volume_up():

    volume = get_volume()

    for _ in range(5):
        volume.VolumeStepUp(None)

    speak("Volume increased.")


def volume_down():

    volume = get_volume()

    for _ in range(5):
        volume.VolumeStepDown(None)

    speak("Volume decreased.")


def mute_volume():

    volume = get_volume()

    volume.SetMute(True, None)

    speak("Volume muted.")


def unmute_volume():

    volume = get_volume()

    volume.SetMute(False, None)

    speak("Volume unmuted.")


def max_volume():

    volume = get_volume()

    volume.SetMasterVolumeLevelScalar(1.0, None)

    speak("Volume set to maximum.")


# ==========================================
# BRIGHTNESS CONTROL
# ==========================================

def increase_brightness():

    try:

        current = sbc.get_brightness(display=0)[0]

        new = min(current + 10, 100)

        sbc.set_brightness(new)

        speak(f"Brightness increased to {new} percent.")

    except Exception as e:

        print(e)

        speak("Unable to increase brightness.")


def decrease_brightness():

    try:

        current = sbc.get_brightness(display=0)[0]

        new = max(current - 10, 0)

        sbc.set_brightness(new)

        speak(f"Brightness decreased to {new} percent.")

    except Exception as e:

        print(e)

        speak("Unable to decrease brightness.")


def set_brightness(value):

    try:

        value = max(0, min(100, int(value)))

        sbc.set_brightness(value)

        speak(f"Brightness set to {value} percent.")

    except Exception as e:

        print(e)

        speak("Unable to set brightness.")


def max_brightness():

    try:

        sbc.set_brightness(100)

        speak("Brightness set to maximum.")

    except Exception as e:

        print(e)

        speak("Unable to change brightness.")


def min_brightness():

    try:

        sbc.set_brightness(0)

        speak("Brightness set to minimum.")

    except Exception as e:

        print(e)

        speak("Unable to change brightness.")