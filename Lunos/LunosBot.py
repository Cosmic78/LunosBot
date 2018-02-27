#Lunos 0.5 by Cosmic
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

print("Initializing bot... \n")

bot = commands.Bot(command_prefix=">")

#Commands and Other things
@bot.event
async def on_ready():
    print("Lunos 0.5")
    print(discord.__version__)
    print("__***Commands***__ \n >Help \n >ping \n >slap")

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("**pong**")
    print("Someone has done a ping command")

@bot.command(pass_context=True)
async def Help(ctx):
    await bot.say("__***Commands***__ \n >Help \n >ping \n >slap")
    print("Help has been asked for")

@bot.command(pass_context=True)
async def slap(ctx, user: discord.Member):
    await bot.say("You have slapped %s :wave:" %user.name)
    print("Someone just got slapped")
#Commands and Other things

bot.run("NDA1ODMzNzk3NzkyNDMyMTI4.DXD9yQ.P1Gr72GxvVlnYhZPTxGcCQSOweg")
