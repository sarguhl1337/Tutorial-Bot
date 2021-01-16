from datetime import datetime, timedelta
from platform import python_version
from time import time

import discord
from discord import __version__ as discord_version
from discord.ext import commands


class Manage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="stats")
    async def stats_command(self, ctx):
        embed = discord.Embed(
            title="Stats Command",
            colour=ctx.author.colour,
            timestamp=ctx.message.created_at
        )
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.add_field(name="Guilds", value=str(len(self.bot.guilds)), inline=True)
        embed.add_field(name="All Users", value=str(len(self.bot.users)), inline=True)
        embed.add_field(name="Bot Version", value=self.bot.VERSION, inline=True)
        embed.add_field(name="Discord.Py Version", value=discord_version, inline=True)
        
        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Manage(bot))
