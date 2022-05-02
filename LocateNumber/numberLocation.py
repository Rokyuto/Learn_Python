import phonenumbers
#import opencage
#import folium
from phonenumbers import geocoder
#from Numbers import myNumber
import subprocess

numberFile = 'python LocateNumber\\Numbers.py'
openNumber = subprocess.Popen(numberFile)
out, err = openNumber.communicate()

from Numbers import myNumber

valid = phonenumbers.is_valid_number(phonenumbers.parse(myNumber)) # Check if phone number is valid
posible = phonenumbers.is_possible_number(phonenumbers.parse(myNumber)) # Check if phone number is possible

if valid & posible:
    Number = phonenumbers.parse(myNumber) # Parse the number to Country Code and Number
    numLocation = geocoder.description_for_number(Number, "en") # Get the Country Location of the number in English language
 
    print("Country Location for the following number is: " + numLocation)

    # Get the Service Provider
    from phonenumbers import carrier # Library for initializing the Provider for the phone number

    serviceProvider = carrier.name_for_number(Number, "en") # Get the Service Provider
    print("Service Provider for the following number is: " + serviceProvider) # Print

"""# Get Number Global Location
from opencage.geocoder import OpenCageGeocoder

key = '66df5746c2c3404cb766bffc56cde252' # Key for my OpenCage Account

geocoder = OpenCageGeocoder(key)

# Conver the Number in string format and create Query object
query = str(numLocation)

# Get all information about the Query (Number)
results = geocoder.geocode(query)

# Get World / Global Location of the Number
latitude = results[0]['geometry']['lat'] # Географска ширина
lognitude = results[0]['geometry']['lng'] # Географска дължина

# Snap to the location in the World
myMap = folium.Map(location=[latitude,lognitude], zoom_start=9)

# Create a marker 
folium.Marker([latitude,lognitude],popup=numLocation).add_to(myMap)

# Save the Map in HTML file
myMap.save("myLocation.html")"""
