import os
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
import KPoPPost

# Initialize Variables
baseURL = 'https://kpopping.com/kpics/gender-female/category-all/idol-any/group-any/order' # Website Default URL
lastImage = None
newestImage = None
newestElementHREF = None # Last Image Initial Value
lastKPOPImagesList = [] # List with Last Image for each KPOP Link

# Function to retrieve the last images from lastFilterImages.txt document and save them in lastKPOPImagesList
def f_RestoreLastKPOPImagesList():
    global lastKPOPImagesList
    file_lastFilterImages = open('txt/lastFilterImages.txt') # Open file
    all_lines = file_lastFilterImages.readlines() # Read all lines
    lastKPOPImagesList = [line[:-1] for line in all_lines] # Write each line in the List as new element (line[:-1] -> remove \n from each line because they are on new lines)
    return lastKPOPImagesList # Save and Return lastKPOPImagesList


# Function to change lastKPOPImagesList size when the user add new KPOP for tracking
def f_FillLastKPOPImagesList(KPOPLinksList):
    if len(lastKPOPImagesList) < len(KPOPLinksList): # If lastKPOPImagesList is smaller than KPoPLinksList
        lastKPOPImagesList.append(None) # The lastKPOPImagesList will receive new Index and the Value will be None
    

def FindNewestImage(KPOPLink):
    global newestElementHREF
    URL = KPOPLink

    page = requests.get(URL) # Call the Website
    soup = BeautifulSoup(page._content, 'html.parser') # Parse the Website to be able to get information || Get all information in the website 
    images = soup.find(class_='box pics infinite') # Get Container with all Idols Images
    
    newestCategory = images.find(class_='matrix matrix-breezy mb-2') # Get the Newest Children Idols Images Container
    newestElement = newestCategory.find(class_='cell') # Get the Newest Element in the Category
    newestElementHREF = newestElement.find('a')['href'] # Get the Newest Element' Image
    
    return newestElementHREF # Return and Update the newest Element href 


async def CheckImage(bot,KPOPLinksList): 
    # Check if the KPOP Links List has any Links
    if (len(KPOPLinksList) > 0): # If TRUE then it will go Check for new Images in this Link else (if false) the bot won't do anything    
        global lastKPOPImagesList   
        
        for link in KPOPLinksList:        
            f_SearchMachine(link) # Call Funtion to get the newest Image Photo from newest Element HREF
            
            currentLinkIndex = KPOPLinksList.index(link) # Get the Index of the current Link
                                    
            if newestImage != lastKPOPImagesList[currentLinkIndex]:
                lastKPOPImagesList[currentLinkIndex] = newestImage # Update the last Image for current KPoP
                
                #print(lastKPOPImagesList)
                
                # Rewrite the lastFilterImages.txt document with lastKPOPImagesList elements
                with open('txt/lastFilterImages.txt', "w") as lastFilterImages:
                    for currentElement in lastKPOPImagesList:
                        lastFilterImages.writelines(f"{currentElement}\n")
                
                await KPoPPost.ImagePost(bot, newestImage) # Call KPoPPost.ImagePost() Function
                
    else:
        global lastImage # Initialize Last Image
        f_SearchMachine(baseURL)
        
        with open('txt/lastLink.txt', "r") as lastLinkFile:
            lastLink = lastLinkFile.read()
        
        if newestImage != lastImage and newestImage != lastLink: # If the newest image is not the same as the last image and is different from the saved link in lastLink.txt 
                await KPoPPost.ImagePost(bot, newestImage) # Call KPoPPost.ImagePost() Function
                lastImage = newestImage # Update last Image
                # Update the Link in lastLink.txt to the newest
                with open('txt/lastLink.txt', "w") as lastLinkFile:
                    lastLinkFile.write(newestImage)
                    print("Updated lastLink.txt with the newestImage")
        else: # If the newest image is the same as the last link in lastLink.txt or the same as the lastImage
            print("The newestImage is the Same as the last")


# Funtion to get the newest Image from newest Element HREF
def f_SearchMachine(link):
    FindNewestImage(link) # Call Finding Newest Image href function
    global newestImage
    
    newestElementLink = "https://kpopping.com% s" % newestElementHREF #  Newest Element Website URL
    newestElementPage = requests.get(newestElementLink)# Newest Element URL 
    newestElementSoup = BeautifulSoup(newestElementPage._content, 'html.parser') # Parse the Website to be able to get information || Get all information in the website 
    
    newestImageDiv = newestElementSoup.find(class_='justified-gallery') # Get the Newest Element Div Object
    newestImageLink = newestImageDiv.find('img')['src'] # Get the Newest Element Link / Src  
    newestImageLinkTrim = urlparse(newestImageLink).path # Trim the Image to Remove Everithing after Image Format (.jpeg)
    newestImage = "https://kpopping.com% s" % newestImageLinkTrim # Build newest Image ImageURL
    
    return newestImage
