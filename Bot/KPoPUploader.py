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

bot_commandsDict = { 
                "!kpop_bot_commands" : "View Bot Commands" ,
                "!kpop_clear_idols_list" : "Clear List with Idols" ,
                "!kpop_clear_groups_list" : "Clear List with Groups" ,
                "!kpop_add_idol" : "Add Idol for Tracking" , 
                "!kpop_add_group" : "Add Group for Tracking" ,
                "!kpop_idols_list" : "View List with Idols for Tracking",
                "!kpop_groups_list" : "View List with Groups for Tracking"
                }
groupsList = []
idolsList = []

# Startup Bot 
@bot.event
async def on_ready():
    print("Connected...")
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


# Display All Bot Commands Function
@bot.command(pass_context=True)
async def kpop_bot_commands(ctx):
    # The Bot Prints all Commands, which he have
    await ctx.send("My Bot Commands: ")
    for key,value in bot_commandsDict.items():
        currentCommand = key +' : '+ value
        await ctx.send(currentCommand)
 

@bot.command(pass_context=True)
async def kpop_clear_idols_list(ctx):
    idolsList.clear()
    
    await ctx.send("Clearing List with Idol for Tracking")
    
    
@bot.command(pass_context=True)
async def kpop_clear_groups_list(ctx):
    groupsList.clear()
    
    await ctx.send("Clearing Groups List for Tracking")
  
    
# Function to Add Entered after Bot Command Idol for Tracking
@bot.command(pass_context=True)
async def kpop_add_idol(ctx, idol): # Example: !kpop_add_idol rose
    idol = idol.lower() # Format Entered Idol to lowercase
    idolsList.append(idol) # Add the Entered Idol to the Idols Tracking List
    
    await ctx.send(f'Adding IDOL {idol} for Tracking')  


# Function to Add Entered after Bot Command Group for Tracking
@bot.command(pass_context=True)
async def kpop_add_group(ctx, group):
    group = group.lower() # Format Entered Group to lowercase
    groupsList.append(group) # Add the Entered Group to the Idols Tracking List
    
    await ctx.send(f'Adding GROUP {group} for Tracking')


@bot.command(pass_context=True)
async def kpop_idols_list(ctx):
    await ctx.send(idolsList)
    
    await ctx.send("View KPOP Idols for Tracking List")


@bot.command(pass_context=True)
async def kpop_groups_list(ctx):
    await ctx.send(groupsList)
    
    await ctx.send("View KPOP Groups for Tracking List")


# Bot Token (Initialize the Bot) and Run him
bot.run(token)
