import discord

# Track Image Function 
async def ImagePost(bot,imageToPrint):
    channel = bot.get_channel(971052643470413859) # Specify the channel where to post   
    await channel.send(imageToPrint) # Send the Image his Name in Discord
