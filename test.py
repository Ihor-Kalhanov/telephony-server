# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure

account_sid = "ACaf69dc760ec01ffc33cd035d75296050"
auth_token = "e5961e68a1c1f0ea7bac7467666fd9c1"
client = Client(account_sid, auth_token)

call = client.calls.create(
  url="http://demo.twilio.com/docs/voice.xml",
  to="+380993775027",
  from_="+18142059419"
)

print(call.sid)