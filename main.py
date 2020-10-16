import os
import json
import discord
from dotenv import load_dotenv
from discord.ext import commands
from helperFunctions import folderMaker, readListFromFile, saveListToFile
from config.constants import *
from AnimeHelper.webscrapeRecents import Weeb

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
folderMaker("config")

bot = commands.Bot(command_prefix=COMMAND_PREFIX)


@bot.command()
async def load(ctx, extensions):
    bot.load_extension(f"cogs.{extensions}")


@bot.command()
async def unload(ctx, extensions):
    bot.unload_extension(f"cogs.{extensions}")


for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)

if __name__ == "__main__":
    pass
