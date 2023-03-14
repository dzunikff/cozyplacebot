from dotenv import load_dotenv
from nextcord import Interaction, SlashOption, ChannelType
from nextcord.abc import GuildChannel
from nextcord.ext import commands
import nextcord
import os
import discord
import random
import asyncio
import json


##############################
# Dotenv
##############################

load_dotenv()
TOKEN = os.getenv("TOKEN")

##############################
# Commands
##############################
bot = commands.Bot()

testingServerID = 1079665815533650000


@bot.event
async def on_ready():
    print("Bot is online!")


@bot.slash_command(name="st", description="Shows active tournaments", guild_ids=[testingServerID])
async def st(interaction: Interaction):
    await interaction.response.send_message(f"{interaction.user.mention}, there are none active tournaments. Try again later!", ephemeral=True)


@bot.slash_command(name="jt", description="Tries to join an active tournament", guild_ids=[testingServerID])
async def jt(interaction: Interaction):
    await interaction.response.send_message(f"{interaction.user.mention}, there are none active tournaments. Try again later!", ephemeral=True)


@bot.slash_command(name="rt", description="Tries to register at an active tournament", guild_ids=[testingServerID])
async def rt(interaction: Interaction):
    await interaction.response.send_message(f"{interaction.user.mention}, сначала прочитайте информацию в <#1079733513269551154>, затем пройдите регистрацию в https://forms.gle/3cHCgDnSpuZV1cxS8.", ephemeral=True)


@bot.slash_command(name="ct", description="Просмотр зарегистрированных команд", guild_ids=[testingServerID])
async def ct(interaction: Interaction):
    data = json.load(open('registered_teams.json', 'r'))
    await interaction.response.send_message(data['team_name'], ephemeral=True)


@bot.slash_command(name="tw", description="Просмотр победителей турнира", guild_ids=[testingServerID])
async def tw(interaction: Interaction):
    data = json.load(open('tournament_winners.json', 'r'))
    await interaction.response.send_message(data['team_name'], ephemeral=True)


@bot.slash_command(name="tl", description="Выход из турнира", guild_ids=[testingServerID])
async def jt(interaction: Interaction):
    await interaction.response.send_message(f"{interaction.user.mention}, для выхода из турнира напишите <@535113125104582666>", ephemeral=True)

##############################
# Running bot with token from dotenv
##############################

bot.run(TOKEN)
