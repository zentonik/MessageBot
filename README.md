# MessageBot

MessageBot is a Discord bot designed to forward messages from a specific channel to a designated webhook. It captures user avatars and message content and sends this information to the webhook.

## Features

- Forwards messages from a specified Discord channel to a webhook.
- Displays user avatars and message content in the forwarded messages.
- Logs the status of the webhook request.

## Prerequisites

- Python 3.7 or higher
- `discord.py` library
- `requests` library
## Configuration

DISCORD_TOKEN = 'your_discord_token'  # Your Discord bot token
CHANNEL_ID = 123  # Your channel ID
WEBHOOK_URL = 'your_webhook_url'  # Your webhook URL

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/zentonik/MessageBot.git
   cd MessageBot

