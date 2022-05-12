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
token = ''

# Bot Command Prefix
bot = commands.Bot(command_prefix='!')

bot_commandsDict = { 
                "!kpop_bot_commands" : "View Bot Commands" ,
                "!kpop_idols_list" : "View List with Idols for Tracking",
                "!kpop_groups_list" : "View List with Groups for Tracking",
                "!kpop_add_idol" : "Add Idol for Tracking" , 
                "!kpop_add_group" : "Add Group for Tracking" ,
                "!kpop_clear_idols_list" : "Clear List with Idols" ,
                "!kpop_clear_groups_list" : "Clear List with Groups" ,
                "!kpop_remove_idol" : "Remove Idol from Tracking List",
                "!kpop_remove_group" : "Remove Group from Tracking List"
                
                }
groupsList = []
idolsList = []

KPOPtrackings = None # Total List with all Groups and Idols for Tracking

# Startup Bot 
@bot.event
async def on_ready():
    print("Connected...")
    await delay()
    

# Loop the Bot
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
 
 
# Function to Display the Idols Tracking List
@bot.command(pass_context=True)
async def kpop_idols_list(ctx):
    await ctx.send("View KPOP Idols for Tracking List")
    await ctx.send(idolsList)
    

# Function to Display the Groups Tracking List
@bot.command(pass_context=True)
async def kpop_groups_list(ctx):
    await ctx.send("View KPOP Groups for Tracking List")
    await ctx.send(groupsList)

 
 # Function to Add Entered after Bot Command Idol for Tracking
@bot.command(pass_context=True)
async def kpop_add_idol(ctx, idolToAdd): # Example: !kpop_add_idol rose
    idol = idolToAdd.lower() # Format Entered Idol to lowercase
    idolsList.append(idol) # Add the Entered Idol to the Idols Tracking List
    
    await f_KPOPsTracking(ctx) # Call Function to Update the Total List with all Groups and Idols for Tracking
    
    await ctx.send(f'Adding IDOL {idol} for Tracking')  


# Function to Add Entered after Bot Command Group for Tracking
@bot.command(pass_context=True)
async def kpop_add_group(ctx, groupToAdd):
    group = groupToAdd.lower() # Format Entered Group to lowercase
    groupsList.append(group) # Add the Entered Group to the Idols Tracking List
    
    await f_KPOPsTracking(ctx) # Call Function to Update the Total List with all Groups and Idols for Tracking
    
    await ctx.send(f'Adding GROUP {group} for Tracking')
    

# Clear the Idols Tracking List
@bot.command(pass_context=True)
async def kpop_clear_idols_list(ctx):
    idolsList.clear()
    
    await ctx.send("Clearing List with Idol for Tracking")

    
# Clear the Groups Tracking List
@bot.command(pass_context=True)
async def kpop_clear_groups_list(ctx):
    groupsList.clear()
    
    await ctx.send("Clearing Groups List for Tracking")
  
 
# Function to Remove Entered after Bot Command Idol for Tracking
@bot.command(pass_context=True)
async def kpop_remove_idol(ctx, idolToRemove):
    idol = idolToRemove.lower() # Format Entered Idol to lowercase
    if idol in idolsList:
        idolsList.remove(idol) # Remove the Entered Idol from the Idols Tracking List
        await ctx.send(f'Removing IDOL {idol} from Tracking List') # Print what happened
        
        await f_KPOPsTracking(ctx) # Call Function to Update the Total List with all Groups and Idols for Tracking
        
    else:
        await ctx.send(f'The Entered Idol : {idol} do not exist in the Idols Tracking List')
    
 
# Function to Remove Entered after Bot Command Group for Tracking
@bot.command(pass_context=True)
async def kpop_remove_group(ctx, groupToRemove):
    group = groupToRemove.lower() # Format Entered Group to lowercase
    if group in groupsList:
        groupsList.remove(group) # Remove the Entered Group from the Groups Tracking List
        await ctx.send(f'Removing GROUP {group} from Tracking List') # Print what happened
        
        await f_KPOPsTracking(ctx) # Call Function to Update the Total List with all Groups and Idols for Tracking
        
    else:
        await ctx.send(f'The Entered Group : {group} do not exist in the Groups Tracking List')


# Function to Update KPOPs for Tracking
async def f_KPOPsTracking(ctx):
    KPOPtrackings = idolsList + groupsList; # Update Total List with all Groups and Idols for Tracking
    await ctx.send(f'KPOPs for Tracking: {KPOPtrackings}') # Print the List
  

# Bot Token (Initialize the Bot) and Run him
bot.run(token)
