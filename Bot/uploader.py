import discord
from discord.ext import commands 
from discord.ext.commands import bot
import asyncio
import datetime as dt
import subprocess
import tracker
import os

# Bot Command Prefix
bot = commands.Bot(command_prefix='!')

# Startup Bot 
@bot.event
async def on_ready():
    print("Connected!...")


# Call Tracker 
def call_tracker():
    file = 'python Bot\\tracker.py' # Initilialize tracker.py to track for new Image and Download it
    # Run tracker.py
    trackImage = subprocess.Popen(file)
    out, err = trackImage.communicate()
   
   

# Bot Command Text = image
# Send Image in Discord function
@bot.command(pass_context=True)
async def image(ctx):
    call_tracker() # Call Tracker function

    # Send Image in Discord
    await ctx.send(file=discord.File(tracker.SavedImage))


# Bot Token (Initialize the Bot)
bot.run('Nzk4NjExMTIxNTI3MzI0Njky.X_3ikA.0PbLyw5QOcDpxuF9Fb3CgVGRYrc')
