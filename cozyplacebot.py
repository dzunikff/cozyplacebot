##############################
# Imports
##############################

import discord
import requests
import os
import random
from discord.ext import commands, tasks
import asyncio

##############################
# Dotenv
##############################

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TOKEN")

##############################
# Intents & Description
##############################

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)
description = "Bot is online!"
bot = discord.Bot()

##############################
# Login Terminal Output
##############################


@bot.event
async def on_ready():
    print(description)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'Cozy Place Tournaments Bot | Created by LinHidden'))

##############################
# Commands
##############################


@bot.slash_command(name="greetings",
                   description="Greetings!",
                   options=[])
async def hello(ctx):
    name = ctx.author.mention
    await ctx.respond(f"Hello {name}!")


@bot.slash_command(name="calculate",
                   description="Any numbers, any output.",
                   options=[])
async def calc(ctx, operation: str):
    await ctx.respond("Your answer is: " + str(eval(operation.replace(' ', ''))) + "!")


@bot.slash_command(name="ping",
                   description="Outputs bot's latency",
                   options=[])
async def ping(ctx):
    await ctx.respond(f'Pong! In {round(bot.latency * 1000)}ms')


##############################
# Running bot with token from dotenv
##############################

bot.run(TOKEN)
