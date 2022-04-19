from tkinter import *  # Import tkinter gui library
from tkinter import filedialog

# Create Folder Function
def createFolder():
    # Set Default Path / Directory to create Folder
    filepath = filedialog.askdirectory(initialdir="C:\\Users\\pc\\Desktop")
    # Show the Directory
    print(window.filepath)
 
   
#GUI 
window = Tk() # Window
window.title("Create Folder")
window.geometry('350x150+700+200')
button = Button(text="Create Folder", command=createFolder, height=10, width=20,bg='#567', fg='White', font=('Arial', 14 )).pack(pady=10) # Button with command to create Folder
#button.pack()
window.mainloop()
 
 