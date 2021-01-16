import discord
from discord.ext import commands

response = ["Sorry but I can't do that."]

def extract_from_text(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    
    return l

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    return a/b

def pow(a, b):
    return a**b

def sorry():
    return response[0]

operations={'ADD':add,'PLUS':add,'SUM':add,'ADDITION':add, 
        'SUB':sub,'SUBTRACT':sub,'MINUS':sub,'DIFFERENCE':sub,
        'PRODUCT':mul,'MULTIPLY':mul,'MULTIPLICATION':mul, 
        'DIVISION':div,
        'POW':pow,'POWER':pow}

class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="math", aliases=["m", "mt"])
    async def math_command(self, ctx):
        text=str(ctx.message.content)
        
        for word in text.split(' '):
            if word.upper() in operations.keys():
                try:
                    l = extract_from_text(text)
                    r = operations[word.upper()] (l[0],l[1])
                    await ctx.send(r)
                except:
                    await ctx.send("I'm sorry but I can't do that.")
                finally:
                    break
        else:
            await ctx.send(sorry())
        
        

def setup(bot):
    bot.add_cog(Math(bot))
    