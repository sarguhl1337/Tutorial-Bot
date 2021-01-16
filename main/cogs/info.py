from typing import Optional

import discord
from discord.ext import commands


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="userinfo", aliases=["memberinfo", "ui", "mi"])
    async def userinfo_command(self, ctx, target: Optional[discord.Member]):
        target = target or ctx.author
        
        embed = discord.Embed(
            title="User Information",
            colour=target.colour,
            timestamp=ctx.message.created_at
        )
        
        embed.set_thumbnail(url=target.avatar_url)
        
        fields = [
            ("Name", str(target), True),
            ("ID", target.id, True),
            ("Status", str(target.status).title(), True),
            ("Joined Discord", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), True)
        ]
        
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        
        await ctx.send(embed=embed)
    
    
    
    @commands.command(name="serverinfo", aliases=["si"])
    async def userinfo_command(self, ctx):
        
        embed = discord.Embed(
            title="Server Information",
            colour=ctx.author.color,
            timestamp=ctx.message.created_at
        )

        embed.set_thumbnail(url=ctx.guild.icon_url)
        
        fields = [  ("ID", ctx.guild.id, True),
                    ("Owner", ctx.guild.owner, True),
                    ("Region", ctx.guild.region, True),
                    ("Created at", ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
                    ("Members", len(ctx.guild.members), True),
                    ("Banned members", len(await ctx.guild.bans()), True),
                    ("Text channels", len(ctx.guild.text_channels), True),
                    ("Voice channels", len(ctx.guild.voice_channels), True),
                    ("Categories", len(ctx.guild.categories), True),
                    ("Roles", len(ctx.guild.roles), True),
                    ("Invites", len(await ctx.guild.invites()), True)
        ]
        
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        
        await ctx.send(embed=embed)
    
    

def setup(bot):
    bot.add_cog(Information(bot))
