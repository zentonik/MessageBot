import discord
import requests

DISCORD_TOKEN = 'TOKEN' # your bot token
CHANNEL_ID = 123 # your channel ID
WEBHOOK_URL = 'WEBHOOK_URL' # your webhook URL

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'logged in as {client.user}')

@client.event
async def on_message(message):
    if message.channel.id == CHANNEL_ID and not message.author.bot:
        avatar_url = message.author.avatar.url if message.author.avatar else None
        embed = {
            'username': 'Message Forwarder',
            'embeds': [
                {
                    'title': f"{message.author}:",
                    'description': message.content,
                    'color': 0x00ff00,
                    'thumbnail': {
                        'url': avatar_url
                    }
                }
            ]
        }
        response = requests.post(WEBHOOK_URL, json=embed)
        
        print(f"Webhook response status code: {response.status_code}")
        if response.status_code == 204:
            print(f"Message successfully sent to webhook.")
        else:
            print(f"Failed to forward message. Status code: {response.status_code}, Response text: {response.text}")

client.run(DISCORD_TOKEN)