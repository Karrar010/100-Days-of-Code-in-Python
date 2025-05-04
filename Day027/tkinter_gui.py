#Just like previous turtle library similarly the tkinter library works
#It is a Python library for GUI representation
import tkinter

#similar to turtle we need a screen to show the GUI
window = tkinter.Tk()
window.title("First Tkinter GUI")
window.minsize(width=500,height=300) #parameters are set for the screen, by this screen will by defualt accommodate all widgets on screen

#to write something on screen we need the label() class from tkinter library
my_screen_label = tkinter.Label(text="Hello World!",font=('Arial',24,'bold'))#only this doesnot show the text on screen as it requires other func
# print(type(my_screen_label))
# my_screen_label.pack()  #this shows text on screen and by defualt it sets side= 'top'
my_screen_label.pack(side= 'left') 

# my_screen_label['text']  = 'Goodbye World!' #we can also manupulate the text= property of label 
my_screen_label.config(text= 'Hello Bye')




window.mainloop()#mainloop is similar to exitonclick() func and its written at the end of all code and it keeps showing the window

# You will get an error like this
# window = tkinter.Tk()
#              ^^^^^^^^^^
# AttributeError: partially initialized module 'tkinter' has no attribute 'Tk' (most likely due to a circular import)
#solv: this happens because you named the file tkinter.py so rename it to avoid this