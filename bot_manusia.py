#jalan sih tapi gabisa respon apa apa

import discord
from discord.ext import commands
from note import TOKEN_2

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


def run_bot():
    client = discord.Client(intents=intents)
    token = TOKEN_2

    @bot.command()
    async def test(ctx, arg):
        await ctx.send(arg)
        
    @client.event
    async def on_ready():
        print(f'{client.user} is ready')

    client.run(token)

if __name__ == '__main__':
    run_bot()