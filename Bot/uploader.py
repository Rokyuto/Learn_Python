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

"""
# Call Tracker 
def call_tracker():
    print(os.getcwd())

    file = 'python Bot\\tracker.py' # Initilialize tracker.py to track for new Image and Download it
    # Run tracker.py
    trackImage = subprocess.Popen(file)
    out, err = trackImage.communicate()
""" 
   

# Bot Command Text = image
# Send Image in Discord function
@bot.command(pass_context=True)
async def image(ctx):
    #call_tracker() # Call Tracker function

    # Get the Newest Image, saved in 'Bot\Images', from tracker.py file by the variable 'newestImage'
    with os.scandir(os.getcwd()) as dirs: # Scan the current working directory (Saving Directory)
        for entry in dirs: # for each finded object
            #Image = entry.name # Update Saved Image
            await ctx.send(file=discord.File(entry)) # Send Image in Discord


# Bot Token (Initialize the Bot)
bot.run('token')
