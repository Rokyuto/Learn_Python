import time
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

imageDir = os.path.dirname('Images/') # Get Saving Image Directory

initialDir = os.getcwd() # Get tge Current directory (Initial directory)
# print("Initial Directory: ", initialDir) # Debug Print

# Startup Bot 
@bot.event
async def on_ready():
    print("Connected!...")


# Track Image Function 
def call_tracker():
    tracker.TrackImage() # Call Tracker Function from tracker.py
    
    # Change the Current Working Directory to the Given Directory (Images Saving Directory)
    os.chdir(os.path.join(os.getcwd(), imageDir)) # Now we will be able to get the Saved Image
   

# Bot Command Text = image
# Send Image in Discord function
@bot.command(pass_context=True)
async def image(ctx):
    call_tracker() # Call Tracker function
    
    #print("Mid Directory: ", os.getcwd()) # Debug Print

    # Get the Newest Image, saved in 'Bot\Images', from tracker.py file by the variable 'newestImage'
    with os.scandir(os.getcwd()) as dirs: # Scan the current working directory (Saving Directory)
        for entry in dirs: # for each finded object
            #Image = entry.name # Update Saved Image
            await ctx.send(file=discord.File(entry)) # Send Image in Discord
            
    # Return to the Initial Project (Bot) Directory
    os.chdir(initialDir)
    #print("End Directory: " , os.getcwd()) # Debug Print

# Bot Token (Initialize the Bot)
bot.run('token')
