import time
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
import KPoPPost
import csv

# Initialize Variables
baseURL = 'https://kpopping.com/kpics/gender-female/category-all/idol-any/group-any/order' # Website Default URL
lastImage = None
newestImage = None
newestElementHREF = None # Last Image Initial Value
lastKPOPImagesList = [] # List with Last Image for each KPOP Link
lastImageThumb = None # Last Image which is the first in the container of the newest posted , also it's thumbnail of the newest cell in the website
newestImagesList = [] # List with the Newest Posted Images for any Idol

# Function to retrieve the last images from lastFilterImages.txt document and save them in lastKPOPImagesList
def f_RestoreLastKPOPImagesList():
    global lastKPOPImagesList
    file_lastFilterImages = open("csv/filter.csv", "r") # Open filter.csv in read mode
    csvReader = csv.reader(file_lastFilterImages) # CSV reader
    for line in csvReader: # For each Line
        lastKPOPImagesList.append(line[3]) # Append to lastKPOPImagesList each row Image (Last Column Value)
    return lastKPOPImagesList # Save and Return lastKPOPImagesList


# Function to change lastKPOPImagesList size when the user add new KPOP for tracking
def f_FillLastKPOPImagesList(KPOPLinksList):
    if len(lastKPOPImagesList) < len(KPOPLinksList): # If lastKPOPImagesList is smaller than KPoPLinksList
        lastKPOPImagesList.append(None) # The lastKPOPImagesList will receive new Index and the Value will be None    
        

def FindNewestImagesHREF(KPOPLink):
    global newestElementHREF
    URL = KPOPLink
    page = requests.get(URL) # Call the Website
    soup = BeautifulSoup(page._content, 'html.parser') # Parse the Website to be able to get information || Get all information in the website 
    try:
        images = soup.find(class_='box pics infinite') # Get Container with all Idols Images || 
        newestCategory = images.find(class_='matrix matrix-breezy mb-2') # Get the Newest Children Idols Images Container ||
        newestElement = newestCategory.find(class_='cell') # Get the Newest Element in the Category
        newestElementHREF = newestElement.find('a')['href'] # Get the Newest Element' Image
    except Exception as exception:
        print(exception)
        time.sleep(60)
        FindNewestImagesHREF(baseURL)
    
    return newestElementHREF # Return and Update the newest Element href ( Open the newest Cell (newest postet idol pictures) )


async def CheckImage(bot,KPOPLinksList):
    global newestImagesList
    # Check if the KPOP Links List has any Links
    if (len(KPOPLinksList) > 0): # If TRUE then it will go Check for new Images in this Link else (if false) the bot won't do anything    
        global lastKPOPImagesList   
        
        for link in KPOPLinksList:        
            f_SearchMachine(link) # Call Funtion to get the newest Image Photo from newest Element HREF
            
            currentLinkIndex = KPOPLinksList.index(link) # Get the Index of the current Link
            
            for currentImg in newestImagesList: # Get each Idol Image in the List                
                if currentImg != lastKPOPImagesList[currentLinkIndex]:
                    lastKPOPImagesList[currentLinkIndex] = currentImg # Update the last Image for current KPoP
                    
                    tempList = [] # Temp List fot Filling with the edited rows
                    filter=open("csv/filter.csv","r") # Open filter.csv in read mode
                    csvReader=csv.reader(filter) # Create csv reader object by the help of csv library for filter.csv
                    i=0
                    for row in csvReader:
                        row[3] = lastKPOPImagesList[i] # Update Row Last Image (last Column)
                        tempList.append(row) # Append the row for the tempList
                        i+=1 
                    filter=open("csv/filter.csv","w",newline='') # Open filter.csv in write mode
                    csvWriter=csv.writer(filter) # Create csv writer object by the help of csv library for filter.csv
                    csvWriter.writerows(tempList) # Rewrite the filter.csv rows with the tempList
                    filter.close() # Close the file

                    await KPoPPost.ImagePost(bot, currentImg) # Call KPoPPost.ImagePost() Function to Post each Idol Image in the List
                
    else:
        global lastImage # Initialize Last Image
        global lastImageThumb # Last Image Thumbnail of the newest cell in the website
        
        f_SearchMachine(baseURL)
        
        with open('txt/lastLink.txt', "r") as lastLinkFile:
            lastLink = lastLinkFile.read()
            if lastImageThumb != lastLink:
                for currentImg in newestImagesList: # Get each Idol Image in the List 
                    # If the newest image is not the same as the last image and is different from the saved link in lastLink.txt  
                    if currentImg != lastImage and currentImg != lastLink:
                        await KPoPPost.ImagePost(bot, currentImg) # Call KPoPPost.ImagePost() Function
                        
                lastImage = lastImageThumb
                with open('txt/lastLink.txt', "w") as lastLinkFile:
                    lastLink = lastLinkFile.write(lastImage)
                    print("Updated lastLink.txt with the newestImage")
            else: # If the newest image is the same as the last link in lastLink.txt or the same as the lastImage
                print("The newestImage is the Same as the last")
        


# Funtion to get the newest Image from newest Element HREF
def f_SearchMachine(link):
    FindNewestImagesHREF(link) # Call Finding Newest Image href function
    # Initialize Variables
    global newestImage
    global lastImage
    global lastImageThumb # Last Image Thumbnail of the newest cell in the website
    global newestImagesList
    
    newestElementLink = "https://kpopping.com% s" % newestElementHREF #  Newest Element Website URL
    newestElementPage = requests.get(newestElementLink)# Newest Element URL 
    newestElementSoup = BeautifulSoup(newestElementPage._content, 'html.parser') # Parse the Website to be able to get information || Get all information in the website 
    newestImageDiv = newestElementSoup.find(class_='justified-gallery') # Get the Newest Images Element Div Object

    # Update Last Image which is the first in the container of the newest posted , also it's thumbnail of the newest cell in the website
    lastImageThumb = findNewImage(newestImageDiv.find('img')['src'])
    if newestImageDiv != None and lastImageThumb != None :
        if lastImage != lastImageThumb:
            # newestImageDiv.findAll('img') => Find All Images in the Div Contatiner
            for image in newestImageDiv.findAll('img'): # Itterate through All Images in the Div Contatiner
                
                # Append Image to newest Images List
                newestImagesList.append(findNewImage(image['src'])) # image['src'] => Get the Newest Element Link / Src
            
            return newestImagesList
    else:
        time.sleep(5)
        f_SearchMachine(baseURL)


def findNewImage(newImageLink):
    newImageLinkTrim = urlparse(newImageLink).path # Trim the Image to Remove Everithing after Image Format (.jpeg)
    newImage = "https://kpopping.com% s" % newImageLinkTrim # Build new Image ImageURL
    return newImage
