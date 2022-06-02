import cv2
import os

# QR-Code Folder Directory
currentDirectory = "W:\\#Code_Projects\\Python\\QR-Code"
# Change the working directory to QR-Code folder
os.chdir(currentDirectory)
# read the QRCODE image
qrCode = cv2.imread("qrCode.png")

# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

# detect and decode
data, bbox, straight_qrcode = detector.detectAndDecode(qrCode) # data will find the site who is stored in the QRCODE

print(data)