import os
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
import KPoPPost

#global newestImage
#lastImage = None # Last Image Initial Value
# Initialize Variables
newestElementHREF = None # Last Image Initial Value
lastKPOPImagesList = [] # List with Last Image for each KPOP Link

# Function to change lastKPOPImagesList size when the user add new KPOP for tracking
def f_FillLastKPOPImagesList(KPOPLinksList):
    if len(lastKPOPImagesList) < len(KPOPLinksList): # If lastKPOPImagesList is smaller than KPoPLinksList
        #for index in range(len(lastKPOPImagesList), len(KPOPLinksList)): # The lastKPOPImagesList will receive new Index 
            #print ("Filling index: ", index)
        lastKPOPImagesList.append(None) # The lastKPOPImagesList will receive new Index and the Value will be None
         
        # Debug Prints   
        # print("KPOPLinksList ", len(KPOPLinksList))
        # print("lastKPOPImagesList ", len(lastKPOPImagesList))
        # print("lastKPOPImagesList elements" , lastKPOPImagesList)
        
    #lastKPOPImagesList = [None] * len(KPOPLinksList)
    

def FindNewestImage(KPOPLink):
    global newestElementHREF
    #URL = 'https://kpopping.com/kpics/gender-female/category-all/idol-any/group-any/order' # Website URL
    URL = KPOPLink

    page = requests.get(URL) # Call the Website
    
    soup = BeautifulSoup(page._content, 'html.parser') # Parse the Website to be able to get information || Get all information in the website 
    
    images = soup.find(class_='box pics infinite') # Get Container with all Idols Images
    
    newestCategory = images.find(class_='matrix matrix-breezy mb-2') # Get the Newest Children Idols Images Container
    
    newestElement = newestCategory.find(class_='cell') # Get the Newest Element in the Category
    
    newestElementHREF = newestElement.find('a')['href'] # Get the Newest Element' Image
    
    return newestElementHREF # Return and Update the newest Element href 


async def CheckImage(bot,KPOPLinksList):
    #print(KPOPLinksList) # Debug Print
    
    # Check if the KPOP Links List has any Links
    if (len(KPOPLinksList) > 0): # If TRUE then it will go Check for new Images in this Link else (if false) the bot won't do anything
        for link in KPOPLinksList:          
            #global lastImage # Initialize Last Image
            FindNewestImage(link) # Call Finding Newest Image href function
            
            #newestElementName = newestElementImg['src'] # Get the Newest Element Name
            #newestElementNameFormated = newestElementName.replace(" ", "-").replace("---", "-") # Forma the Newest Element Name
            
            newestElementLink = "https://kpopping.com% s" % newestElementHREF #  Newest Element Website URL

            newestElementPage = requests.get(newestElementLink)# Newest Element URL 
            
            newestElementSoup = BeautifulSoup(newestElementPage._content, 'html.parser') # Parse the Website to be able to get information || Get all information in the website 
            
            newestImageDiv = newestElementSoup.find(class_='justified-gallery') # Get the Newest Element Div Object
            
            newestImageLink = newestImageDiv.find('img')['src'] # Get the Newest Element Link / Src
            
            newestImageLinkTrim = urlparse(newestImageLink).path # Trim the Image to Remove Everithing after Image Format (.jpeg)

            newestImage = "https://kpopping.com% s" % newestImageLinkTrim # Build newest Image ImageURL
            
            
            #print("NEW: ",newestImageLinkTrim) # Debug Print
            #print("OLD: ",lastImage) # Debug Print
            # Debug Prints
            #print("Link: " , link)
            currentLinkIndex = KPOPLinksList.index(link)
            # print("Current Link Index: " , currentLinkIndex)
            # print("lastKPOPImagesList Range: ", len(lastKPOPImagesList))
            # print("lastKPOPImagesList: " , lastKPOPImagesList)
            
            # Error with lastKPOPImagesList lenght
            
            # if newestImage != lastImage: # If the newest image is not the same as the last image
            #     await KPoPPost.ImagePost(bot, newestImage) # Call KPoPPost.ImagePost() Function
            #     lastImage = newestImage # Update last Image
            
            if newestImage != lastKPOPImagesList[currentLinkIndex]:
                await KPoPPost.ImagePost(bot, newestImage) # Call KPoPPost.ImagePost() Function
                lastKPOPImagesList[currentLinkIndex] = newestImage # Update the last Image for current KPoP
    
    #return newestImage, isNew, lastImage


#TrackImage()
#print("NEW" , newestImage)
#print("Old: ", lastImage)