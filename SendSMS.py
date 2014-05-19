from twilio import rest
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC94aeb0952c226fbf03399bd6da5270be"
auth_token = "ce446ff813981e284050703c5e7fe917"
client = rest.TwilioRestClient(account_sid, auth_token)
message = client.messages.create(body="Test Mesage from Python",
to="+16305064340", # Replace with your phone number
from_="+17088132181") # Replace with your Twilio number
print message.sid

