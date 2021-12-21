import discord
import logging
from reddit import get_reddit_post
from secrets import TOKEN

logging.basicConfig(level=logging.INFO)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('meme pls'):
        url = get_reddit_post()
        await message.channel.send(url)

client.run(TOKEN)
