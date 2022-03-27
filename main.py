import discord
import asyncio
from discord.ext import commands
from discord.ext import tasks
import time
# import os
# import datetime

TOKEN = 'OTU3Mzg5MDY3OTI0OTM0NjY2.Yj-EDQ.3Ld43lvx2v3qk1DVYSxrDyHwTks'  # discord bot token

client = discord.Client()

channel_id = '957476426632798208'  # set it to proper channel ID


@client.event
async def on_ready():
    print('Up and ready for action!')


@tasks.loop(seconds=5)
async def alarm_message():

    await client.wait_until_ready()
    channel = client.get_channel(channel_id)

    await channel.send('I am going to send a message every 5 seconds!')


@client.event
async def on_message(message):

	if message.author == client.user:
		return
	if message.content.startswith('!schedule'):
		alarm_message.start()

client.run(TOKEN)

# @client.event
# async def on_message(message):

# 	if message.author == client.user:
# 		return
# 	if message.content.startswith('!schedule'):
# 		await message.channel.send('You got it!')

# while True:
# 	time = datetime.datetime.today()

# 	if message.content.startswith('!schedule {time.hour}:{time.minute}'):
# 		await client.get_channel(channel_id).send(f"It is {time.hour}:{time.minute}!")
