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

@tasks.loop(days=1)
async def alarm_message():
    await client.wait_until_ready()
    channel = client.get_channel(channel_id)
    message = 'test'
    await channel.send(message)
    
    alarm_message.start()

@client.event
async def on_message(message):

	if time.hour == 12:
		if time.minute == 43: # The discord bot here comes and grabs the channel id and sends a random message of yours!
			await client.get_channel(channel_id).send(f"It is {time.hour}:{time.minute}!")
	while True:
		time = datetime.datetime.today()
	
	if message.author == client.user:
			return
	elif message.content.startswith('!schedule {time.hour}:{time.minute}'):
			await client.get_channel(channel_id).send(f"It is {time.hour}:{time.minute}!")
				
			client.run(TOKEN)