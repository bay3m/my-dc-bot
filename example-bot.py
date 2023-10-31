
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

def run_bot():
    client.run('MTE2ODc2MTYwMzkxMTYwMjE5Ng.Gw7z2Q.UGRDbXMRgrX3wrC4iXYkHxKfgZ9R-hscUQNuXs')

if __name__ == "__main__":
    run_bot()