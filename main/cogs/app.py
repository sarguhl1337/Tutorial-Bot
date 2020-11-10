import discord
from discord import Activity, ActivityType
from discord.ext import commands
from discord.ext.commands import Cog


class App(Cog):
    def __init__(self, bot):
        self.bot = bot
        
        self._message = "listening Cool Music"
        
    @property
    def message(self):
        return self._message
    
    @message.setter
    def message(self, value):
        if value.split(" ")[0] not in ("playing", "watching", "listening"):
            raise ValueError("Invalit Activity Type")
        
        self._message = value
        
    async def set(self):
        _type, _name = self.message.split(" ", maxsplit=1)
        
        await self.bot.change_presence(activity=Activity(name=_name, type=getattr(ActivityType, _type, ActivityType.playing)))

def setup(bot):
    bot.add_cog(App(bot))