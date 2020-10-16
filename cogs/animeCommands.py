import json
import discord
from discord.ext import commands


class AnimeCommands(commands.Cog):
    def __int__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is now online")

    @commands.command(
        help="Displays N amount of recent anime from saved sites (data may be outdated)",
        brief="Displays old Anime data"
    )
    async def recentAnimeOld(self, ctx, arg=-1):
        try:
            arg = int(arg)

        catch()

        with open("config/recentAnimeQuery.JSON") as inputFile:
            data = json.load(inputFile)

        for website in data:

            numFields = entry = 0
            used_char_count = len(website)
            embedVar = discord.Embed(title=website, color=0x00ff00)

            for title in data[website]:
                content = f"[{title}]({data[website][title]})"
                entry += 1
                if len(content) + used_char_count > 6000 or numFields + 1 > 25:
                    await ctx.send(embed=embedVar)

                    numFields = 0
                    used_char_count = len(website)
                    del embedVar
                    embedVar = discord.Embed(title=website, color=0x00ff00)

                embedVar.add_field(name='\u200b', value=content, inline=False)
                numFields += 1
                used_char_count += len(content)

                if entry == arg:
                    break

            if numFields != 0:
                await ctx.send(embed=embedVar)


def setup(bot):
    bot.add_cog(AnimeCommands(bot))

#
# import os
# import json
# import discord
# from dotenv import load_dotenv
# from discord.ext import commands
# from helperFunctions import folderMaker, readListFromFile, saveListToFile
# from config.constants import *
# from AnimeHelper.webscrapeRecents import Weeb
#
# class AnimeCommands(commands.ext.Bot):
#     def __int__(self, bot):
#         self.bot = bot
#
#     # bot = commands.Bot(command_prefix=COMMAND_PREFIX)
#
#     # @bot.event
#     # async def on_ready():
#     #     print("logged in as ")
#
#     @self.bot.command(
#         help="Displays N amount of recent anime from saved sites (data may be outdated)",
#         brief="Displays old Anime data"
#     )
#     async def recentAnimeOld(ctx, arg: int):
#         with open("config/recentAnimeQuery.JSON") as inputFile:
#             data = json.load(inputFile)
#
#         for website in data:
#
#             numFields = entry = 0
#             used_char_count = len(website)
#             embedVar = discord.Embed(title=website, color=0x00ff00)
#
#             for title in data[website]:
#                 content = f"[{title}]({data[website][title]})"
#                 entry += 1
#                 if len(content) + used_char_count > 6000 or numFields + 1 > 25:
#                     await ctx.send(embed=embedVar)
#
#                     numFields = 0
#                     used_char_count = len(website)
#                     del embedVar
#                     embedVar = discord.Embed(title=website, color=0x00ff00)
#
#                 embedVar.add_field(name='\u200b', value=content, inline=False)
#                 numFields += 1
#                 used_char_count += len(content)
#
#                 if entry == arg:
#                     break
#
#             if numFields != 0:
#                 await ctx.send(embed=embedVar)
#
#
#     @bot.command(
#         help="Displays N amount of recent anime fresh saved sites",
#         brief="Displays new Anime data"
#     )
#     async def recentAnimeNew(ctx, arg: int):
#         t = Weeb()
#         parsed_websites = t.parseWebsites()
#         results = t.scrapeWebsites(parsed_websites)
#         t.updateJSON(results)
#
#         await ctx.invoke(bot.get_command('recentAnimeOld'), arg=arg)
#
#
#     @bot.command(
#         help="Adds an anime title into the watchlist. The watchlist being all the anime that we should be alerted to if "
#              "their uploaded to the watch websites",
#         brief="Adds an anime title to the watchlist"
#     )
#     async def AddToWatchList(ctx, *args):
#         title = ' '.join(args)
#
#         oldData = readListFromFile(WATCH_LIST_FILENAME)
#         oldData.append(title)
#
#         await ctx.send(
#             "Successfully added " + title if saveListToFile(oldData, WATCH_LIST_FILENAME) else "Failed to add " + title)
#
#
#     @bot.command(
#         help="Adds an anime title into the watchlist. The watchlist being all the anime that we should be alerted to if "
#              "their uploaded to the watch websites",
#         brief="Adds an anime title to the watchlist"
#     )
#     async def AddToWatchList(ctx, *args):
#         title = ' '.join(args)
#
#         oldData = readListFromFile(WATCH_LIST_FILENAME)
#         oldData.append(title)
#
#         await ctx.send(
#             "Successfully added " + title if saveListToFile(oldData, WATCH_LIST_FILENAME) else "Failed to add " + title)
#
#     # @bot.command(
#     #     help="Says hi back, no args = Bro, args = args",
#     #     brief="Says hi back"
#     # )
#     # async def hello(ctx, arg="Bro"):
#     #     embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
#     #     embedVar.add_field(name="Field1", value="hi", inline=False)
#     #     embedVar.add_field(name="Field2", value="hi2", inline=False)
#     #
#     #     await ctx.send(embed=embedVar)  # f"{arg} Hi, how are ya?"
#     #
#     #
#     # @bot.command()
#     # async def oga(ctx):
#     #     await ctx.send("oga wait'n be the problem!")
#     #
#
# bot.run(TOKEN)
#
# if __name__ == "__main__":
#     pass
