# Imports
import os

from docs import black_jack
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='$$')
postPrefix = '$$'



@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.command(help='- Lets you play blackjack')
async def BlackJack(ctx):
    await black_jack(ctx, client)


@client.command()
async def Slots():
    pass

"""
# Only implement if using client.event()
def check_for_post_prefix(ctx):
    msg = ctx.message.content
    if msg[len(msg)-2:len(msg)-1] == postPrefix:
        return True
    return False
"""



client.run(TOKEN)
