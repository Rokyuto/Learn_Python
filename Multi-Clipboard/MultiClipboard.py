import sys
import clipboard
import json

#command = sys.argv[0] # Python File
SAVED_DATA = 'Multi-Clipboard\clipboard.json' # clipboard file directory (clipboard.json)

# Save data function
def save_data(filepath, data):
    with open(filepath, 'w') as file: # If file already exist rewrite him, in not exist - create file
        json.dump(data, file) # Rewrite data in the file

#Load data function
def load_data(filepath):
    try: # Try to open dictionary
        with open(filepath, 'r') as file: # Open and read file
            data = json.load(file) # Update data variable with the data from the file
            return data
    except: # If there is no dictionary
        return {} # Return empty dictionary

if(len(sys.argv) == 2): # If terminal has 2 arguments - python file and command
    command = sys.argv[1] # Update command variable to command entered in the terminal
    data = load_data(SAVED_DATA) # Set data variable value to command entered in the terminal

    if command == "save":
        key = input("Enter a key: ") # Ask for name of the dictionary key
        data[key] = clipboard.paste() # Overwrite the data on the key to the clipboard data 
        save_data(SAVED_DATA, data) # Call save command to overwrite the data in the clipboard file(clipboard.json = SAVED_DATA)
        print("Data saved!")
        
    elif command == "load":
        key = input("Enter a key: ") # Ask for name of the dictionary key
        if key in data: # If the entered key is a data dictionary key
            clipboard.copy(data[key]) # Copy the data on the key in the dictionary to the clipboard
            print("Data copied from the clipboard!")
        else:
            print("Key does not exist!")
            
    elif command == "list":
        print(data)
    else:
        print("Unknown command")
        
else:
    print("Please enter exactly one command")