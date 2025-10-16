import requests
import os

bot_token = os.getenv('BOT_TOKEN')
if not bot_token:
    bot_token = input("Enter your bot token: ")

user_id = input("Enter user ID: ")
channels = -1002162858751
url = "https://py-today-member-checker.vercel.app/"

params = {
    'token': bot_token,
    'channel': channels,
    'userid': user_id
}

response = requests.get(url, params=params)

if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Error:", response.text)
