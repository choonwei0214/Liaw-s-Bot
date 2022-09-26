import discord
import pandas as pd
from discord.ext import commands


db = pd.read_csv('db.csv')

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# @bot.event
# async def on_message(message):
# 	if message.content.lower() == "hello" or message.content.lower() == "hi":
# 		await message.channel.send(f"hey {message.author},{db}")

members_list = discord.Guild().members
@bot.event
async def on_message(message):
	if message.content.lower() == "hello" or message.content.lower() == "hi":
		await message.channel.send(f"hey {message.author},{members_list}")


bot.run("MTAyMzgzMDk1NzgxMzQxNTk4Nw.GrIYd6._Te5TGLFKXXfECO1sTce8kS85djLCW_tTBBB6E")