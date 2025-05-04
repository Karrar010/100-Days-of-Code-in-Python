# There are three layout managers for Tkinter 1. Pack , 2. Place , 3. Grid

#1. Pack: places the tkinter widgets next to each other (when i say widgets i means the labels,entry,button etc)

#2. Place: with this we place widget anywhere on the window by specifying the X and Y coordinate 

#3. Grid: grid layout manager imagins the whole window as a grid/table with rows and columns and points widgets to appropriate locations
# grid allocation is relative to other widgets (depends on other widgets)

#TIP: DONOT USE BOTH PACK AND GRID TOGETHER IN CODE

from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# window.config(padx=100, pady=200)   #this property padx,pady adds padding along all sides of our widget(here window)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50) #this property padx,pady adds padding along all sides of our widget

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)









window.mainloop()