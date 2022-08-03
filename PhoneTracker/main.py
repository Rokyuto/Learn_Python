import phonenumbers
from myphone import number
from phonenumbers import geocoder
from phonenumbers import carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import folium

parseNumber = phonenumbers.parse(number)

location = geocoder.description_for_number(parseNumber, "en") # Get Country Location of the phone number
print(location)

serviceProvider = carrier.name_for_number(parseNumber,"en") # Get phone Number Service Provider (Telenor)
print(serviceProvider)

# Get All Country Information
key = '66df5746c2c3404cb766bffc56cde252' # OpenCage Account Key
_geocoder = OpenCageGeocode(key)
query = str(location)
results = _geocoder.geocode(query)
print(results)

# Get Phone Number World Coord
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location=[lat,lng],zoom_start = 9)
folium.Marker([lat,lng],popup=location).add_to(myMap)
myMap.save("PhoneTracker/myLocation.html")