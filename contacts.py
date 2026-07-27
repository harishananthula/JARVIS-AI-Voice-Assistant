"""
=========================================
CONTACTS MODULE
Automatically loads contacts from contacts.csv
=========================================
"""

import csv
import re

CONTACTS = {}


def clean_phone(phone):
    """Convert phone number to international format."""

    if not phone:
        return None

    digits = re.sub(r"\D", "", phone)

    if len(digits) < 10:
        return None

    # Indian 10-digit number
    if len(digits) == 10:
        return "+91" + digits

    # Indian number with country code
    if len(digits) == 12 and digits.startswith("91"):
        return "+" + digits

    # Any other international number
    return "+" + digits


def clean_name(name):
    """Normalize contact name."""

    if not name:
        return None

    name = name.strip().lower()

    if len(name) < 2:
        return None

    invalid = {
        "🙂",
        "😊",
        "😂",
        "😍",
        "5",
        "2024",
        "test",
        "unknown",
    }

    if name in invalid:
        return None

    return name


def load_contacts():

    try:

        with open("contacts.csv", newline="", encoding="utf-8-sig") as file:

            reader = csv.DictReader(file)

            for row in reader:

                name = clean_name(row.get("First Name", ""))

                if not name:
                    continue

                phone = clean_phone(row.get("Phone 1 - Value", ""))

                if not phone:
                    continue

                email = ""

                # Automatically detect an email column if present
                for key, value in row.items():
                    if "email" in key.lower() and value.strip():
                        email = value.strip()
                        break

                # Ignore duplicate names
                if name not in CONTACTS:

                    CONTACTS[name] = {
                        "phone": phone,
                        "email": email,
                    }

    except FileNotFoundError:

        print("contacts.csv not found.")


load_contacts()