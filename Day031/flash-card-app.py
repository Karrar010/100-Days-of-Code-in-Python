from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_list = []

# Getting Values From File
try:
    dataframe = pandas.read_csv("./Day31/data/words_to_learn.csv")
except:
    original_dataframe = pandas.read_csv("./Day31/data/french_words.csv")
    data_list = original_dataframe.to_dict(orient= "records")
else:
    data_list = dataframe.to_dict(orient="records")

def show_french_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(data_list)
    canvas.itemconfig(card_background,image = card_front)
    canvas.itemconfig(card_title,text = "French",fill = "black")
    canvas.itemconfig(card_word,text =  current_card["French"], fill= "black")
    
    flip_timer= window.after(3000,func=show_english_card)

def show_english_card():
    canvas.itemconfig(card_title,text = "English",fill= "white")
    canvas.itemconfig(card_word,text =  current_card["English"],fill= "white")
    canvas.itemconfig(card_background, image = card_back) 

def known_french_card():
    data_list.remove(current_card)
    print(len(data_list))
    dataframe = pandas.DataFrame(data_list)
    dataframe.to_csv("./Day31/data/words_to_learn.csv", index=False)#index= false doesnot add record/row numbers to csv file everytime we run code
    show_french_card()

# ----------------------- UI --------------------------
window = Tk()
window.title("Flash Card App")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=show_english_card)

# CARD
canvas = Canvas(height=526,width=800, bg= BACKGROUND_COLOR, highlightthickness=0) 
card_front =  PhotoImage(file="./Day31/images/card_front.png")
card_back =  PhotoImage(file="./Day31/images/card_back.png")
card_background = canvas.create_image(400,263,image = card_front) 
card_title = canvas.create_text(400,158,text="Title",font=("Arial",40,"italic"))
card_word = canvas.create_text(400,263,text="Word",font=("Arial",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0, columnspan=2)


# BUTTONS
wrong_img = PhotoImage(file="./Day31/images/wrong.png")
wrong_btn = Button(image= wrong_img,highlightthickness=0,command=show_french_card)
wrong_btn.grid(row= 1,column=0)

right_img = PhotoImage(file="./Day31/images/right.png")
right_btn = Button(image= right_img, highlightthickness=0,command=known_french_card)
right_btn.grid(column=1,row=1)


show_french_card()


window.mainloop()