# Imports
import os

import discord
from discord.ext import commands
from discord.ext.commands import Bot as Botbase
from discord.ext.commands import (Cog, CommandOnCooldown, Context,
                                  MissingPermissions, NotOwner,
                                  has_permissions, when_mentioned_or)
from discord.ext.commands.errors import (BadArgument, CommandNotFound,
                                         MissingRequiredArgument)
from discord.utils import get

intents = discord.Intents.default()
intents.members = True
intents.presences = True

# Prefix and More
OWNER_IDS = [703686351111061605]
IGNORE_EXCEPTIONS = (CommandNotFound, BadArgument)

class Bot(Botbase):
    def __init__(self):
        self.ready = False
        
        super().__init__(command_prefix="!", owner_ids=OWNER_IDS, intents=intents)
    
    def load(self):
        extentions = [
            "main.cogs.app",
            "main.cogs.fun"
        ]
        
        for ext in extentions:
            self.load_extension(ext)
            print(ext)
        
    def run(self, version):
        self.VERSION = version
        
        self.load()
        
        self.TOKEN = open("./data/restricted/token.txt", "r").read()
        
        super().run(self.TOKEN, reconnect=True)
    
    async def on_ready(self):
        if not self.ready:
            self.ready = True
            
            app = self.get_cog("App")
            await app.set()
            
            print("Bot ready!")
        
        else:
            print("Bot reconnected.")
    
bot = Bot()