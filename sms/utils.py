import nexmo
from django.conf import settings
import re

def send_sms(to_number, message):
    # Initialize Nexmo client using API key and secret from Django settings
    client = nexmo.Client(key=settings.VONAGE_API_KEY, secret=settings.VONAGE_API_SECRET)
    
    # Send the SMS message
    response_data = client.send_message({
        "from": "Vonage APIs",  # Use your sender ID or a valid number
        "to": to_number,
        "text": message,
    })
    
    # Check if the SMS was sent successfully
    if response_data["messages"][0]["status"] == "0":
        return True, "Message sent successfully."
    else:
        return False, response_data["messages"][0]["error-text"]


def is_valid_phone_number(to_number):
    """
    Validates the phone number to ensure it's in the correct international format.
    E.g., +639123456789 (Philippines format)
    """
    pattern = r"^\+?[1-9]\d{1,14}$"  # Regex pattern for international numbers
    
    if re.match(pattern, to_number):
        return True
    else:
        return False