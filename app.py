# This is a script that allows us to receive and reply 
# to a message. This is a small web application using a framework
# called Flask, and this can accept incoming HTTP requests that are 
# triggered when your Twilio number receives SMS messages. 
# In addition to running this script, you also need to get a public URL
# using something like ngrok, and enter that URL in your Messaging
# Service Inbound Settings.

# Learn more: https://www.twilio.com/docs/sms/tutorials/how-to-receive-and-reply-python

from flask import Flask, request, session
from twilio.rest import Client

# Terrible texts inspired by a Justin Bieber song. I'm sorry.
LYRICS = [
    'say you love me',
    'as much as i love u',
    'woud you hurt me baby 😐',
    'could you DO that to me?!',
    'yeah??',
    'would u lie to me BABY'
]
PRANKED_MESSAGE = 'yoo you got pranked bro!!'

# Change these values to your own.
# DANGER! This is insecure. See http://twil.io/secure
ACCOUNT_SID = 'ACXXXXXXXXXXXXXXXXX' # You can find this on https://www.twilio.com/console'
AUTH_TOKEN = 'some_auth_token' # Also on https://www.twilio.com/console'
MESSAGING_SERVICE_SID = 'MGXXXXXXXXXXXXXXXXX' # You can find this on https://www.twilio.com/console/sms/services'

# This secret key is needed for conversation tracking using cookies.
# This helps us store which "stage" we're on, so we can know which 
# lyric to send. More info:
# https://www.twilio.com/docs/sms/tutorials/how-to-create-sms-conversations-python
SECRET_KEY = 'a_secret_key'
app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    # This gets the conversation-tracking counter,
    # increments it, then stores it in the session
    counter = session.get('counter', 0)
    counter += 1
    session['counter'] = counter

    # Determine what message to send using counter
    message_text = ''
    if counter <= len(LYRICS):
        message_text = LYRICS[counter - 1]
    else:
        message_text = PRANKED_MESSAGE

    # Send our response to the number that the message came from
    from_number = request.values.get('From')
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
            body=message_text,
            messaging_service_sid=MESSAGING_SERVICE_SID,
            to=from_number
        )
    print("Sent response:", message_text)
    return str(message)

if __name__ == "__main__":
    app.run(debug=True)