from twilio.rest import Client


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, message_body):
        account_sid = 'TWILLIO SID'
        auth_token = 'TWILLIO TOKEN'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
          from_='TWILLIO NUMBER',
          body=message_body,
          to='RECEIVER's NUMBER'
        )

        print(message.sid)
