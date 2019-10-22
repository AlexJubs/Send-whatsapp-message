from twilio.rest import Client

account_sid = '***********'
auth_token = '**********'
client = Client(account_sid, auth_token)

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+14164276256'

message = 'Wagawn my g, its yaa boiiiii. I wrote this using a python script'

client.messages.create(body=message,
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)

print (message.sid)
