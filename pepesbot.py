import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import platform
import colorsys
import random
import os
import time
from discord.voice_client import VoiceClient
from discord import Game, Embed, Color, Status, ChannelType









bot=commands.Bot(command_prefix='P!')

@client.event
async def on_ready():
  print("The bot is ready and connected to Discord!")
  
@client.event
async def Ping():
  await client.send_message("Pong!")
  
@client.run(os.getenv("BOT_TOKEN"))
