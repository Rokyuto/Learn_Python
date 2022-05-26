import time
from urllib.request import Request
from bs4 import BeautifulSoup
import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime
import subprocess
import KPoPTracker
import os
import requests 

# Bot Token
token = 'token'

# Bot Command Prefix
bot = commands.Bot(command_prefix='!')

bot_commandsDict = {
    "!kpop_bot_commands": "View Bot Commands",
    "!kpop_idols_list": "View List with Idols for Tracking",
    "!kpop_groups_list": "View List with Groups for Tracking",
    "!kpop_add_idol": "Add Idol for Tracking",
    "!kpop_add_group": "Add Group for Tracking",
    "!kpop_clear_idols_list": "Clear List with Idols",
    "!kpop_clear_groups_list": "Clear List with Groups",
    "!kpop_remove_idol": "Remove Idol from Tracking List",
    "!kpop_remove_group": "Remove Group from Tracking List"

}
groupsList = []
idolsList = []

groupsLinksList = []
idolsLinksList = []

KPOPlist = None  # Total List with all Groups and Idols for Tracking
KPOPLinksList = idolsLinksList + groupsLinksList


# Startup Bot
@bot.event
async def on_ready():
    print("Connected...")
    #await f_delayed_call() # Call the function when the bot is Started


# Loop the Bot and call Image Check from KPOP Tracker File with 2 seconds timeout
async def f_delayed_call():
    while True:  # Infinity Loop

        # Calculate the delay
        now = datetime.datetime.now()
        then = now+datetime.timedelta(seconds=2)
        wait_time = (then-now).total_seconds()

        await asyncio.sleep(wait_time)  # Wait the delay time

        # Call Tracker Function from tracker.py
        await KPoPTracker.CheckImage(bot,KPOPLinksList)
        # await ImageTracker() # Call Function to Track for New Image


# Display All Bot Commands Function
@bot.command(pass_context=True)
async def kpop_bot_commands(ctx):
    # The Bot Prints all Commands, which he have
    await ctx.send("My Bot Commands: ")
    for key, value in bot_commandsDict.items():
        currentCommand = key + ' : ' + value
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


# Get the Default Website Page Container
def f_BaseURL():
    global baseURLnewestCategory
    # Default Website Page
    baseURL = 'https://kpopping.com/kpics/gender-female/category-all/idol-any/group-any/order'
    baseURLpage = requests.get(baseURL)
    baseURLsoup = BeautifulSoup(baseURLpage._content, 'html.parser')
    baseURLimages = baseURLsoup.find(class_='box pics infinite')
    baseURLnewestCategory = baseURLimages.find(class_='matrix matrix-breezy mb-2')
    
    return baseURLnewestCategory

# Get the Entered Idol Website Page Container
def f_IdolURL(idol):
    idolURL = f'https://kpopping.com/kpics/gender-female/category-all/idol-{idol}/group-any/order'
    idolURLpage = requests.get(idolURL)
    idolURLsoup = BeautifulSoup(idolURLpage._content, 'html.parser')
    idolURLimages = idolURLsoup.find(class_='box pics infinite')
    idolURLnewestCategory = idolURLimages.find(class_='matrix matrix-breezy mb-2')
    
    return idolURLnewestCategory

def f_GroupURL(group):
    groupURL = f'https://kpopping.com/kpics/gender-female/category-all/idol-any/group-{group}/order'
    groupURLpage = requests.get(groupURL)
    groupURLsoup = BeautifulSoup(groupURLpage._content, 'html.parser')
    groupURLimages = groupURLsoup.find(class_='box pics infinite')
    groupURLnewestCategory = groupURLimages.find(class_='matrix matrix-breezy mb-2')
    
    return groupURLnewestCategory

 # Function to Add Entered after Bot Command Idol for Tracking
