# twilitroll
Send funny texts to your friends.

## How to start:
1. Clone this project with `git clone https://github.com/kelseymakesthings/twilitroll.git`
2. `cd twilitroll`

## To send a single message:
(Full instructions including installations [here](https://www.twilio.com/docs/sms/quickstart/python)):
1. Fill in placeholder values on `send_single_message.py`
2. `python send_single_message.py`

## To receive and reply to messages:
(Full instructions [here](https://www.twilio.com/docs/sms/tutorials/how-to-receive-and-reply-python))
1. Fill in placeholder values on `app.py`
2. `python app.py`
3. In another tab, [install ngrok](https://ngrok.com/download) and `ngrok http 8000`
4. Click on your Messaging Service (find it [here](https://www.twilio.com/console/sms/services)), and under Settings/Inbound Settings click "Send an incoming_message webhook"
5. For the request url, type in the ngrok forwarding url, plus `/sms` at the end. Something like: `https://abcde12345.ngrok.io/sms`
6. Save settings, then send a message to your Twilio number to see the response!
