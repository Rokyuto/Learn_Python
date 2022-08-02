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
import re
import csv

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

KPOPlist = []  # Total List with all Groups and Idols for Tracking
KPOPLinksList = []

# Startup Bot
@bot.event
async def on_ready():
    #print("Connected...")
    channel = bot.get_channel(971514773634162769)
    await channel.send("I'm online :)")
    f_restoreLists() # Restore Bot Searching Filters
    await f_delayed_call() # Call the function when the bot is Started

def f_restoreLists():
    global groupsList, idolsList, groupsLinksList, idolsLinksList
    # If filter.csv document is not empty then fill Filters Lists
    if(os.path.getsize('csv/filter.csv') != 0 ):
        filterFile = open('csv/filter.csv', "r") # Open the csv document in read mode
        csvReader=csv.reader(filterFile)
        for line in csvReader: # Read Second Column (idol or group)
            if(line[1] == 'idol'): # If it's found the word 'idol' on the line
                idolsList.append(line[0]) # Append the name of the Idol (filter.csv first column) to idolsList
                idolsLinksList.append(line[2]) # Append the Idol Link (filter.csv third column) to idolsLinksList
            else:
                groupsList.append(line[0]) # Append the name of the Group (filter.csv first column) to groupsList
                groupsLinksList.append(line[2]) # Append the Group Link (filter.csv third column) to groupsLinksList
                 
        KPOPlist.extend(groupsList)
        KPOPlist.extend(idolsList)

        KPOPLinksList.extend(groupsLinksList)
        KPOPLinksList.extend(idolsLinksList)
        
        print(KPOPlist)
        print(KPOPLinksList)
        filterFile.close()
    
        KPoPTracker.f_RestoreLastKPOPImagesList()
    
    return KPOPlist, KPOPLinksList, groupsList, idolsList, groupsLinksList, idolsLinksList # Return and Save Filters Lists


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

# Get the Entered Group Website Page Container
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
    
    baseURLnewestCategory = f_BaseURL() # Get the Default Website Page Container
    idolURLnewestCategory = f_IdolURL(idol) # Get the Entered Idol Website Page Container
    
    # Compare the two Containers
    if baseURLnewestCategory == idolURLnewestCategory: # If they are equal then the entered Idol is WRONG
        await ctx.send("Entered Idol is not Valid")
    else: # Entered Idol is Correct
        # Check if the new idol already exist
        if idol not in KPOPlist:
            # Add the Entered Idol to the Idols Tracking List
            idolsList.append(idol)
            idolsLinksList.append(f'https://kpopping.com/kpics/gender-female/category-all/idol-{idol}/group-any/order')
            
            with open('csv/filter.csv', 'a', newline='\n', encoding='utf-8') as filter: # Oppen Filter.csv file in append mode
                writer = csv.writer(filter)
                writer.writerow([idol,'idol',f'https://kpopping.com/kpics/gender-female/category-all/idol-{idol}/group-any/order', 'None']) # Append new Row to the Filter.csv
            filter.close()   
            
            KPOPlist.append(idol)
            KPOPLinksList.append(f'https://kpopping.com/kpics/gender-female/category-all/idol-{idol}/group-any/order')
            
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
        if group not in KPOPlist:
            # Add the Entered Group to the Groups Tracking List
            groupsList.append(group)
            groupsLinksList.append(f'https://kpopping.com/kpics/gender-female/category-all/idol-any/group-{group}/order')
            
            with open('csv/filter.csv', 'a', newline='\n', encoding='utf-8') as filter: # Oppen Filter.csv file in append mode
                writer = csv.writer(filter)
                writer.writerow([group,'group',f'https://kpopping.com/kpics/gender-female/category-all/idol-any/group-{group}/order', 'None']) # Append new Row to the Filter.csv
            filter.close()
            
            KPOPlist.append(group)
            KPOPLinksList.append(f'https://kpopping.com/kpics/gender-female/category-all/idol-any/group-{group}/order')
            
        else:
            await ctx.send(f'The Group {group} already exists in the List for Tracking')

        # Call Function to Update the Total List with all Groups and Idols for Tracking
        await d_KPOPsTracking(ctx)

