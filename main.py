import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def plan(ctx):
    await ctx.send('plan')

@bot.event
async def on_ready():
    guild_count = 0
    for guild in bot.guilds:
        print(
            f"{bot.user} is connected to the following guild:\n"
            f"{guild.name} (id: {guild.id})"
        )
        guild_count += 1

bot.run(TOKEN)