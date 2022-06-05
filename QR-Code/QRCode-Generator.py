import qrcode
import os

# Site
site = "https://github.com/Rokyuto" # My Site -  - http://rokyuto.hopto.org/Home.html
# QR Code Image name
filename = "qrCode.png"
# Create a QR Code
img = qrcode.make(site)
# QR-Code Folder Directory
currentDirectory = "W:\\#Code_Projects\\Python\\QR-Code"
# Change the working directory to QR-Code folder
os.chdir(currentDirectory)
# Save the QR Code image
img.save(filename)

