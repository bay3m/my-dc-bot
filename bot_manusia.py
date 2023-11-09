#dikasih embed

import discord
from discord.ext import commands
from note import TOKEN_2

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def test(ctx, arg):
    await ctx.send(embed=discord.Embed(
        title="Hello",
        description=arg,
        color=0xff0ff
    ))
    
@bot.event
async def on_ready():
    print(f'{bot.user} is ready')

if __name__ == '__main__':
    bot.run(TOKEN_2)