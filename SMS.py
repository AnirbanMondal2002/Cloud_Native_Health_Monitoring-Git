from twilio.rest import Client
import time

TWILIO_ACCOUNT_SID = "AC4ef52a29f2343ca61540605ef0262dc2"
TWILIO_AUTH_TOKEN = "95694c62bbafa8c858e07db9efbd5656"
TWILIO_PHONE_NUMBER = "+14173612839"
EMERGENCY_CONTACTS = ["+918391888767", "+916294455866"] 

def send_emergency_message(emergency_type="General Emergency", location="Unknown Location"):
    """
    Sends an emergency SMS to predefined contacts.
    Args:
        emergency_type (str): Type of emergency (e.g., "Medical Emergency").
        location (str): Location of the emergency.
    """
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message_body = (
        f"Emergency Alert!\n"
        f"Type: {emergency_type}\n"
        f"Location: {location}\n"
        f"Please respond immediately."
    )

    for contact in EMERGENCY_CONTACTS:
        try:
            message = client.messages.create(
                body=message_body,
                from_=TWILIO_PHONE_NUMBER,
                to=contact
            )
            print(f"Message sent to {contact}: SID {message.sid}")
        except Exception as e:
            print(f"Failed to send message to {contact}: {e}")


def monitor_emergency_triggers():
    print("Monitoring for emergencies...")
    time.sleep(5)  
    trigger_detected = True  

    if trigger_detected:
        print("Emergency detected!")
        send_emergency_message(
            emergency_type="Medical Emergency",
            location="SRM Institute of Science and Technology, Kattagulatur, Chennai"
        )


if __name__ == "__main__":
    monitor_emergency_triggers()