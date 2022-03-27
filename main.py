import discord
# from discord.ext import commands
from discord.ext import tasks
import asyncio
import datetime
import time
# import os

TOKEN = 'OTU3Mzg5MDY3OTI0OTM0NjY2.Yj-EDQ.goc40Ay9l-LhzgOzfTDxQ5pOSg8'  # discord bot token

client = discord.Client()

channel_id = '957476426632798208'  # set it to proper channel ID

@client.event
async def on_ready():
    print('{0.user}: Up and ready for action!'.format(client))

@tasks.loop(days=1)
async def alarm_message(message):
	await client.wait_until_ready()
	channel = client.get_channel(channel_id)
	
	if alarm_message.author == client.user:
			return
	if alarm_message.content.startswith('!schedule'):
			await alarm_message.channel.send('You got it!')
    # message = 'test'
    # await channel.send(message)
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