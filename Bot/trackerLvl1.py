import os
import requests
from bs4 import BeautifulSoup

editNewestImage = ""

def TrackImage():
    # Find Images Saving Directory (Folder)
    folderPath = os.path.dirname('Images/') # If running the code from VS Code dirname must be 'Bot/Images/'

    # Change the Current Working Directory to the Given Directory (Images Saving Directory)
    os.chdir(os.path.join(os.getcwd(), folderPath)) # Now all work with files will be done in this directory

    SavedImage = "" # Variable for the stored image in the Saving Directory
    isEmpty = True # Variable to check if the Saveing Image Directory is empty

    with os.scandir(os.getcwd()) as dirs: # Scan the current working directory (Saving Directory)
        for entry in dirs: # for each finded object
            isEmpty = False # Directory is not empty
            SavedImage = entry.name # Update Saved Image

    URL = 'https://kpopping.com/kpics/gender-female/category-all/idol-any/group-any/order' # Website URL

    page = requests.get(URL) # Call the Website

    soup = BeautifulSoup(page._content, 'html.parser') # Parse the Website to be able to get information || Get all information in the website 

    images = soup.find(class_='box pics infinite') # Get Container with all Idols Images

    newestCategory = images.find(class_='matrix matrix-breezy mb-2') # Get the Newest Children Idols Images Container

    newestElement  = newestCategory.find(class_='cell') # Get the Newest Element in the Category

    newestImage = newestElement.find('img') # Get the Image in the Newest Element

    newestImageName = newestImage['alt'] # Newest Image Name

    newestImageLink = newestImage['src'] # Newest Image Source

    editNewestImage = newestImageName.replace(' ', '-').replace('/','') + '.jpg' # Change Image Name

    if editNewestImage != SavedImage: # If the founded newest Image in the Website doesn't exists in the Saving Directory
        # Open the Last Image' Name
        with open (editNewestImage , 'wb') as f:
            img = requests.get("https://kpopping.com% s" % newestImageLink) # Get Full Image Source and Download it 
            
            if isEmpty == False:
                # Delete the old Saved Image
                os.remove(SavedImage)
            
            f.write(img.content) # Create File (Image) in the Current Directory (Saving Directory)
            print("Writing: " , newestImageName) # Debug print
            SavedImage = editNewestImage # Update the Saved Image to the Newest Image in the Website
            
            # Change the Current Directory to the file (tracker.py) Directory
            #trackerDir = os.chdir(os.path.dirname(__file__))
            
    else: # If the founded newest Image in the Website already exists in the Saving Directory
        print("The Image Already Exists")
        
    # Change the Current Directory to the Project (Bot) Directory
    os.chdir(os.path.dirname(__file__))
    #print("Current Directory: " , os.getcwd())