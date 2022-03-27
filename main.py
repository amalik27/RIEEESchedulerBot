import discord
import asyncio
from discord.ext import commands
from discord.ext import tasks
import time
from apscheduler.schedulers.blocking import BlockingScheduler
# import os
# import datetime

TOKEN = 'OTU3Mzg5MDY3OTI0OTM0NjY2.Yj-EDQ.oIe39LR-SVXOrEqeA2SaiNw9vr I'  # discord bot token

client = discord.Client()

channel_id = 957476426632798211  # set it to proper channel ID


@client.event
async def on_ready():
    print('Up and ready for action!')


@tasks.loop(seconds=5)
async def alarm_message():

    await client.wait_until_ready()
    channel = client.get_channel(channel_id)
    # await client.send_message(discord.Object(channel_id), 'I am going to send a message every 5 seconds!')
    await channel.send('I am going to send a message every 5 seconds!')


@client.event
async def on_message(message):
	
	if message.author == client.user:
		return
	if message.content.startswith('!timer'):
		alarm_message.start()
		await message.channel.send('I will start sending a message every 5 seconds!')
	if message.content.startswith('!stop'):
		alarm_message.stop()
		await message.channel.send('man fuck abdul!')

@client.event
async def job_function():
    print("First Event")

sched = BlockingScheduler()

# Schedules job_function to be run on the third Friday
# of June, July, August, November and December at 00:00, 01:00, 02:00 and 03:00
sched.add_job(job_function, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')

sched.start()

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
