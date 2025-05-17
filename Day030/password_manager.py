import tkinter
import tkinter.messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def password_generator():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []  #password size is from min 12 char to max 18 char
    password_letters = [random.choice(letters) for char in range(nr_letters) ] #list comprehension
    password_numbers = [random.choice(numbers) for char in range(nr_numbers) ] 
    password_symbols = [random.choice(symbols) for char in range(nr_symbols) ]
    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0,password) 
    pyperclip.copy(password)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    website = website_input.get()
    try:
        with open(file="./Day30/password_data.json") as data_file: 
            data = json.load(data_file) #read json file

    except FileNotFoundError: #exception handling when there is no json file and search btn in clicked
        tkinter.messagebox.showerror(title="Error", message="No data file found")
    else:
        if website in data:
            password_in_json = data[website]["password"]
            email_in_json = data[website]["email"]
            tkinter.messagebox.showinfo(title = f"{website}", message = f"Email: {email_in_json}\nPassword: {password_in_json}")
        else:
            tkinter.messagebox.showerror(title="Error", message="No details found")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data_to_file():
    new_data = {
        website_input.get() : {
            "email" : user_detail_input.get(),
            "password" : password_input.get()
        }
    }
    if len(website_input.get()) == 0 or len(user_detail_input.get()) == 0 or len(password_input.get()) == 0:
        warning = tkinter.messagebox.showinfo(title = "Warning", message = "Enter your details, Don't leave fields empty")
        print("Enter Details Please")

    else:
        try:
            with open(file="./Day30/password_data.json",mode="r") as data_file:
                # Read Json file into data dict
                data = json.load(data_file)
        except FileNotFoundError:
            with open(file="./Day30/password_data.json",mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
    
        else:
            # Updating old data with new data in json
            data.update(new_data)
                
            with open(file="./Day30/password_data.json",mode="w") as data_file:
                # Write dict with new data into Json file
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0,50) 
            password_input.delete(0,50)
            print("Password Added to File")
    




# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx= 50, pady= 50)

# image on canvas
my_canvas = tkinter.Canvas(height=200 , width=200)  
my_image = tkinter.PhotoImage(file="./Day30/logo.png")
my_canvas.create_image(100,100,image=my_image)
my_canvas.grid(column=1,row=0)
#text on window
website_txt = tkinter.Label(text="Website: ")
website_txt.grid(column=0,row=1)

user_detail_txt = tkinter.Label(text="Username/Email: ")
user_detail_txt.grid(column=0,row=2)

password_txt = tkinter.Label(text="Password: ")
password_txt.grid(column=0,row=3)

#website name input
website_input = tkinter.Entry(width=34)
website_input.grid(column=1,row=1)
website_input.focus()#using this when gui has started, one can directly start typing in this Entry
#user detail input
user_detail_input = tkinter.Entry(width=54)
user_detail_input.grid(column=1,row=2,columnspan=2)
user_detail_input.insert(0,"yashkun@gmail.com")#this shows up in this entry from the start of GUI

#password input
password_input = tkinter.Entry(width=34)
password_input.grid(column= 1,row=3 )


#Buttons on window

# search webpage button
search_password_btn = tkinter.Button(text="Search",width=15,command=search)
search_password_btn.grid(column=2,row=1)

#password generation button
generate_password_btn = tkinter.Button(text="Password Generator",command=password_generator)
generate_password_btn.grid(column=2,row=3)

#add password to text.file button
add_btn = tkinter.Button(text="Add",width=46,command=add_data_to_file)
add_btn.grid(column=1,row=5,columnspan=2) 


window.mainloop()