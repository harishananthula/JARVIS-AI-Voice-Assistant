from ollama import chat

# ==========================================
# AI Chat Function
# ==========================================

MODEL_NAME = "llama3.2:3b"


def ask_ai(prompt):

    if not prompt:
        return "Please ask me something."

    try:

        response = chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:

        print(f"AI Error: {e}")

        return (
            "Sorry Harish, I couldn't connect to the AI model. "
            "Please make sure Ollama is running."
        )