from tkinter import *  # Import tkinter gui library
from PIL import ImageTk,Image

program = Tk()  # Create Program
program.title("Calculator")
program.iconbitmap('W:/#Assets/Calculator_Icon.ico')
program.config(bg='#333')

default_button_img = PhotoImage(file = 'W:/#Assets/Default_Button.png')
clear_button_img = PhotoImage(file = 'W:/#Assets/Clear_Button.png')
equal_button_img = PhotoImage(file = 'W:/#Assets/Equal_Button.png')

entry = Entry(program, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = entry.get()  # Set the new input to the current
    entry.delete(0, END)  # Delete the last entered number
    entry.insert(0, str(current) + str(number))  # Add a new number to the other


def button_clear():
    entry.delete(0, END)


def button_add():
    first_number = entry.get()  # Read First Num Input
    global f_num
    global math
    math = "addition"  # Set the math action
    f_num = float(first_number)   # Save the Input as Variable
    entry.delete(0, END)  # Delete it from the input


def button_equal():
    second_number = entry.get()  # Read the second Input
    entry.delete(0, END)  # Delete it
    global f_num
    if math == "addition":
        result = entry.insert(0, f_num + int(second_number))  # Calculate the two numbers (+)
    if math == "subtraction":
        result = entry.insert(0, f_num - int(second_number))  # Calculate the two numbers (-)
    if math == "multiplication":
        result = entry.insert(0, f_num * int(second_number))  # Calculate the two numbers (*)
    if math == "division":
        result = entry.insert(0, f_num / int(second_number))  # Calculate the two numbers (/)

    f_num = result  # Save the result as the new First Num Input


def button_subtract():
    first_number = entry.get()  # Read First Num Input
    global f_num
    global math
    math = "subtraction"  # Set the math action
    f_num = float(first_number)  # Save the Input as Variable
    entry.delete(0, END)  # Delete it from the input


def button_multiply():
    first_number = entry.get()  # Read First Num Input
    global f_num
    global math
    math = "multiplication"  # Set the math action
    f_num = float(first_number)  # Save the Input as Variable
    entry.delete(0, END)  # Delete it from the input


def button_divide():
    first_number = entry.get()  # Read First Num Input
    global f_num
    global math
    math = "division"  # Set the math action
    f_num = float(first_number)  # Save the Input as Variable
    entry.delete(0, END)  # Delete it from the input


# Create Buttons
button_1 = Button(program, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(program, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(program, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(program, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(program, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(program, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(program, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(program, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(program, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(program, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(program, text="+", padx=38, pady=85, command=button_add)
button_equal = Button(program, text="=", padx=86, pady=20, command=button_equal)
button_clear = Button(program, text="Clear", padx=77, pady=20, command=button_clear)

button_subtract = Button(program, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = Button(program, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(program, text="/", padx=41, pady=20, command=button_divide)

# Display Buttons
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_0.grid(row=5, column=0)

button_clear.grid(row=1, column=0, columnspan=2)
button_add.grid(row=3, column=3, rowspan=3)
button_equal.grid(row=5, column=1, columnspan=2)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=1, column=3)
button_divide.grid(row=1, column=2)

program.mainloop()
