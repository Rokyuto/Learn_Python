# Open text.txt and set mode for the file to WRITE
from turtle import clear


file = open("text.txt","w")
text = "Hello World"

# Write String Text
for i in text:
    file.write(i)
    
file.write("\n")

oceans = ["Pacific", "Atlantic", "Indian" , "Southern" , "Arctic"]

# Write each element from the List on new Row
for ocean in oceans:
    file.write(ocean)
    file.write("\n")
    