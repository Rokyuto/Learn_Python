from tkinter import *  # Import tkinter gui library
from tkinter import filedialog

def createFile():
    filepath = filedialog.asksaveasfilename(initialdir="C:\\Users\\pc\\Desktop")
    file = open(filepath, 'w')
    print(file.write())
    file.close()
    
window = Tk()
button = Button(text="Create", command=createFile)
button.pack()
window.mainloop()
 
 