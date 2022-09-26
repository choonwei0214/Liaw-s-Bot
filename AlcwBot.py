import discord
import pandas as pd
import random
from discord.ext import commands


db = pd.read_csv('db.csv')

intents=discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_message(message):
	if message.content.lower() == "hello" or message.content.lower() == "hi":
		await message.channel.send(f"hey {message.author},{db}")
	await bot.process_commands(message)

@bot.command()
async def info(ctx):
	embed=discord.Embed(title="Ah Liaw's Bot", description="Here are the commands that you can use:", color=0xffffff)
	embed.add_field(name="$stats", value="To view your statistics", inline=False)
	embed.add_field(name="$steal", value="To steal gold from someone else (1 hour cooldown)", inline=False)
	embed.add_field(name="$work", value="To earn gold (3 hours cooldown)", inline=False)
	embed.add_field(name="$upgrade", value="To upgrade your ability to steal", inline=True)
	embed.add_field(name="$leaderboard", value="To view the latest leaderboard", inline=False)
	await ctx.channel.send(embed=embed)

@bot.command()
async def stats(ctx):
	current_player = ctx.message.author.id
	db_stats = db.loc[db['ID'] == current_player]
	db_sorted = db.sort_values(by="gold", ascending=False, ignore_index=True)
	embed3=discord.Embed(title="Statistics", description="Your current status")
	embed3.add_field(name="Name", value=db_stats['name'].values[0], inline=False)
	embed3.add_field(name="Gold", value=db_stats['gold'].values[0], inline=False)
	embed3.add_field(name="Stealing power", value=db_stats['stealing_power'].values[0], inline=False)
	embed3.add_field(name="Current ranking", value=db_sorted.index[db_sorted['ID'] == current_player].tolist()[0]+1, inline=False)
	await ctx.channel.send(embed=embed3)

@bot.command()
@commands.cooldown(1, 3600, commands.BucketType.user)
async def steal(ctx):
	current_player = ctx.message.author.id
	db_steal = db.loc[db['ID'] != current_player]
	
	# The player that kena steal
	player_to_steal = db_steal.loc[random.randint(0, len(db_steal))]
	# Amount to steal from the player
	amt_to_steal = round(random.uniform(0.03, 0.05) * player_to_steal['gold'],2)
	
	# Original amount from the player
	ori_amt = db.loc[db['ID'] == player_to_steal['ID']]['gold']
	# Deduct from the player
	final_amt = ori_amt - amt_to_steal
	db.loc[db['ID'] == player_to_steal['ID'], 'gold'] = final_amt

	# Add to the player who steals
	curr_amt = db.loc[db['ID'] == current_player, 'gold']
	db.loc[db['ID'] == current_player, 'gold'] = curr_amt + amt_to_steal
	await ctx.channel.send(f"You stole {amt_to_steal} golds from {player_to_steal['name']}!")

@bot.command()
async def leaderboard(ctx):
	db_sorted = db.sort_values(by="gold", ascending=False, ignore_index=True)
	embed2=discord.Embed(title="Leaderboard", description="Top 5 players with the most golds")
	for i in range(5):
		embed2.add_field(name=f"Top {i+1}: {db_sorted.loc[i,'name']}", value=db_sorted.loc[i,'gold'], inline=False)
	await ctx.channel.send(embed=embed2)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.channel.send(f'This command is on cooldown, you can use it in {round(error.retry_after, 2)}s')

bot.run("MTAyMzgzMDk1NzgxMzQxNTk4Nw.GrIYd6._Te5TGLFKXXfECO1sTce8kS85djLCW_tTBBB6E")