#this from ChatGPT

import discord
from note import TOKEN

# Create an instance of the bot client
client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user.name}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Ignore messages from the bot itself

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
client.run(TOKEN)