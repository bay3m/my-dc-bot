#FROM YT
#source: https://youtu.be/hoDLj0IzZMU?si=4UjRroo1BuNaQ7GX
#
#problem: recieve message in DM but not in server
from note import TOKEN
import discord

intents = discord.Intents.all()

def handelResponse(message):
    p_message = message.lower()

    if p_message == 'hello':
        return 'hey there'
    
    if p_message == '!help':
        return 'This is a help message'

async def send_message(message, user_message, is_private):
    try:
        response = handelResponse(user_message)
        if response:
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    token = TOKEN
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is ready')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
     
        username     = message.author
        channel      = message.channel
        is_private   = isinstance(message.channel, discord.DMChannel)
        user_message = message.content.lower()

        if user_message.startswith('?'):
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)

        else:
            response = handelResponse(user_message)
            if response:
                await send_message(message, user_message, is_private)

        print(f'{username} -- {user_message} -- {channel}')

    client.run(token)

if __name__ == '__main__':
    run_discord_bot()
