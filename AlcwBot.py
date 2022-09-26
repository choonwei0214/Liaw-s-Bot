import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_message(message):
	if message.content.lower() == "hello":
		await message.channel.send(f"hey {message.author}")



bot.run("MTAyMzgzMDk1NzgxMzQxNTk4Nw.GrIYd6._Te5TGLFKXXfECO1sTce8kS85djLCW_tTBBB6E")