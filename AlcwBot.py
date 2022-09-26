import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_message(message):
	if message.content == "hello":
		await message.channel.send(f"hey {message.author}")



bot.run(DISCORD_TOKEN)