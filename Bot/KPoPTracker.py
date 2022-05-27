import os
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
import KPoPPost

#global newestImage
lastImage = None # Last Image Initial Value
newestElementHREF = None # Last Image Initial Value
lastKPOPImages = [] # List with Last Image for each KPOP Link

def FindNewestImage():
    global newestElementHREF
    URL = 'https://kpopping.com/kpics/gender-female/category-all/idol-any/group-any/order' # Website URL

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
    if (len(KPOPLinksList) > 0): # If TRUE then it will go Check for new Images in this Link
        #for link in KPOPLinksList:          
        global lastImage # Initialize Last Image
        FindNewestImage() # Call Finding Newest Image href function
        
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
        
        if newestImage != lastImage: # If the newest image is not the same as the last image
            await KPoPPost.ImagePost(bot, newestImage) # Call KPoPPost.ImagePost() Function
            lastImage = newestImage # Update last Image
    
    #return newestImage, isNew, lastImage


#TrackImage()
#print("NEW" , newestImage)
#print("Old: ", lastImage)