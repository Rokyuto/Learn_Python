from bson.json_util import dumps
from pymongo import MongoClient
import json
import random
from overideCollection import f_GetDatabaseQuestions

data = ""
TestList = []
   
f_GetDatabaseQuestions() # Call f_GetDatabaseQuestions function form overideCollection.py to get Database Questions
        
with open('TestGenerator/DatabaseCollection.json', 'r') as file: # Open Collection.json file in read mode
    data = json.load(file) # Load the all data from the file and override data variable

def f_GenerateRandomQuestions():
    testSize = int(input("Enter Questions Quantity: ")) # Enter Questions Quantity
    for i in range(testSize): # Iterator
        randomIndex = random.choice(list(data)) # Get random key/index from the converted to list data
        TestList.append(data.get(randomIndex)) # Get the generated key value and append it to TestList
        data.pop(str(randomIndex)) # Remove the generated key from the data
    f_PrintQuestions() # When the iterator ends, call Function to Update the txt document with the Questions
    
def f_PrintQuestions():
    with open('TestGenerator/TestQuestions.txt', 'w') as file: # Open TestQuestions.txt in write mode
        for question in TestList: # Iterate the TestList, who contains the Random Generated Questions
            file.write("%s \n" % question) # Frite the Current Question to the txt file
              
f_GenerateRandomQuestions() # After the f_GetDatabaseQuestions function Ends, this function is called