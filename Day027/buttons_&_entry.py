import tkinter

import tkinter.test
# from tkinter import * for importing all classes of tkinter
window = tkinter.Tk()
window.title("First Tkinter GUI")
window.minsize(width=500,height=300) 

# LABEL
my_screen_label = tkinter.Label(text="Hello World!",font=('Arial',24,'bold'))
my_screen_label.pack() 
# my_screen_label.config(text= 'Hello Bye')



# BUTTON

def button_clicked():   #this func acts as an as event listener like in turtle and when button is clicked then command trigger this function
    print('I got clicked') # inc console this will be printed

    #challenge: make the 'i got clicked' str appear instead of 'Hello world' on screen
    # my_screen_label.config(text= 'Button got clicked')

    #challenge: when text entered in entry then button is clicked change text of my label to that entry text
    my_screen_label.config(text = enter_text.get())  #get command in Entry class prints out the string input by user 

button = tkinter.Button(text='Click Me', command=button_clicked) # with command we only write the name of function and  we donot call it
button.pack() #for the button click me to appear


# ENTRY

enter_text = tkinter.Entry(width= 25)  #this class takes input from user
enter_text.pack()
print( enter_text.get())  #get command in Entry class prints out the string input by user , but this print wont print anything idk 


window.mainloop()

