import smtplib
from email.message import EmailMessage

from config import EMAIL_ADDRESS, EMAIL_PASSWORD
from speech import speak


def send_email(receiver, subject, body):

    try:

        msg = EmailMessage()

        msg["From"] = EMAIL_ADDRESS
        msg["To"] = receiver
        msg["Subject"] = subject

        msg.set_content(body)

        with smtplib.SMTP("smtp.gmail.com", 587) as server:

            server.starttls()

            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            server.send_message(msg)

        speak("Email sent successfully.")

        print("✅ Email sent successfully.")

    except Exception as e:

        print(e)

        speak("Sorry. I couldn't send the email.")