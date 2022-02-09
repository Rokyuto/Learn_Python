from tkinter import *  # Import tkinter gui library

x_loc = 0
y_loc = 0

program = Tk()  # Create Program
program.title("Drawing")  # Set Program Title
program.geometry("800x800")  # Set Program Size
program.configure(bg='black')  # Set Program Background
program.resizable(width=False, height=False)
canvas = Canvas(program, height=800, width=800, bg="black")
canvas.pack()

rect = canvas.create_rectangle(x_loc, y_loc, x_loc+100, y_loc+100, outline="purple", fill="green")

movement_step = 100


#  On Mouse Click
def movement(event):
    if event.keysym == 'Up':
        canvas.move(rect, 0, -movement_step)
    elif event.keysym == 'Down':
        canvas.move(rect, 0, +movement_step)
    elif event.keysym == 'Right':
        canvas.move(rect, +movement_step, 0)
    elif event.keysym == 'Left':
        canvas.move(rect, -movement_step, 0)


program.bind_all('<Key>', movement)  # Create Mouse Button 1 Click Binding

program.mainloop()  # Update/Refresh the Program
