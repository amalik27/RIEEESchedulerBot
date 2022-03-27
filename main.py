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
# from discord.ext import commands
# from discord.ext import tasks
# import asyncio
# import datetime
# import time
# import os

TOKEN = "OTU3Mzg5MDY3OTI0OTM0NjY2.Yj-EDQ.kV3VcBA66rQPKqQXNwjS-MCrFio" # discord bot token

client = discord.Client()

# channel_id = '957476426632798208' # set it to proper channel ID

@client.event
async def on_ready():
    print("{0.user}: Up and ready for action!".format.client)

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	elif message.content.startswith('!schedule'):
		await message.channel.send('You got it!')

client.run(TOKEN)