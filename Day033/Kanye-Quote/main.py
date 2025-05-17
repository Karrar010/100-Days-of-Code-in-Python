from tkinter import *
import requests

def get_quote():
    response_api = requests.get(url="https://api.kanye.rest")
    response_api.raise_for_status() # for showing error
    # print(response_api.json())
    kanye_quote = response_api.json()['quote']
    canvas.itemconfig(quote_text, text = kanye_quote)



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="./Day33/Kanye-Quote/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="./Day33/Kanye-Quote/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

reminder = Label(text="{ Press on Kanye to get a Quote }")
reminder.grid(row=2,column=0)

window.mainloop()