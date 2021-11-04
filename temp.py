# import os
# from twilio.rest import Client
#
#
# # Your Account Sid and Auth Token from twilio.com/console
# # and set the environment variables. See http://twil.io/secure
# account_sid = 'ACc8633dce6be4e952d94b4f72e60da0d9'
# auth_token = '7d3855421f32708dcdb85d0e1352be36'
# client = Client(account_sid, auth_token)
#
# message = client.messages \
#     .create(
#     body="Appointments for 18+ available!\nSikar Rajasthan",
#     from_='+13072033219',
#     to='+919096126744'
# )
#
# print(message.sid)

import datetime

min_age_limit = 45
poll_frequency = 5

baseURL = 'https://cdn-api.co-vin.in/api/v2'
endpoint = '/appointment/sessions/public/findByPin'

days = [(datetime.date.today() + datetime.timedelta(days=x)).strftime('%d-%m-%Y') for x in range(2)]

print(days)