from twilio.rest import Client


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, message_body):
        account_sid = 'AC1498b39891ab497125a713db481d9e72'
        auth_token = '61592578095c2a266e5873de4608a1eb'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
          from_='+12513354300',
          body=message_body,
          to='+2349055789508'
        )

        print(message.sid)