# Clear the Idols Tracking List
@bot.command(pass_context=True)
async def kpop_clear_idols_list(ctx):
    global KPOPlist
    global KPOPLinksList
    
    idolsList.clear()
    idolsLinksList.clear()
    f_RewriteFilterFile(1,'idol') # Call Function to remove all filter idols from filter.csv
    
    KPOPlist = idolsList + groupsList
    KPOPLinksList = idolsLinksList + groupsLinksList
    
    # Clear idols links list
    await ctx.send("Clearing List with Idol for Tracking")
    await ctx.send(KPOPlist)
    
# Clear the Groups Tracking List
@bot.command(pass_context=True)
async def kpop_clear_groups_list(ctx):
    global KPOPlist
    global KPOPLinksList
 
    groupsList.clear()
    groupsLinksList.clear()
    f_RewriteFilterFile(1,'group') # Call Function to remove all filter groups from filter.csv

    KPOPlist = idolsList + groupsList
    KPOPLinksList = idolsLinksList + groupsLinksList
    
    # Clear groups links list
    await ctx.send("Clearing Groups List for Tracking")
    await ctx.send(KPOPlist)

# Function to Remove Entered after Bot Command Idol for Tracking
@bot.command(pass_context=True)
async def kpop_remove_idol(ctx, idolToRemove):
    idol = idolToRemove.lower()  # Format Entered Idol to lowercase
        
    if idol in idolsList:
        # Remove Idol Link from IdolsLinks List
        idolLinkIndex = idolsList.index(idol)
        idolsLinksList.pop(idolLinkIndex) # Pop = remove
        linkIndex = KPOPlist.index(idol)
        KPOPLinksList.pop(linkIndex)
        
        # Remove the Entered Idol from the Idols Tracking List
        idolsList.remove(idol)
        KPOPlist.remove(idol)
        
        f_RewriteFilterFile(0,idol) # Call Functio to remove the entered idol form filter.csv
        
        # Print what happened
        await ctx.send(f'Removing {idol} from Tracking List')
        
    else:
        await ctx.send(f'The Entered Idol : {idol} do not exist in the Idols Tracking List')

# Function to Remove Entered after Bot Command Group for Tracking
@bot.command(pass_context=True)
async def kpop_remove_group(ctx, groupToRemove):
    group = groupToRemove.lower()  # Format Entered Group to lowercase
    
    if group in groupsList:
        # Remove Group Link from GroupsLinks List
        groupLinkIndex = groupsList.index(group)
        groupsLinksList.pop(groupLinkIndex) # Pop = remove
        linkIndex = KPOPlist.index(group)
        KPOPLinksList.pop(linkIndex)
        #print(groupsLinksList)
        
        # Remove the Entered Group from the Groups Tracking List
        groupsList.remove(group)
        KPOPlist.remove(group)
        
        f_RewriteFilterFile(0,group) # Call Functio to remove the entered group form filter.csv
        
        # Print what happened
        await ctx.send(f'Removing {group} from Tracking List')

    else:
        await ctx.send(f'The Entered Group : {group} do not exist in the Groups Tracking List')

# Function to remove defined kpop category (idol/group) or defined kpop idol/group from filter.csv when the function is called
def f_RewriteFilterFile(index,kpop):
    filter=open("csv/filter.csv","r") # Open filter.csv in read mode
    csvReader=csv.reader(filter) # Create csv reader object by the help of csv library for filter.csv
    tempList = [] # Temp List,who will be filled with not defined kpop category (idol/group), when the function is called
    for row in csvReader: # For each Row in the filter.csv
        if (row[index]==kpop): # If column 2 (idol/group) of the row contains the defined kpop category (idol/group), then Skip (Continue)
            continue
        else:
            tempList.append(row) # Append the row to the tempList
            
    filter=open("csv/filter.csv","w",newline='') # Open filter.csv in write mode
    csvWriter=csv.writer(filter) # Create csv writer object by the help of csv library for filter.csv
    csvWriter.writerows(tempList) # Rewrite the filter.csv rows with the tempList
    filter.close() # Close the file
    tempList.clear() # Clear the tempList

# Function to Update KPOPs for Tracking
async def d_KPOPsTracking(ctx):
    KPoPTracker.f_FillLastKPOPImagesList(KPOPLinksList) # Update the last KPOP Images List's size
    await ctx.send(f'KPOPs for Tracking: {KPOPlist}')  # Print the List
    
# Bot Token (Initialize the Bot) and Run him
bot.run(token)
