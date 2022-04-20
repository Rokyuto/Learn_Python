from tkinter import *  # Import tkinter gui library
from tkinter import filedialog

# Create File Function
def createFile():
    # Set Default Path / Directory to create File
    filepath = filedialog.asksaveasfilename(initialdir="C:\\Users\\pc\\Desktop") 
    file = open(filepath, 'w')
   
#GUI 
window = Tk() # Window
window.title("Create File")
window.geometry('350x150+700+200')
button = Button(text="Create File", command=createFile, height=10, width=20,bg='#567', fg='White', font=('Arial', 14 )).pack(pady=10) # Button with command to create Folder
#button.pack()
window.mainloop()
 
 