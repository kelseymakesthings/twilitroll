# This is a script to send one message to your target using a 
# Messaging Service. This script cannot receive messages.

# Learn more: https://www.twilio.com/docs/sms/quickstart/python

from twilio.rest import Client

MESSAGE_TEXT = 'hey baby i got a new phone 😙'

# Change these values to your own.
# DANGER! This is insecure. See http://twil.io/secure
ACCOUNT_SID = 'ACXXXXXXXXXXXXXXXXX' # You can find this on https://www.twilio.com/console'
AUTH_TOKEN = 'some_auth_token' # Also on https://www.twilio.com/console'
MESSAGING_SERVICE_SID = 'MGXXXXXXXXXXXXXXXXX' # You can find this on https://www.twilio.com/console/sms/services'
TO_NUMBER = '+14151234567' # The number to send the message to

client = Client(ACCOUNT_SID, AUTH_TOKEN)
message = client.messages \
    .create(
        body=MESSAGE_TEXT,
        messaging_service_sid=MESSAGING_SERVICE_SID,
        to=TO_NUMBER
    )
print("Sent message:", MESSAGE_TEXT)