@bot.command(pass_context=True)
async def kpop_add_idol(ctx, idolToAdd):  # Example: !kpop_add_idol rose
    idol = idolToAdd.lower()  # Format Entered Idol to lowercase
    
    #f_BaseURL()
    #f_IdolURL(idol)
    
    baseURLnewestCategory = f_BaseURL() # Get the Default Website Page Container
    idolURLnewestCategory = f_IdolURL(idol) # Get the Entered Idol Website Page Container
    
    # Compare the two Containers
    if baseURLnewestCategory == idolURLnewestCategory: # If they are equal then the entered Idol is WRONG
        await ctx.send("Entered Idol is not Valid")
    else: # Entered Idol is Correct
        # Check if the new idol already exist
        if idol not in idolsList:
            # Add the Entered Idol to the Idols Tracking List
            idolsList.append(idol)
            idolsLinksList.append(f'https://kpopping.com/kpics/gender-female/category-all/idol-{idol}/group-any/order')
        else:
            await ctx.send(f'The Idol {idol} already exists in the List for Tracking')

        # Call Function to Update the Total List with all Groups and Idols for Tracking
        await d_KPOPsTracking(ctx)


# Function to Add Entered after Bot Command Group for Tracking
@bot.command(pass_context=True)
async def kpop_add_group(ctx, groupToAdd):
    group = groupToAdd.lower()  # Format Entered Group to lowercase
        
    baseURLnewestCategory = f_BaseURL() # Get the Default Website Page Container
    groupURLnewestCategory = f_GroupURL(group) # Get the Entered Idol Website Page Container
    
    # Compare the two Containers
    if baseURLnewestCategory == groupURLnewestCategory: # If they are equal then the entered Idol is WRONG
        await ctx.send("Entered Group is not Valid")
    else: # Entered Idol is Correct
        # Check if the new idol already exist
        if group not in groupsList:
            # Add the Entered Group to the Groups Tracking List
            groupsList.append(group)
            groupsLinksList.append(f'https://kpopping.com/kpics/gender-female/category-all/idol-any/group-{group}/order')
        else:
            await ctx.send(f'The Group {group} already exists in the List for Tracking')

        # Call Function to Update the Total List with all Groups and Idols for Tracking
        await d_KPOPsTracking(ctx)


# Clear the Idols Tracking List
@bot.command(pass_context=True)
async def kpop_clear_idols_list(ctx):
    idolsList.clear()
    # Clear idols links list
    await ctx.send("Clearing List with Idol for Tracking")


# Clear the Groups Tracking List
@bot.command(pass_context=True)
async def kpop_clear_groups_list(ctx):
    groupsList.clear()
    # Clear groups links list
    await ctx.send("Clearing Groups List for Tracking")


# Function to Remove Entered after Bot Command Idol for Tracking
@bot.command(pass_context=True)
async def kpop_remove_idol(ctx, idolToRemove):
    idol = idolToRemove.lower()  # Format Entered Idol to lowercase
        
    if idol in idolsList:
        
        # Remove Idol Link from IdolsLinks List
        idolLinkIndex = idolsList.index(idol)
        idolsLinksList.pop(idolLinkIndex) # Pop = remove
        print(idolsLinksList)
        
        # Remove the Entered Idol from the Idols Tracking List
        idolsList.remove(idol)
        # Print what happened
        await ctx.send(f'Removing {idol} from Tracking List')

        # Call Function to Update the Total List with all Groups and Idols for Tracking
        await d_KPOPsTracking(ctx)

    else:
        await ctx.send(f'The Entered Idol : {idol} do not exist in the Idols Tracking List')


# Function to Remove Entered after Bot Command Group for Tracking
@bot.command(pass_context=True)
async def kpop_remove_group(ctx, groupToRemove):
    group = groupToRemove.lower()  # Format Entered Group to lowercase
    
    if group in groupsList:
        
        # Remove Group Link from GroupsLinks List
        groupLinkIndex = idolsList.index(group)
        groupsLinksList.pop(groupLinkIndex) # Pop = remove
        print(groupsLinksList)
        
        # Remove the Entered Group from the Groups Tracking List
        groupsList.remove(group)
        # Print what happened
        await ctx.send(f'Removing {group} from Tracking List')

        # Call Function to Update the Total List with all Groups and Idols for Tracking
        await d_KPOPsTracking(ctx)

    else:
        await ctx.send(f'The Entered Group : {group} do not exist in the Groups Tracking List')


# Function to Update KPOPs for Tracking
async def d_KPOPsTracking(ctx):
    global KPOPlist
    global KPOPLinksList
    # Update Total List with all Groups and Idols for Tracking and Their Links
    KPOPlist = idolsList + groupsList
    KPOPLinksList = idolsLinksList + groupsLinksList
    await ctx.send(f'KPOPs for Tracking: {KPOPlist}')  # Print the List
    

# Bot Token (Initialize the Bot) and Run him
bot.run(token)
