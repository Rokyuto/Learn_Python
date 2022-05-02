import requests

# API = Application User Interface
API_KEY = "1b63f0b176bdbd207fe71d449e72ab24" # API Weather Key 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather" # API URL

city = input("Enter city: ")
# f - To Embed variables and expressions
# q = query
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}" # Get Data for the entered city
response = requests.get(request_url) # Send request and return information about the entered city

# If the response is successful
if response.status_code == 200:
    # Get the data for the entered city
    data = response.json() # Convert the responce to a JSON object and Give you a JSON data as Python Dictionary
    
    # Get Weather Key and Information on him from the list of the city data
    weather = data["weather"][0]["description"] # Get First Element in the Weather Key and Get Description Information
    
    # Get Main Key / Temperature Key / Information on him from the list of the city data
    temperature = round(data["main"]["temp"] - 273.15, 2) # In Celsius || Formated to second decimal number
    
    # Print
    print("Weather:", weather)
    print("Temperature:" , temperature , "°C")
    
else:
    print("An Error occurred.")
   
    