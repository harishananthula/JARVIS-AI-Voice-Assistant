import wikipedia

from speech import speak


# ==========================================
# Wikipedia Search
# ==========================================

def search_person(person):

    if not person:
        speak("Please tell me whom to search.")
        return

    try:

        speak(f"Searching Wikipedia for {person}.")

        result = wikipedia.summary(
            person,
            sentences=2,
            auto_suggest=False
        )

        print("\nWikipedia:\n")
        print(result)

        speak(result)

    except wikipedia.DisambiguationError as e:

        speak(
            f"There are multiple results for {person}. Please be more specific."
        )

        print("Suggestions:", e.options[:5])

    except wikipedia.PageError:

        speak("Sorry, I couldn't find that person or topic.")

    except Exception as e:

        print(e)

        speak("Something went wrong while searching Wikipedia.")