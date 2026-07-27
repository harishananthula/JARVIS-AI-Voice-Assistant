import pyttsx3

print("Step 1")
print("Step 2")

try:
    engine = pyttsx3.init()
    print("Step 3")

    engine.say("Hello Harish")
    print("Step 4")

    engine.runAndWait()
    print("Step 5")

except Exception as e:
    print("Error:", e)