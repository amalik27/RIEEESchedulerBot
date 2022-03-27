# import discord
# token = "OTU3Mzg5MDY3OTI0OTM0NjY2.Yj-EDQ.kV3VcBA66rQPKqQXNwjS-MCrFio"

# client = discord.Client()
# @client.event
# async def on_ready():
# 	print("{0.user} is online!".format.client)
# @client.event
# async def on_message(message):
# 	if message.author == client.user:
# 		return
# 	elif message.content.startswith('!setMessage'):
# 		await message.channel.send('I am alive!')
# client.run(token)

import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio
import datetime
import time

TOKEN = 'OTU3MzUyNDQzNjYwODgyMDIw.Yj9h8Q.detpUGrH4oU0Gcp28ycS3mVQ4gQ' # discord bot token

client = commands.Bot(command_prefix = '.')

channel_id = '957476426632798208' # set it to proper channel ID

@client.event
async def on_ready():
    print('Scheduler Bot: Up and ready for action!')

# @tasks.loop(days=1)
async def alarm_message():
    await client.wait_until_ready()
    while not client.is_closed:
        channel = client.get_channel(channel_id)
        messages = ('test')
        await client.send_message(channel, messages)
        await asyncio.sleep(5) #runs every 5 seconds

client.loop.create_task(alarm_message())

client.run(TOKEN)

# @client.event
# async def on_message(message):

# 	if message.author == client.user:
# 		return
# 		elif message.content.startswith('!setMessage'):
# 			await message.channel.send('I am alive!')
	
# 		client.run(TOKEN)