import discord
from secrets import TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('meme pls'):
        await message.channel.send('Hier sollte ein Meme stehen.')

client.run(TOKEN)
