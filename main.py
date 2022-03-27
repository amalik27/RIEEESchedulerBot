
import discord
import os
token = 'OTU3Mzg5MDY3OTI0OTM0NjY2.Yj-EDQ.kV3VcBA66rQPKqQXNwjS-MCrFio'
client = discord.Client()
@client.event
async def on_ready():
	print("{0.user} is online!".format.client)
@client.event
async def on_message(message):
	if message.author == client.user:
		return
	elif message.content.startswith('!setMessage'):
		await message.channel.send('Im alive!')
client.run(token)