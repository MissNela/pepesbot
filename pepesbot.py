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







client = commands.Bot(command_prefix = 'P!')

@client.event
async def on_ready():
    print("The bot is online and connected with Discord!")

@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.content.startswith('Ping'):
        await client.send_message(message.channel, ":ping_pong: Pong!")

@client.run(os.getenv("BOT_TOKRN"))
