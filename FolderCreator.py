# importing os module - Operating System
import os
  
# Directory Name
directory = "Folder Creator"
  
# Parent Directory path
parent_dir = "C:/Users/pc/Desktop/"
  
# Path
path = os.path.join(parent_dir, directory)
  
# Create the directory
# 'Folder Creator' in
os.mkdir(path)

# Print For Success
print("Directory '% s' created" % directory)
  