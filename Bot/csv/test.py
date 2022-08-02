import sys
import re
import csv
import os

kpop = 'group'

def f_ClearKPoPList(index,kpop):
    filter=open("e:/Work/#Code Projects/Python/Bot/csv/filter.csv","r") # Open filter.csv in read mode
    csvReader=csv.reader(filter) # Create csv reader object by the help of csv library for filter.csv
    tempList = [] # Temp List,who will be filled with not defined kpop category (idol/group), when the function is called
    testList = ['1','2']
    i=0
    for row in csvReader: # For each Row in the filter.csv
        print(row)
        
        
        row[3] = testList[i]
        i+=1       
        
        if (row[index]==kpop): # If column 2 (idol/group) of the row contains the defined kpop category (idol/group), then Skip (Continue)
            continue
        else:
            tempList.append(row) # Append the row to the tempList
            
    filter=open("e:/Work/#Code Projects/Python/Bot/csv/filter.csv","w",newline='') # Open filter.csv in write mode
    csvWriter=csv.writer(filter) # Create csv writer object by the help of csv library for filter.csv
    csvWriter.writerows(tempList) # Rewrite the filter.csv rows with the tempList
    filter.close() # Close the file
    tempList.clear() # Clear the tempList
    
    
def f_UpdateLastImage():
    filter=open("e:/Work/#Code Projects/Python/Bot/csv/filter.csv","w",newline='') # Open filter.csv in write mode
    csvWriter=csv.writer(filter)


def testFunc():
    f_ClearKPoPList(0,'irene')
    
    
#testFunc()


groupsList = []
idolsList = []

groupsLinksList = []
idolsLinksList = []

KPOPlist = []  # Total List with all Groups and Idols for Tracking
KPOPLinksList = []

def f_restoreLists():
    global groupsList, idolsList, groupsLinksList, idolsLinksList
    # If filter.csv document is not empty then fill Filters Lists
    if(os.path.getsize("e:/Work/#Code Projects/Python/Bot/csv/filter.csv") != 0 ):
        filterFile = open("e:/Work/#Code Projects/Python/Bot/csv/filter.csv", "r") # Open the csv document in read mode
        csvReader=csv.reader(filterFile)
        for line in csvReader: # Read Second Column (idol or group)
            idol = re.compile('idol') # searcher for the word 'idol'
            if(line[1] == idol): # If it's found the word 'idol' on any line
                idolsList.append(line[0]) # Append the name of the Idol (filter.csv first column) to idolsList
                idolsLinksList.append(line[2]) # Append the Idol Link (filter.csv third column) to idolsLinksList
            else:
                groupsList.append(line[0]) # Append the name of the Group (filter.csv first column) to groupsList
                groupsLinksList.append(line[2]) # Append the Group Link (filter.csv third column) to groupsLinksList
                
        KPOPlist.extend(groupsList)
        KPOPlist.extend(idolsList)

        KPOPLinksList.extend(groupsLinksList)
        KPOPLinksList.extend(idolsLinksList)
        
        print(KPOPlist)
        print(KPOPLinksList)
        
    
#f_restoreLists()

lastKPOPImagesList = []
file_lastFilterImages = open("e:/Work/#Code Projects/Python/Bot/csv/filter.csv", "r") # Open file
csvReader = csv.reader(file_lastFilterImages)
for line in csvReader:
    
    lastKPOPImagesList.append(line[3])

print(lastKPOPImagesList)