import discord
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="hello")
    async def hello_command(self, ctx):
        
        embed = discord.Embed(title="Hello", description=f"Hello and welcome {ctx.author.mention}!")#
        
        embed.add_field(name="This is a greeting to:", value=ctx.author.mention, inline=True)
        
        embed.set_author(name="Basement Bot", icon_url="https://www.finishedbasementsplus.com/wp-content/uploads/2020/01/highland-mi-open-basement-design-fireplace.jpg")
        
        await ctx.send(embed=embed)
        
    
    

def setup(bot):
    bot.add_cog(Fun(bot))