import time
import discord
from discord.ext import commands 
from discord.ext.commands import bot
import asyncio
import datetime
import subprocess
import KPoPTracker
import os

# Bot Token
token = 'token'

# Bot Command Prefix
bot = commands.Bot(command_prefix='!')

# Startup Bot 
@bot.event
async def on_ready():
    print("Connected!...")
    await delay()


async def delay():
    while True: # Infinity Loop
        
        # Calculate the delay
        now = datetime.datetime.now()
        then = now+datetime.timedelta(seconds=2)
        wait_time = (then-now).total_seconds()
        
        await asyncio.sleep(wait_time) # Wait the delay time

        await KPoPTracker.CheckImage(bot) # Call Tracker Function from tracker.py    
        #await ImageTracker() # Call Function to Track for New Image

# Bot Token (Initialize the Bot)
bot.run(token)
